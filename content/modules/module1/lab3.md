# Lab 3 Advanced Lab: Building Custom Tools in Agentic Workflow

!!! Question "Why build custom tools in Agentic Workflows?"
    We need custom tools for :

    * **LLMs have a knowledge cut-off date.** Their understanding of the world is frozen at the time their training ends. They have no awareness of events happening right now. ( For e.g. what is the price of stock right now)  
    * **To Interact** with Private and Proprietary Systems  
    * **To Perform Reliable and Deterministic Actions:** LLMs may make mistakes in calculations.

## Conceptual Walkthrough
Let us understand how Custom Tools can help us create agents that will perform customized tasks, such as converting Natural Language to Text or performing data transformations

* Your instructor will now facilitate this lab through the presentation, using section [building custom agent tools](https://docs.google.com/presentation/d/1jSKkVN6xjV9blB_2pUYuZwnD1yhOVE9lzcAr-yVV8vE/edit?slide=id.g36b28bd9dbb_0_0#slide=id.g36b28bd9dbb_0_0) presentation.


## Assignment Objective
 The Airquality report generated in the earlier Lab did not have an author. Your objective is to add author information to the report.We will now use our newly gained knowledge of custom tools, to update our Airquality Investigator System to add Author information into the report

* Your application input will have additional information as below 
### Expected Input
!!! Input
    Can you provide an air quality report for Sydney  between 01.Jan.2025 to 03.Jan.2025 focussing on pm25 parameter. Please use the name of the author as  Vish Rajagopalan ( USE YOUR TEAM NAME HERE )

### Expected Output

![example_output](./updated_module3_output.png)

## Assignment Tasks

- [ ] Update the `input_parser` tool in the Lab to add author information. NOTE:  add a default "Cloudera AI Agent Studio" as author if no author information is provided
- [ ] Update the main_v1.py to include Author information in prompts


## Solution Approach Hints

- Make a copy of your input_parser_tool.py and main_v1.py. Use these copies to run the new workflow, so that you do not lose the work done so far.
- Make changes to input_parser class to ensure additional information is generated as below
![updated_input_parser](./updated_input_parser.png)
- Make code changes in pydantic structures in input_parser and in the prompts in agent_quality_analyst agent in main file. 
- Validate your changes by checking code in solution file main_v2.py and input_parser_v2.py ( Hint : search for version 2 comment)
- Compare your code with the output from running the below command on terminal

```bash
 python3 main_v2.py --user-input  "Can you provide an air quality report for Singapore  between 01.Jan.2025 to 03.Jan.2025 using pm25  parameter.The author of this report should be Vish Rajagopalan"
```

- Discuss your design changes with the Lab participants

## Learning Notes

In this Lab we have

- [x] Learnt the basic building blocks of creating Tools  
- [x] We also learnt how to "Equip" agents to the newly created tools  
- [x] Understanding Hand coded Agents are important to advise clients on migrating their flows into CAI and drive usage of Agent Studio

**:rocket: We have now concluded Lab 3 :rocket:**
