# Lab 4: Test, Monitor and Deploy Workflows

## Objectives

- [ ] In this Lab, we will test our Agentic Workflow, Monitor it and Deploy it as an Application

## Lab Steps
* Click on your workflow in edit mode from the home page
![edit_workflow](./edit_workflow.png)
* Click on the capability description and add the below text into the text box under Capability guide

```text {.prompt-block}
The "Air Aware" workflow is designed to provide a comprehensive analysis of air quality for specified locations over a given date range. It involves a series of specialized agents and tasks that work collaboratively to achieve this goal. The process begins with the retrieval of bounding box coordinates for each location, which are then used to gather historical weather data focusing on factors that influence air quality, such as temperature, wind, and precipitation. Concurrently, air quality data is fetched from OpenAQ, focusing on specified parameters if provided. The collected data is then analyzed to identify trends, calculate averages, and explore potential correlations between weather conditions and air quality. The workflow culminates in a detailed report that summarizes the air quality situation for each location, highlighting key findings and notable observations related to weather patterns.

Input to the tool : 
Can you provide an air quality report for Sydney  between 01.Jan.2025 to 03.Jan.2025 focussing on pm25 parameter

```

![ai_studio_update_capability_guide](./ai_studio_update_capability_guide.png)

* Click on `Save & Next` until you reach the _Configure_ step in the workflow as shown below.

![ai_studio_configure_workflow](./ai_studio_configure_workflow.png)

* Enter the API Key you created from the Open AQ website in [Getting Setup for Workshop](../module1/lab1.md) lab. Click `Save & Next`


* Test the workflow by adding the following text in `user_input` text box below

```text {.prompt-block}
Can you provide an air quality report for Sydney, Australia  between 01.Jan.2025 to 03.Jan.2025 focussing on pm25 parameter
```

![ai_studio_test_workflow](./ai_studio_test_workflow.png)

* Click on the `Monitoring` Icon Tab to monitor your workflow using Phoenix

![ai_studio_monitoring](./ai_studio_monitoring.png)

* You should be able to use Phoenix to monitor your workflow by clicking on the name of your Project as shown below.

![ai_studio_monitoring_project](./ai_studio_monitoring_project.png)

![ai_studio_monitoring_project_summary](./ai_studio_monitoring_project_summary.png)

* Check the workflow for each tool. For example the below shows the workflow for the Input Parser Agent, which has used the tool to parse the user input

![ai_studio_monitoring_trace](./ai_studio_monitoring_trace.png)

*  If the Workflow has executed properly, you should be able to see the output below as a final Air quality report the user is expected to
get.

![ai_studio_workflow_final_report](./ai_studio_workflow_final_report.png)

* Click on `Save & Next`, and first save your workflow as a Template and then `Deploy`.

![ai_studio_workflow_deploy](./ai_studio_workflow_deploy.png)

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
