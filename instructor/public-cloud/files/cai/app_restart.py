from __future__ import print_function
import re
import cmlapi
from cmlapi.rest import ApiException
import os

PROJECT_NAME_PREFIX = os.environ["PROJECT_NAME_PREFIX"]
NUM_PROJECTS = int(os.environ["NUM_USERS"])


api = cmlapi.default_client()

def find_project_by_prefix_bounded(prefix: str):
    """
    Match prefix followed by a word boundary, e.g. 'AgentLab 1' matches
    'AgentLab 1 - ecole' but NOT 'AgentLab 10 ...'.
    """
    pattern = re.compile(rf"^{re.escape(prefix)}\b")
    try:
#        projects = api.list_projects(search_filter='{"name":"' + PROJECT_NAME_PREFIX + '"}',include_all_projects=True,page_size=100).projects
        projects = api.list_projects(include_all_projects=True,page_size=100).projects
        return next((p for p in projects if pattern.match(p.name)), None)
    except ApiException as e:
        print(f"❌ Failed to list projects: {e}")
        return None

def find_applications_for_project(project_id: str):
   """
   Finds all applications under a specified project
   """
   try:
      apps = api.list_applications(target_project.id)
      return apps.applications
   except ApiException as e:
        print(f"❌ Failed to list applications in project: {e}")
        return None

     
    
# --- main flow ---
for i in range(1, NUM_PROJECTS + 1):
  project_name = f"{PROJECT_NAME_PREFIX}-{i:03d}"  # Changes format to AgentLab-001, AgentLab-002, etc.
  print(f"\nRestart Applications in : {project_name}")

  target_project = find_project_by_prefix_bounded(project_name)

  app_list = find_applications_for_project(target_project.id)

  for app in app_list:

    try:
      api.restart_application(target_project.id, app.id)
      print(f"  → Restarted : {app.name} in Project : {target_project.name}")
    except ApiException as e:
      print(f"❌ Failed to restart application {app.id} in project {target_project.id}: {e}")