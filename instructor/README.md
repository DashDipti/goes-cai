# Instructor Guide for Cloudera AI Agentic Studio Hands On Lab

This guide provides detailed instructions on setting up the workshop environment.

## Hands on Lab Cloudera on CLoud Environment Setup

The `public-cloud/` folder contains Ansible playbooks and Terraform configuration files to setup the Cloudera on Cloud environment, data services. The setup playbooks also create assets required for the Hands on Lab.

> [!IMPORTANT]  
> The commands below are run from the `public-cloud/` directory this repository.

* Ensure Python virtual environment with `ansible-navigator` is activated. Sample commands are shown below.

```bash
python -m venv ~/cdp-navigator;
source ~/cdp-navigator/bin/activate;

pip install ansible-core ansible-navigator
```

>[!NOTE]
> You also will need either **Docker** or **Podman** up and running.

* Set the required environment variables.

```bash
export AWS_ACCESS_KEY_ID=your-aws-access-key-id
export AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
export AWS_SESSION_TOKEN=your-aws-session-token # (optional if using AWS SSO)
export CDP_ACCESS_KEY_ID=your-cdp-access-key-id
export CDP_PRIVATE_KEY=your-cdp-private-key
```

* Copy `config-template.yml` to `config.yml` and update the parameters as required.

   ```bash
   cp config-template.yml config.yml
   ```

* Notably, you should add and/or change the below parameters. The Data Services configurations (e.g. GPU for CML) can be edited in the config.yml file.

```yaml
prefix: "<ENTER_VALUE>" # Short prefix to append to all resources created
owner_email: "<ENTER_VALUE>"
infra_region:   us-east-2 # CSP region for infra

owner_email: "<ENTER_VALUE>"           # email address of owner

# Your Cloudera AI API key (known only after workspace is created)
# Only used in the setup-hol-assets.yml playbook; ignored in other playbooks
ml_workspace_api_key: "<ENTER_VALUE>"

# Number of Cloudera AI projects to create
num_projects: 5
```

* To setup the environment and datalake run the command below.

```bash
ansible-navigator run setup-cdp-env.yml -e @./config.yml
```

* To enable the required data services run the command below.

```bash
ansible-navigator run setup-cdp-services.yml -e @./config.yml
```

* To update the data and configure the assets required for the hands on lab run the command below.

> [!NOTE]  
> This module/playbook requires a Cloudera AI API key for the AI Workbench.
> :exclamation: The API key needs to have both **API** and **Application** scopes.
> Before running, ensure you have updated the `ml_workspace_api_key` variable in the configuration file with your valid API key.
> Once configured, you can execute this playbook as intended.

```bash
ansible-navigator run setup-hol-assets.yml -e @./config.yml
```

### Assigning Lab Atteendees to Cloudera on Cloud Group

By default a `{{ prefix }}-attendee` Cloudera on Cloud group is created as part of the environment setup. This group has the roles and resource roles to complete each of the lab exercises.

Before the lab, you will need to assign the attendee users to this group. Then run **Synchronize Users** for the Hands on Lab Cloudera on cloud environment.

Alternatively, if users are logging in via Keycloak, we should update the configuration file, `config.yml`, with the Keycloak group name so that users are automatically added when they login via their Keycloak account. A sample of the required changes to the configuration file is shown below.

```yaml
cdp_attendee_group:
  name: "<KEYCLOAK_GROUP_NAME>" # NOTE: This can be a pre-existing group aligning with the Keycloak realm
  create_group: no
  add_to_idbroker: yes
  sync_on_login: no
...
```

### Teardown

The cleanup is split into three separate playbooks - one to cleanup tghe hands on lab assets; one to remove all Data Services and the third to remove the Cloudera Environment and infrastructure.

Tear down hands on lab assets by running the following command:

> [!NOTE]  
> This module/playbook requires a Cloudera AI API key for the AI Workbench.
> Before running, ensure you have updated the `ml_workspace_api_key` variable in the configuration file with your valid API key.
> Once configured, you can execute this playbook as intended.

```bash
ansible-navigator run teardown-hol-assets.yml -e @./config.yml
```

Tear down data services by running the following command:

```bash
ansible-navigator run teardown-cdp-services.yml -e @./config.yml
```

Tear down the CDP environment and infrastructure by running the command below:

```bash
ansible-navigator run teardown-cdp-env.yml -e @./config.yml
```

### Known Issues / Manual Steps

| Issue | Description | Workaround |
|-------|-------------|------------|
| Cloudera AI Project permissions. | Automation to assign HoL users as collaborators on different projects is not yet available. | Manually assign user the Collaborator role in the assigned Cloudera AI project |

## Viewing and Publishing the Workshop Guide

Two methods are available to publish this lab guide to GitHub pages - a GitHub Action (recommended) and manually publishing.

> [!NOTE]  
> Follow the manual steps to test your guide locally (via the `mkdocs serve` command).

### Using GitHub Action

The [publish_mkdocs.yml](../.github/workflows/publish_mkdocs.yml) GitHub action is used to automatically publish the the lab guide to GitHub pages.

The action is triggered on a push to the `main` branch. The action can also be launched manually if required.

### Steps to manually publish the guide

* Create a Python Virtual Environment

   ```bash
   python3 -m venv ~/mkdocs_venv
   source ~/mkdocs_venv/bin/activate
   ```

* Clone the hol-005-agentic-studio GitHub repository

  ```bash
  git clone https://github.infra.cloudera.com/GOES/hol-005-agentic-studio.git
  ```

* Install Required Dependencies for MkDocs

   ```bash
   cd hol-005-agentic-studio/instructor/mkdocs
   pip install -r requirements.txt
   ```

* Run the following command to test your guide locally:

   ```bash
   mkdocs serve
   ```

   Open `http://127.0.0.1:8000` in your browser to view the guide.

* Use the following command to publish the guide to the `origin` repository's GitHub Pages:

   ```bash
   mkdocs gh-deploy -r origin --no-history
   ```

* The lab guide should now be live on your GitHub Pages site. The URL for the site can be found via the `Settings -> Pages` menu of the repository, or go to https://github.infra.cloudera.com/pages/GOES/hol-005-agentic-studio/