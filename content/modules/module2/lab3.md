# Lab 3: Create Custom Tools in Agent Studio and equip Agents with these tools.

## Objectives

- [ ] In this Lab, we will connect our Agent Workflows  to APIs and S3 buckets for data processing

- [ ] We will learn to create tools in Tool catalog and use them in workflows.

## Lab Steps

* Let us start by creating Tools in Tools Catalog. Click on `Tools Catalog` and then `Create`.

![tools](./tools.png)

* Enter the tool name `Input Parser Team XX` (use your team name, ex - `Input Parser Team 05`) and then click `Generate`. A tool template will get created. 

!!! NOTE
    Special characters are not allowed in Tool Name

![tool_input_parser_1](./tool_input_parser_1.png)

* The tool template has 2 parts - `tool.py` & `requirements.txt`. These files can be edited in Cloudera AI workspace giving developers the capability to use low code (via Agent Studio) and high code (via Cloudera workspace) together while creating agentic workflows.

![tool_input_parser_2](./tool_input_parser_2.png)

* Click on `Edit tool file`. This will open Cloudera workspace where you will be editing the code. Keep this window open we will come back to it as we need to check GitHub page for the code that we want to use here. It is mentioned in the next step.  

![tool_input_parser_3](./tool_input_parser_3.png)


!!! Danger "IMPORTANT"
    Branch Name:  “LAB” branch and  Folder Name : “agent_tools_cai_studio” for all the tools. 

* Update the Tool Code : 
    * Goto the Github Location for CAI custom tools [url](https://github.com/SuperEllipse/AirAware/tree/Lab/agent_tools_cai_studio). Make sure you are on the `Lab` branch as shown below. There should be 4 code files there.
    ![tool_input_parser_github_4](./tool_input_parser_github_4.png)
    * Copy the code in the `input_parser_tool.py` file. 
    ![tool_input_parser_github_5](./tool_input_parser_github_5.png)
    * Now go back to the Cloudera workspace that you had opened earlier and update the `input_parser_tool.py` code (from GitHub) into Cloudera AI `tool.py`file. Then  `Save` and `Close` the file.
    ![tool_input_parser_6](./tool_input_parser_6.png)
    ![tool_input_parser_7](./tool_input_parser_7.png)
    ![tool_input_parser_8](./tool_input_parser_8.png)
    ![tool_input_parser_9](./tool_input_parser_9.png)

* Click on `Refresh` and check that the `input_parser_tool.py` is updated. Finally, save the code in tool.py file by clicking on the `Save` button below.

![tool_input_parser_10](./tool_input_parser_10.png)
![tool_input_parser_11](./tool_input_parser_11.png)
![tool_input_parser_12](./tool_input_parser_12.png)


!!! danger "Important"
    Using the same method we have already created 3 more tools namely - `Geocode Boundingbox Tool`, `Weather Tool`, `Air Quality Analysis Tool` which you will be using in the next steps. For the `Air Quality Analysis Tool`, we need some additional packages, so we have updated `requirements.txt` corresponding to `Air Quality Analysis Tool` with those packages as shown below. This is just FYI.
    ```
    #UPDATE THE requirements.txt with the below
    # https://pip.pypa.io/en/stable/reference/requirements-file-format/
    pydantic
    boto3==1.38.17
    pandas==2.2.3
    ```

* Confirm in Tools Catalog if the tools that you have created are listed.

* Now let us go back to our workflow and click on `Air Aware - Team XX` (Your workflow).

![workflow](./workflow.png)

* You might have to then click `Edit & Redeploy`.

![workflow_edit_1](./workflow_edit_1.png)

* In the Workflow click on create or edit agents.

![workflow_edit_2](./workflow_edit_2.png)

* Select the `input_parser_agent` and under `Add Tools` section click on ` + Create or Edit Tools`.

![workflow_tool_1](./workflow_tool_1.png)

* Find your tool name from tool catalog (Ex -  `Input Parser Team 05`) and check if the code is correct or not in the `tool.py` file.

![workflow_tool_2](./workflow_tool_2.png)
    
* Click on the `Create Tool from Template` button which adds the tool.

![workflow_tool_3](./workflow_tool_3.png)

* Click on `Close` button.

![workflow_tool_4](./workflow_tool_4.png)

* Notice how the agent now has a tool associated with it in the workflow as below  

![workflow_tool_5](./workflow_tool_5.png)

* Follow the same approach to add all the other tools (`Geocode Boundingbox Tool`, `Weather Tool`, `Air Quality Analysis Tool`) to our agentic workflow. Finally, your workflow should look like below. Click on `Save & Next`. Keep this window open as we move on to the next exercise. 

![workflow_tool_6](./workflow_tool_6.png)


## Learning Notes

- [x] In this lab we learnt how to create Custom Tools in Agent Studio and have agents equipped with these tools.

**:rocket: We have now concluded Lab 3 :rocket:**
