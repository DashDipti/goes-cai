# Lab 2: Create Tasks in Agent Studio

## Objectives

- [ ] Create Tasks for each of the Agents
- [ ] Create Dynamic Inputs ( Imputation ) for the input from our input_parser

## Lab Steps

Now let us define the tasks for our Agents to work on.

* Start with the Tasks Screen shown below

![ai_studio_edit_tasks](./ai_studio_edit_tasks.png)

| Description | Agent | Expected Output |
| :---- | :---- | :---- |
| Parse the user input: {user_input}. Extract locations, start date, end date, and air quality parameters using the InputParserTool. | input_parser_agent | A dictionary containing parsed 'locations', 'start_date', 'end_date', and 'aq_parameters' from the user input. |
| For each of the following locations, use the 'bounding_box_extractor' tool to find their bounding box coordinates. Return the bounding boxes associated with each location. | bounding_box_retriever | A dictionary or list containing the bounding box coordinates (south, west, north, east) for each specified location. |
| For each of the following locations, use the bounding boxes (south, west, north, east), and the start_date and end_date in the context,  to query the weather tool to find a concise summary of relevant historical weather conditions between provided  start_date and end_date. Focus on key weather aspects that might influence air quality (e.g., temperature, wind, precipitation). | weather_data_integrator | A dictionary or list containing aggregate of historical weather conditions for each specified location. |
| Fetch air quality data using the air_quality_tool for the eacj location: from start_date to end_date ONLY using the bounding boxes for each location. If specific parameters are provided by the aq_parameters attribute, focus on those. Return the data as a pandas DataFrame. | air_quality_retriever | A pandas DataFrame containing the air quality data for the specified locations, dates, and parameters. |
| Analyze the provided air quality data (including parameters like pm10, value, units, date, and location) for the specified locations and dates. Consider the historical weather information (temperature, wind, precipitation, humidity) for the same period. Identify any trends in air quality, calculate average values where relevant, and discuss any potential correlations or influences of weather conditions on the air quality. Provide a detailed report summarizing the air quality situation for each location, including the key findings and any notable observations related to weather patterns. Include facts and observations to compare the provided locations, as well as your own reliable knowledge base sources to comment on the overall Airquality | air_quality_analyst | A comprehensive report detailing the air quality analysis for each location, including trends, averages, and a discussion of potential relationships with the historical weather conditions. Include a Summary at the top and Conclusion at the end |

* Click on `Save and Next` to go to the Configurations Page.  

* Set the Configurations to `1000` New Tokens as below.

![ai_studio_workflow_config](./ai_studio_workflow_config.png)

* Let us now test the workflow. With the following user_input

    ```
    Can you provide an air quality report for Sydney, Australia  between 01.May.2025 to 03.May.2025 focussing on pm25 parameter
    ```

* As you can see the LLM is now hallucinating and generating data for New York and Los Angeles in Oct 2023 etc.

![ai_studio_workflow_test_hallucinating](./ai_studio_workflow_test_hallucinating.png)

!!! info
    While we have set up Agents and Tasks, the default LLM lacks the ability for us to build a **Trustworthy Investigative system**.

    In the next section we will use Custom Tools to get us a more accurate and trust worthy report

## Learning Notes

In this Lab

- [x] we learnt how to set up Tasks and associate them with Agent.

- [x] We also saw that only using Prompts lacks the ability to generate a good quality output  

**:rocket: We have now concluded Lab 2 :rocket:**
