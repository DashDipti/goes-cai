import os 
import re
import requests
import time

from __future__ import print_function

import cmlapi
from cmlapi.rest import ApiException

PROJECT_NAME_PREFIX = os.environ["PROJECT_NAME_PREFIX"]
KEYCLOAK_CDP_GROUP = os.environ.get("KEYCLOAK_CDP_GROUP")
LABUSERNAME_PREFIX = os.environ["LABUSERNAME_PREFIX"]
NUM_PROJECTS = int(os.environ["NUM_USERS"])
TEAM = os.environ["TEAM_NAME"]

CDSW_API_URL=os.getenv('CDSW_API_URL')
CDSW_API_KEY=os.getenv('CDSW_API_KEY')

api = cmlapi.default_client()

def run_team_sync() -> bool:
    """
    Wait for team sync to complete by polling the sync status.
    Returns True if sync completed successfully, False otherwise.
    """
    # Run sync team operation
    requests.patch(f'{CDSW_API_URL}/site/teams', 
        headers={'content-type': 'application/json'}, 
        auth=(CDSW_API_KEY, ''), 
        json={})
    print("Waiting for team sync to complete...")
    max_attempts = 30  # Maximum attempts (5 minutes at 10 second intervals)
    attempt = 0
    
    while attempt < max_attempts:
        try:
            sync_status = api.teams_sync_status()
            status = sync_status.status
            print(f"Sync attempt {attempt + 1}: Status = {status}")
            
            if status == 'success':
                print(f"✅ Team sync completed successfully!")
                print(f"Message: {sync_status.message}")
                print(f"Total synced users: {sync_status.total_synced_users}")
                return True
            elif status == 'failed':
                print(f"❌ Team sync failed: {sync_status.message}")
                return False
            else:
                print(f"⏳ Sync in progress... waiting 10 seconds")
                time.sleep(10)
                attempt += 1
                
        except ApiException as e:
            print(f"⚠️ Error checking sync status: {e}")
            time.sleep(10)
            attempt += 1
    
    print(f"⚠️ Sync did not complete within {max_attempts * 10 / 60} minutes")
    return False

def ensure_team_exists(team_name: str, sync_team: bool = False) -> None:
    """
    Create the team if it doesn't exist. 
    If sync_team is True then creates a Create a synced team.
    Swallow common 'already exists'
    variants across CML deployments so the script never crashes on duplicates.
    """
    print(f"Ensuring team exists: {team_name}")
    
    if sync_team:
        # Try to create a synced team if specified
        try:
            api.create_synced_team(cmlapi.CreateSyncedTeamRequest(username=team_name, group_permissions=[{"cn": team_name, "permission":"admin"}]))
            print(f"Created synced team: {team_name}")
        except ApiException as e:
            status = getattr(e, "status", None)
            text = (getattr(e, "body", None) or str(e) or "").lower()
            
            # Handle team already exists cases (including 500 errors for existing synced teams)
            if status in (400, 409, 500) or "exist" in text or "already" in text or "duplicate" in text:
                print(f"Synced team '{team_name}' may already exist (HTTP {status}). Proceeding with sync.")
            else:
                print(f"⚠️ Could not create synced team '{team_name}' (HTTP {status}): {e}")
                # Don't return here - still try to run sync in case team exists
        
        # Always run sync for synced teams (whether creation succeeded or team already existed)
        if not run_team_sync():
            print(f"⚠️ Team sync did not complete successfully for {team_name}")
    else:
        # Create a regular team
        try:
            api.create_team(cmlapi.CreateTeamRequest(username=team_name))
            print(f"Created team: {team_name}")
        except ApiException as e:
            status = getattr(e, "status", None)
            # Some environments return a message in e.body, others only in str(e)
            text = (getattr(e, "body", None) or str(e) or "").lower()

            # Treat 400/409 or any message that looks like "already exists" as success
            if status in (400, 409) or "exist" in text or "already" in text or "duplicate" in text:
                print(f"Team '{team_name}' already exists (HTTP {status}). Proceeding.")
            else:
                # Log and continue rather than crashing the whole run
                print(f"⚠️ Could not create team '{team_name}' (HTTP {status}): {e}")
                # If you prefer to fail hard on unexpected statuses, replace with: raise

def find_project_by_prefix_bounded(prefix: str):
    """
    Match 'AgentLab N' followed by a word boundary, e.g. 'AgentLab 1' matches
    'AgentLab 1 - ecole' but NOT 'AgentLab 10 ...'.
    """
    pattern = re.compile(rf"^{re.escape(prefix)}\b")
    try:
        projects = api.list_projects(search_filter='{"name":"' + PROJECT_NAME_PREFIX + '"}',include_all_projects=True,page_size=100).projects
        return next((p for p in projects if pattern.match(p.name)), None)
    except ApiException as e:
        print(f"❌ Failed to list projects: {e}")
        return None

def add_admin(project_id: str, principal: str):
    """Add collaborator with admin permission; swallow 'already has access' errors."""
    try:
        api.add_project_collaborator(
            cmlapi.AddProjectCollaboratorRequest(permission="admin"),
            project_id,
            principal,
        )
        print(f"  → Added admin: {principal}")
    except ApiException as e:
        status = getattr(e, "status", None)
        msg = (getattr(e, "body", None) or str(e) or "")
        if status in (400, 409):
            print(f"  (already has admin; HTTP {status})")
        elif status == 404:
            print(f"  ⚠️ Principal not found (404): {principal}")
        else:
            print(f"  ❌ Error adding '{principal}' (HTTP {status}): {msg}")

# --- main flow ---
ensure_team_exists(TEAM)
if KEYCLOAK_CDP_GROUP:
    print(f"Ensuring synced team for Keycloak group: {KEYCLOAK_CDP_GROUP}")
    # Ensure the Keycloak group exists, if specified
    ensure_team_exists(KEYCLOAK_CDP_GROUP, sync_team=True)

for i in range(1, NUM_PROJECTS + 1):
    project_name = f"{PROJECT_NAME_PREFIX}-{i:03d}"  # Changes format to AgentLab-001, AgentLab-002, etc.
    print(f"\nAssigning permissions to: {project_name}")

    target_project = find_project_by_prefix_bounded(project_name)
    if target_project is None:
        print(f"⚠️ Project not found with prefix '{project_name}'. Skipping.")
        continue

    target_user = f"{LABUSERNAME_PREFIX}{i:03d}"  # user001, user010, ...

    add_admin(target_project.id, target_user)
    add_admin(target_project.id, TEAM)