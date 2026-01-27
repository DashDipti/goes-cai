# Lab 1: Getting Setup for Workshop

## Workshop Setup :

| Cloudera Tenant Name     | Workspace Name | Project Names  |
|--------------------------|----------------|-------------------------|
| se-xxx(will be provided) | aistudio-hol-ml| Airaware-Team-XX        |

Your specific Team name will be provided by your instructor

## Objectives

We will learn to:

- [ ] Set up the components required for a hand coded Agentic workflow  
- [ ] Create an Key for working with Open Airquality Dataset (From OPENAQ)

## Lab Steps
!!!danger "IMPORTANT"
    Before performing the steps below, check with your Lab Instructor. The Project may have been already set up for you with an automated deployment. If so, then skip to **Test Your Project** section below

 
### Setup Your CAI  Project
* Create a new Project in CAI
* The project should be of type **Git** and use the following settings:
    * Git URL: `https://github.com/SuperEllipse/AirAware.git`
    * Branch: `Lab`
    
    !!!important
        Make sure you are cloning the **`Lab`** branch and **NOT** the Main branch of the repo above.

* Go to the Project Settings, click on  Advanced Tab and create an environment variable called OPENAI_API_KEY. Provide your OpenAI key  in the value box   

    !!!Note 
        You may not need to add the OPENAI_API_KEY to project settings if project has been set up for you by your instructor. Do confirm anyway with your Instructor.

* Start a new terminal and use the following code in terminal  

* Open `requirements.txt` to review some of the key packages you need for Agentic workflow such as Pydantic and CrewAI  

* Run the command to set up the packages on your system

    ```bash
    pip install -r requirements.txt 
    ```

### Test Your Project
* Your instructor would have assigned you a project and “pair programming” partner.  ( Check with your instructor if you are missing this before proceeding ahead )
* Ensure that you can log into your assigned project 
* Start a new default Cloudera AI  Session with configuration ( 2 vCPU, 4 GB Memory, Python 3.11, PBJ Runtime ) and check if you are able to launch the session succesfully
* Check that you are able to launch a terminal from the session

## API Access Setup 

* Create an Account in Open Air quality Website  at [https://explore.openaq.org/register](https://explore.openaq.org/register).

![Register OpenAQ Account](./openaq_register.png)

**!!!Hint:** <br>
    Strong Password suggestions : AI.agents.rocks.XX(Your Team Number)

* Now Login to the OpenAQ account and generate API Key in account settings.

![Create OpenAQ API Key](./openaq_api_key.png)

* Copy this API key and save it carefully in a notepad. You will need to access it later

## Learning Notes

- [x] We have set up  the CAI Project( If not done so already) and tested the same

- [x]  We set up an account in OPENAQ for accessing an external Air quality data and generated an api key, and updated it in our project

**:rocket: We have now concluded Lab 1 :rocket:**
