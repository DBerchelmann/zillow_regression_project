<h1> Zillow Regression Project </h1>

Hi there,

Welcome to the README file for the <b>Zillow Regression Project.</b>

In here, you will find expanded information on this project including goals, how I will be working through the pipeline and a data dictionary to help offer more insight to the variables that are being used.

-------------------
<h3><u>The Goal</u></h3>

<font color = blue>**Why are we here?**</font>

* <font color = red>Goal 1:</font> <i>Predict the values of single unit properties based on sold data from May-June of 2017</i>
* <font color = red>Goal 2:</font> <i>Identify the county & state where the properties are located in addition to the distributino of property tax rates</i>

-------------------
<h3><u>Where Is Our Data Coming From?</u></h3>

* This data is being pulled from a SQL database under the name 'Zillow'
    * For this project, I am utilizing the 2017 properties and predictions tables along with the property landuse type table
* The data can also be pulled from Kaggle.com 
    * https://www.kaggle.com/c/zillow-prize-1/data

------------------
<H3><u> Project Planning </u></H3>

In addition to this README, you can see my TRELLO project pipeline by visiting the following link: https://trello.com/b/R1afNR64

Here is a snapshot of my project planning/setup on the morning of 4/14/21

<img src="https://i.ibb.co/bQPm0MH/Reg-ppline.png" alt="Reg-ppline" border="0">
  

-------------

<h3><u>Data Dictionary</u></h3>
    
-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  parcelid | int64   | --    |
| landuse_id     | float64 | --|
| landuse_desc   | object | --|
| last_sold_date  | object | --|
|  total_sqft  | float64   | --    |
| bedroom_quanity    | float64 | --|
| bathroom_quanity   | float64 | --|
| fips  | float64 | --|
|  zip_code | float64   | --    |
| year_built    | float64 | --|
| tax_assesed_value   | float64 | --|
| latitude  | float64 | --|
|  longitude  | float64   | --    |
| tax_assess_yr    | float64 | --|
| property_tax   | float64 | --|
| age_of_home  | int64 | --|





-------------------
  <h3><u>Hypothesis and Questions</u></h3>

- This section will be developed
 
--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
 To recreate this project you will need use the following files:
 
 acquire.py
 prepare.py
 explore.py
 model.py
 
 <b>Step 1.</b> Import all necessary libraries to run functions. These can be found in each corresponding .py file
 
 <b>Step 2.</b> Use acquire.py to help pull data from your SQL database. You will need to have your own env.py file with your login information to be able to cpnnect and pull fomr your SQL program.
 
 <b>Step 3.</b> Use the clean_zillow(df) function followed by the train_validate_test_split(df, seed=123) to prep the data.
 
 <b>Step 4.</b> Verify that your data has been prepped using df.head()
 
 <b>Step 5.</b>. Enter the explore phase using the different univariate, bivariate, and multivariate functions from the explore.py file. This is also a great time to use different line plots, swarm plots, and bar charts. The associated libraries to make the charts happen are from matplotlib, seaborn, scipy, and sklearn
 
 <b>Step 6.</b> Evaluate and model the data using different classification algorithms. 
         
 ```
 { 
TBD
 }
 ```
 
 <b>Step 7.</b> After you have found a model that works, you can export a CSV with your predictions and probablities using the get_model() function from model.py.
 
 For a more detailed look, please visit my final notebook for zillow regression for further assistance.
 
--------------------