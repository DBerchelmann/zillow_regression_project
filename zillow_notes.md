 <h4> if you are finished with the exercises...here is what I want y'all to do next...this will help you prepare for the regression project :-D</h4>
 
- use mySQL to query the zillow database. <b>COMPLETE</b>
- you will need to use the properties_2017 and predictions_2017 tables. <b>COMPLETE</b>
- you will want to gather the following information (and figure out which columns are most likely to give you this information)...square feet of the house ("living square feet"), number of bedrooms, number of bathrooms, the assess value of the house by the tax appraisal district ('taxvaluedollarcnt'...this will be your target variable in the project), and 2-3 other variables you think will be useful (think about what you know about what drives home prices, and also the amount of non-null values available in selecting your extra variables.<b>IN PROCESS</b>
- you will want to limit your data to properties that were sold in may, june, july or august (date is in predictions_2017 table). <b>COMPLETE</b>

['bathroomcnt', 'bedroomcnt', 'calculatedfinishedsquarefeet', 'regionidneighborhood', 'yearbuilt', 'taxvaluedollarcnt', and 'taxamount'] 

<h4>There are a ton of rows...so think about how you can limit your data set early to keep your query going! i.e. filter the dates!</h4>

Interesting links to read later:

(https://www.mdpi.com/2220-9964/9/5/288/htm)
    
(https://www.slideshare.net/NicholasMcClure1/python-datascienceatzillow)
    
(https://commercedataservice.github.io/tutorial_zillow_acs/)


Quick obseravations on NULLS for area

- 41,370 total rows pulled for the SQL query involving 2017 properties sold from May - end of August

- 16 missing values (FIPS, Zip, Regionidcounty, lat/long, censustrack....all missing, no way to know location)

  <u><b>parcelid</b></u>  ----  <u><b>FIPS</b></u>
- 12136406	-- NULL
- 13009578	--NULL
- 12038488	--NULL
- 10830484	--NULL
- 12768278	--NULL
- 11924390	--NULL
- 11928618	--NULL
- 12209558	--NULL
- 11491470	--NULL
- 12432369	--NULL
- 12031054	--NULL
- 12139606	--NULL
- 11491470	--NULL
- 11648871	--NULL
- 13008207	--NULL
- 11510663	--NULL
 
 - There are 3 areas, all in California. (FIPS looked up via https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697)
     - 6037 - Los Angeles County, California
     - 6059 - Orange County, California
     - 6111 - Ventura County, California


- Should we use zip code, lat/long to map properties? What about census tract?

-----

My initial MYSQL QUERY to filter Zillow by dates (May-August of 2017)

```
use zillow;
SELECT *
FROM predictions_2017
JOIN properties_2017 USING (parcelid)
WHERE month(transactiondate) >= 05 and month(transactiondate) <= 08
ORDER BY transactiondate;
```

-----

Our target variable (dependent variable) is the current tax value of the property (taxvaluedollarcnt). 

-------

This query will filter based on distinct county ID

```
SELECT DISTINCT regionidcounty 
FROM predictions_2017
JOIN properties_2017 using (parcelid)
WHERE month(transactiondate) >= 05 and month(transactiondate) <= 08
ORDER BY regionidcounty;
```

---

Can also query by FIPS (another unique identifier of the area)

```
SELECT * 
FROM predictions_2017
JOIN properties_2017 using (parcelid)
WHERE month(transactiondate) >= 05 and month(transactiondate) <= 08
ORDER BY fips;
```

-----

Query by features I find important. This led to 16 total null values, same as the list above. 

```
SELECT parcelid, calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, buildingqualitytypeid, fips, regionidzip, yearbuilt, taxvaluedollarcnt, assessmentyear, taxamount
FROM predictions_2017
JOIN properties_2017 using (parcelid)
WHERE month(transactiondate) >= 05 and month(transactiondate) <= 08
ORDER BY fips;
```

----

<b>questions related to above query</b>

 - Is the rating for the building quality type id related to the assesed value? 
 
  - With that info, how does that compare to bedrooms, bath, year built, and area
  
- quick findings

    - building quality type id only shows for home in Los Angeles County (FIPS 6037). Rating goes from 3 to 12.
 
 
 
 ---