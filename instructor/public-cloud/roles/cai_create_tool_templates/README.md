<!--
 Copyright 2025 Cloudera, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

# AI Studios Create Tool Templates

Configure a specified list of LLM models with Cloudera AI Studios.

## Requirements

## Role Variables

Available variables are listed below, along with default values (see also `defaults/main.yml`).

| Variable | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `cai_workspace_api` | `str` | Yes | | Cloudera AI Workbench API endpoint. |
| `cai_workbench_api_key` | `str` | Yes | | Cloudera AI Workbench API v2 key. |
| `cai_project` | `str` | Yes | | The name of a pre-existing Cloudera AI project name. |
| `cai_user` | `str` | Yes |  | Cloudera AI Username. |
| `ai_studio` | `str` | Yes |  | String to select pre-defined AI Studio configurations. |
| `cai_ai_studio_details` | `dict` | No |  | String to select pre-defined AI Studio configurations required for model registering. |
| `llm_model_details` | `list` | No |  | List of LLM models to register. |

## Dependencies

None.

## Example Playbook

```yaml
- hosts: localhost
  connection: local
  tasks:

    - name: Register LLM models
      ansible.builtin.import_role:
        name: cai_register_model
      vars:
        ai_studio: "agent_studio"
        cai_project: "example-project"
        cai_workspace_api: "example-workbench-api"
        cai_workbench_api_key: "example-workbench-api-key"            
        cai_user: "example-user"
        llm_model_details:
          - model_name: "model-1"
            model_type: "OPENAI"
            provider_model: "gpt-4o-mini"
            api_key: "sk-proj-...."
            # api_base:  
            default: true          
          - model_name: "model-2"
            model_type: "OPENAI"
            provider_model: "gpt-4"
            api_key: "sk-proj-...."
            # api_base:  
            default: false          
```

## License

```
Copyright 2025 Cloudera, Inc.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```