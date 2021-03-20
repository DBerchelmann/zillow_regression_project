  
import pandas as pd
import numpy as np
import os

# acquire
from env import host, user, password
from pydataset import data

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split



os.path.isfile('zillow_df.csv')


# Create helper function to get the necessary connection url.
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
    

  
    
    

# Use the above helper function and a sql query in a single function.
def new_zillow_data():
    '''
    This function reads data from the Codeup db into a df.
    '''
    zillow_sql = "SELECT parcelid, propertylandusetypeid, propertylandusedesc, unitcnt, \
                 transactiondate, calculatedfinishedsquarefeet, bedroomcnt, \
                 bathroomcnt, fips, regionidzip, yearbuilt, taxvaluedollarcnt, latitude, longitude,  \
                 assessmentyear, taxamount \
                 FROM predictions_2017 \
                 JOIN properties_2017 using (parcelid) \
                 JOIN propertylandusetype using (propertylandusetypeid) \
                 WHERE month(transactiondate) >= 05 and month(transactiondate) <= 08 \
                 AND propertylandusetypeid > 250 \
                 AND propertylandusetypeid < 280  \
                 AND propertylandusetypeid != 270  \
                 AND propertylandusetypeid != 271 \
                 OR unitcnt = 1 \
                 ORDER BY unitcnt DESC;" 
    
    
    return pd.read_sql(zillow_sql, get_connection('zillow'))


def get_zillow_data(cached=False):
    '''
    This function reads in telco churn data from Codeup database and writes data to
    a csv file if cached == False or if cached == True reads in telco df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile('zillow_df.csv') == False:
        
        # Read fresh data from db into a DataFrame.
        df = new_zillow_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('zillow_df.csv')
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv('zillow_df.csv', index_col=0)
        
    return df

def clean_zillow():
    
    
    '''
    For this practice zillow data frame, we will be locating NaNs in different columns
    and removing those from the dataset.
    
    We will return: df, a cleaned pandas dataframe
    '''
    df = get_zillow_data(cached=False)
    
    # Identify properties that do not qualify as single family homes
    indexpropids = df.loc[df['propertylandusetypeid'].isin([31, 46, 47, 246, 247, 248, 260, 267, 270, 271, 290, 291])].index
    
    # Delete properties that do not qualify as single family homes
    df.drop(indexpropids , inplace=True)
            
    # Remove NaNs from finished square feet
    df.loc[df['calculatedfinishedsquarefeet'].isin(['NaN'])].head()
    indexsize = df.loc[df['calculatedfinishedsquarefeet'].isin(['NaN'])].index
    df.drop(indexsize , inplace=True)
    
    # Remove NaNs from zip code
    df.loc[df['regionidzip'].isin(['NaN'])].head()
    indexzip = df.loc[df['regionidzip'].isin(['NaN'])].index
    df.drop(indexzip , inplace=True)
    
    # Remove NaNs from tax amount
    df.loc[df['taxamount'].isin(['NaN'])].head()
    indextax = df.loc[df['taxamount'].isin(['NaN'])].index
    df.drop(indextax , inplace=True)
    
     # Remove NaNs from year_built
    df.loc[df['yearbuilt'].isin(['NaN'])].head()
    indextax = df.loc[df['yearbuilt'].isin(['NaN'])].index
    df.drop(indextax , inplace=True)
    
    # Remove decimal from latitude and longitude
    df['latitude'] = df['latitude'].astype(int)
    df['longitude'] = df['longitude'].astype(int)
    
    # Convert latitude and longitude to positonal data points using lambda funtion (i.e. putting a decimal in the correct place)
    df['latitude'] = df['latitude'].apply(lambda x: x / 10 ** (len((str(x))) - 2))
    df['longitude'] = df['longitude'].apply(lambda x: x / 10 ** (len((str(x))) - 4))
    
    # Remove properties with a unit count greater than 1
    indexunits = df.loc[df['unitcnt'].isin([2, 3])].index
    
    # Delete properties that do not qualify as single family homes
    df.drop(indexunits , inplace=True)
    
    # Drop unitcnt column
    
    df.drop('unitcnt', axis=1, inplace=True)
    
    # Remove properties with a tax value greater than or equal to 5 million dollars (these are outliers causing issues)
    index5000 = df.loc[df['calculatedfinishedsquarefeet'] >= 5000].index
    df.drop(index5000 , inplace=True)
    
    indexpricey = df.loc[df['taxvaluedollarcnt'] >= 5000000].index
    df.drop(indexpricey , inplace=True)
    
    
    return df

def split_data(df):
    '''
    split our data,
    takes in a pandas dataframe
    returns: three pandas dataframes, train, test, and validate
    '''
    train_val, test = train_test_split(df, train_size=0.8, random_state=123)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=123)
    
    
    return train, validate, test
       
   

 # wrangle!
def wrangle_zillow():
    '''
    wrangle_grades will read in our student grades as a pandas dataframe,
    clean the data
    split the data
    return: train, validate, test sets of pandas dataframes from telco_churn, stratified on total_charges
    '''
    df = clean_zillow(new_zillow_data())
    
    
    
    return split_data(df)