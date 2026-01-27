# Lab 3: Create Custom Tools in Agent Studio and equip Agents with these tools.

## Objectives

- [ ] In this Lab, we will connect our Agent Workflows  to APIs and S3 buckets for data processing

- [ ] We will learn to create tools in Tool catalog and use them in workflows.

## Lab Steps

* Let us start by creating Tools in Tools Catalog.

![ai_studio_tools_catalog](./ai_studio_tools_catalog.png)

* Let us create a List of Tools with the name as follows:
  * Input Parser  `TeamXX` ( use your team name)

!!! NOTE
    Special characters are not allowed in Tool Name

![ai_studio_create_tool_template](./ai_studio_create_tool_template.png)

* Click on Edit tool file show  

![ai_studio_edit_tool_file](./ai_studio_edit_tool_file.png)

!!! Danger "IMPORTANT"
    Branch Name:  “LAB” branch and  Folder Name : “agent_tools_cai_studio” for all the tools. 

* Update the Tool Code : 
    * Goto the Github Location for CAI custom tools [url](https://github.com/SuperEllipse/AirAware/tree/Lab/agent_tools_cai_studio)
    * Copy the input_parser_tool.py code into the tool.py file 
    * Now you go to the location and update the `input_parser_tool.py` code in Cloudera AI `tool.py`file. 

!!! Danger "Important"
    Note that the folder to use is  `agent_tools_cai_studio`
    ![ai_studio_update_input_parser_tool](./branch_and_folder_note.png)



* Refresh and check that the `input_parser_tool.py` is updated. Finally save the tool clicking on the save button below.

![ai_studio_refresh_input_parser_tool](./ai_studio_refresh_input_parser_tool.png)

* Similarly create the following tool using the same approach update the tool.py to create 3 more tools. Do not forget to add your Team name.
    * Geocode_Boundingbox Tool
    * Weather Tool
    * Air Quality Analysis Tool ( **Note** : You need to update 2 files here, tool.py and requirements.txt, see note below)

!!! danger "Important"
    For the Air Quality Analysis Tool, we need some additional packags, so please update the requirements.txt with the packages below
    ```
    #UPDATE THE requirements.txt with the below
    # https://pip.pypa.io/en/stable/reference/requirements-file-format/
    pydantic
    boto3==1.38.17
    pandas==2.2.3
    ```


  

* Confirm in Tools Catalog if the tools that you have created are listed.

* Now let us go back to our workflow and click on "Edit Workflow"
![edit_workflow](./edit_workflow.png)



* In the Workflow  click on create or edit agents.

![ai_studio_create__or_edit_agent](./ai_studio_create__or_edit_agent.png)

* Select the Input_parser_agent and click in the  `Add optional tools` section `Create or Edit Tools`.

![ai_studio_add_optional_tools](./ai_studio_add_optional_tools.png)

* Find your tool name from tool catalog

![ai_studio_find_tool_in_catalog](./ai_studio_find_tool_in_catalog.png)
    
* Click on the `Create Tool from Template` button which adds the tool.

    * You should now be able to save the tool using the `Save Tool` button.

    * You should now be able to see the added tool In the _Optional Tools_ section.

    * Finally you can now save the agent using the `Save Agent` button

* Notice how the agent now has a tool associated with it in the workflow as below  

![ai_studio_input_parser_workflow](./ai_studio_input_parser_workflow.png)

* Follow the same approach to add all the other tools to our agentic workflow i.e.
    * Geocoding Tool
    * Weather Tool
    * Air Quality Analysis Tool  


* Finally your workflow should look like below.

![ai_studio_final_workflow](./ai_studio_final_workflow.png)

## Learning Notes

- [x] In this lab we learnt how to create Custom Tools in Agent Studio and have agents equipped with these tools.

**:rocket: We have now concluded Lab 3 :rocket:**
