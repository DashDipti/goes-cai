# Lab 4: Test, Monitor and Deploy Workflows

## Objectives

- [ ] In this Lab, we will test our Agentic Workflow, Monitor it and Deploy it as an Application

## Lab Steps
* Continue from the last lab where you were on the step of `Add Tasks` for your workflow named `Air Aware - Team XX`. Click on `Save & Next`

![workflow_tool_6a](./workflow_tool_6a.png)

* Enter the API Key you created from the Open AQ website in [Getting Setup for Workshop](../module1/lab1.md) lab. Click `Save & Next`

![workflow_tool_7](./workflow_tool_7.png)

* Test the workflow by adding the following text in `user_input` text box below. Then click `Run Workflow`.

```text {.prompt-block}
Can you provide an air quality report for Sydney, Australia  between 01.Jan.2025 to 03.Jan.2025 focussing on pm25 parameter
```

![workflow_tool_8](./workflow_tool_8.png)

* Click on the `Monitoring` Icon Tab to monitor your workflow using Phoenix

![workflow_tool_9](./workflow_tool_9.png)

* You should be able to use Phoenix to monitor your workflow by clicking on the name of your Project as shown below.

![workflow_tool_10](./workflow_tool_10.png)
![workflow_tool_11](./workflow_tool_11.png)

* Check the workflow for each tool. For example the below shows the workflow for the Input Parser Agent, which has used the tool to parse the user input

![workflow_tool_12](./workflow_tool_12.png)

*  If the Workflow has executed properly, you should be able to see the output below as a final Air quality report the user is expected to get. Then click on `Save & Next`

![workflow_tool_13](./workflow_tool_13.png)

* First save your workflow as a Template and then `ReDeploy`.

![workflow_tool_14](./workflow_tool_14.png)

![workflow_tool_15](./workflow_tool_15.png)

![workflow_tool_16](./workflow_tool_16.png)

!!! note 
    It may take between 5-10 minutes to deploy your application

* You may need to open the workflow again and click on the `Actions` Menu item to deploy.

![ai_studio_workflow_actions_deploy](./ai_studio_workflow_actions_deploy.png)

* Once deployed successfully, you should be able to see the workflow in the main Deployed Workflows section as below.

![ai_studio_deployed_workflows](./ai_studio_deployed_workflows.png)

* Now let us run this Deployed workflow just as a normal user would . Click on the application link as shown below

![ai_studio_run_deployed_workflow](./ai_studio_run_deployed_workflow.png)

* This should open a UI Page below, let us test with user_input comparing Air Quality of 3 cities by entering the following input

```text {.prompt-block}
Can you provide an air quality report for Melbourne between 01.Jan.2025 to 03.Jan.2025 focussing on pm25 parameter
```

![ai_studio_input_deployed_workflow](./ai_studio_input_deployed_workflow.png)

* After a few minutes you should be able to get a complete Air Quality report (partially shown in the screenshot below)

![ai_studio_deployed_workflow_output](./ai_studio_deployed_workflow_output.png)

* Scroll down to download the entire report on your laptop.

## Learning Notes

- [x] In this lab we learnt how to test our Agentic Workflow, Monitor it and Deploy it as an Application

**:rocket: We have now concluded Lab 4 :rocket:**

**:rocket: This concludes our Hands on Workshop :rocket:**



