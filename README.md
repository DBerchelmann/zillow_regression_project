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
* This repository also has a CSV of the data available as well

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
|  parcelid | int64   | Unique parcel identifier    |
| landuse_id     | float64 | Identifier for landuse type|
| landuse_desc   | object | Describes the type of landuse|
| last_sold_date  | object |transaction date of when property last sold|
|  total_sqft  | float64   | Total livable square footage    |
| bedroom_quanity    | float64 | count of bedrooms|
| bathroom_quanity   | float64 | count of bathrooms|
| fips  | object | Federal Information Processing Code (county code)|
|  zip_code | object   | 5 digit code used by US Postal Service    |
| year_built    | object | year home was built|
| tax_assesed_value   | float64 | total value of home established by taxing authority|
| latitude  | float64 | geographic coordinate that specifies the north–south position |
|  longitude  | float64   | geographic coordinate that specifies the east-west position     |
| tax_assess_yr    | float64 | The most recent year property taxes were assessed|
| property_tax   | float64 | ad valorem tax on the value of a property.|
| age_of_home  | int64 | age of home as of today's date in years|
| tax_rate    | float64 | This is property tax / tax_assessed_value|
| baths_pers_qft   | float64 | numbers of baths per sqft|
| beds_pers_qft  | float64| number of beds per sqft|




-------------------
  <h3><u>Hypothesis and Questions</u></h3>

- Is there a relationship between bathroom quantity and total sqft?
- Is there a relationship between bathroom quantity and tax appraised value?
- Is there is a relationship between total sqft and tax appraised value?
- Is there is a relationship between latitude and tax appraised value?
- Is there is a relationship between longitude and tax appraised value?
- Let's look into bathrooms per sqft and see if there is a difference between Los Angeles County and Orange County.

<h5> The questions above will be answered using correlation tests while the last one comparing the means of two subgroups will be achived through a T-Test.</h5>

--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
 To recreate this project you will need use the following files:
 
 wrangle.py
 evaluate.py
 explore.py
 
 Your target variable will be tax_assessed_value which is defined in the above data dictionary. Please visit my final notebook to see this variable being used.
 
 <b>Step 1.</b> Import all necessary libraries to run functions. These can be found in each corresponding .py file
 
 <b>Step 2.</b> Use acquire.py to help pull data from your SQL database. You will need to have your own env.py file with your login information to be able to cpnnect and pull fomr your SQL program.
 
 <b>Step 3.</b> To see the the cleaned data set before training do the following:
 
```df = wrangle_zillow()``` 

After you have gotten to know the data set, run the following to gather the train, validate, test data

```train, validate, X_train, y_train, X_validate, y_validate, X_test, y_test = train_validate_test(df, 'tax_assessed_value')```
    
 
 <b>Step 4.</b> Verify that your data has been prepped using df.head()
 
 <b>Step 5.</b>. Enter the explore phase using the different univariate, bivariate, and multivariate functions from the explore.py file. This is also a great time to use different line plots, swarm plots, and bar charts. The associated libraries to make the charts happen are from matplotlib, seaborn, scipy, plotly and sklearn
 
 <b>Step 6.</b> Evaluate and model the data using different regression algorithms. 
         
* Linear Regression
* Lasso Lars
* Tweedie Regressor
* Polynomial Regressor (using a 2nd degree)
 
<b>Step 7.</b> After you have found a model that works, test that model against out of sample data using the function in my notebook.
 
 For a more detailed look, please visit my final notebook for zillow regression for further assistance.
 
--------------------