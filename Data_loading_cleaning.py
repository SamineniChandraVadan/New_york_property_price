## Import libraries
import os
import ipywidgets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


pd.set_option('display.float_format', lambda x: '%.2f' % x)
def loading_data(directory) :      
    ## Reading the data from the directory & removing unnecessary rows
    nyc_data = pd.read_csv(os.path.join(directory, "Python_project.csv"),na_values=['-', " "])
    nyc_data = nyc_data.drop(['Unnamed: 0'], axis=1)
    
    ## Reading the mapping data
    building_mapping = pd.read_csv(os.path.join(directory, 'building_mapping.csv'))
    
    General_Building_Classes = pd.read_csv(os.path.join(directory, 'General_Building_Classes.csv'))
    
    return nyc_data, building_mapping, General_Building_Classes
        
    
    
    def cleaning_data(nyc_data,building_mapping):
    
    ## Cleaning each columns in the data
    nyc_data['SALE PRICE'] = pd.to_numeric(nyc_data['SALE PRICE'], errors='coerce')
    nyc_data['YEAR BUILT'] = pd.to_numeric(nyc_data['YEAR BUILT'], errors='coerce')
    nyc_data['TOTAL UNITS'] = pd.to_numeric(nyc_data['TOTAL UNITS'], errors='coerce')
    nyc_data['COMMERCIAL UNITS'] = pd.to_numeric(nyc_data['COMMERCIAL UNITS'], errors='coerce')
    nyc_data['RESIDENTIAL UNITS'] = pd.to_numeric(nyc_data['RESIDENTIAL UNITS'], errors='coerce')
    nyc_data['TOTAL UNITS'] = pd.to_numeric(nyc_data['TOTAL UNITS'], errors='coerce')
    nyc_data['GROSS SQUARE FEET'] = pd.to_numeric(nyc_data['GROSS SQUARE FEET'], errors='coerce')
    nyc_data['LAND SQUARE FEET'] = pd.to_numeric(nyc_data['LAND SQUARE FEET'], errors='coerce')
        
    ## Cleaning the sale price data by removing NAs and outliers
    ### Since the sale price is the dependent variable which we are trying to analyze and predict, there is no way in which we
    ### can handle those null and zero values.
    nyc_data = nyc_data.dropna(subset=['SALE PRICE'])
    lower_limit = np.percentile(nyc_data['SALE PRICE'],18)
    upper_limit = np.percentile(nyc_data['SALE PRICE'],99)    
    nyc_data = nyc_data[(nyc_data['SALE PRICE'] > lower_limit) & (nyc_data['SALE PRICE'] < upper_limit)]
    
    # Since *BUILDING CLASS AT TIME OF SALE* did not have any null values, we merged building classification on it.
    merged_df = pd.merge(nyc_data,building_mapping, left_on='BUILDING CLASS AT TIME OF SALE', right_on='Building Code').drop(columns=['Building Code'])
   
    # Converting *SALE DATE* into into date format
    merged_df['SALE DATE'] = pd.to_datetime(merged_df['SALE DATE'])
    
    # Dropping *EASE-MENT* and *APARTMENT NUMBER* since both columns does not have any records.
    # Moreover, these parameters don't have any value for our analysis
    merged_df = merged_df.drop(columns = ['EASE-MENT','APARTMENT NUMBER'], axis=1)
    
    # Some record have *GROSS SQUARE FEET* as 0 which is not possible. Therefore, we are replacing them with NULL so that we can
    # handle those cases while we impute and fill the NULL *GROSS SQUARE FEET*.
    merged_df['GROSS SQUARE FEET'].replace(0,np.nan, inplace=True)
    merged_df['LAND SQUARE FEET'].replace(0,np.nan, inplace=True)
    
    # After imputing stratified means based on *BOROUGH* and *BROAD BUILDING CLASS* feature, we are still left with 3624 null values
    # in *GROSS SQAURE FEET*. On further analyzing, we found that there were some combinations of boroughs and building class 
    # that didn't exist so such values couldn't be imputed. Therefore, we filled the remaining values with mean of just the
    # *BROAD BUILDING CLASS*.
    merged_df['LAND SQUARE FEET'] = merged_df['LAND SQUARE FEET'].fillna(merged_df.groupby(['BOROUGH','BUILDING CLASS AT TIME OF SALE'])['LAND SQUARE FEET'].transform('mean'))
    merged_df['GROSS SQUARE FEET'] = merged_df['GROSS SQUARE FEET'].fillna(merged_df.groupby(['BOROUGH','BUILDING CLASS AT TIME OF SALE'])['GROSS SQUARE FEET'].transform('mean'))
    
    # Since building class category has 47 unique values, we reduced it to 25 by creating broad categories so that we could analyze
    merged_df['BROAD BUILDING CLASS'] = merged_df['BUILDING CLASS AT TIME OF SALE'].str[0]
    
    # After imputing stratified means based on *BOROUGH* and *BROAD BUILDING CLASS* feature, we are still left with 3624 null values
    # in *GROSS SQAURE FEET*. On further analyzing, we found that there were some combinations of boroughs and building class 
    # that didn't exist so such values couldn't be imputed. Therefore, we filled the remaining values with mean of just the
    # *BROAD BUILDING CLASS*.
    merged_df['LAND SQUARE FEET'] = merged_df['LAND SQUARE FEET'].fillna(merged_df.groupby(['BOROUGH','BROAD BUILDING CLASS'])['LAND SQUARE FEET'].transform('mean'))
    merged_df['GROSS SQUARE FEET'] = merged_df['GROSS SQUARE FEET'].fillna(merged_df.groupby(['BOROUGH','BROAD BUILDING CLASS'])['GROSS SQUARE FEET'].transform('mean'))
    merged_df['LAND SQUARE FEET'] = merged_df['LAND SQUARE FEET'].fillna(merged_df.groupby(['BROAD BUILDING CLASS'])['LAND SQUARE FEET'].transform('mean'))
    merged_df['GROSS SQUARE FEET'] = merged_df['GROSS SQUARE FEET'].fillna(merged_df.groupby(['BROAD BUILDING CLASS'])['GROSS SQUARE FEET'].transform('mean'))
    merged_df['GROSS SQUARE FEET'] = merged_df['GROSS SQUARE FEET'].fillna(merged_df['LAND SQUARE FEET'])
    merged_df['AGE OF BUILDING'] = merged_df['SALE DATE'].dt.year - merged_df['YEAR BUILT']
    
    # As the sale price has a large variance owing to varying building types and number of units,
    # Hence, it makes sense to analyze on sale price per unit area, therefore we normalized sale price
    merged_df['SALE PRICE PER UNIT AREA'] = merged_df['SALE PRICE'] / merged_df['LAND SQUARE FEET']
    
    # Re-ordering columns in our final dataframe *nyc* which we will use for our analysis
    nyc = merged_df[['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY','Building Description','BUILDING CLASS AT TIME OF SALE', 
                       'BROAD BUILDING CLASS', 'TAX CLASS AT TIME OF SALE','SALE DATE','YEAR BUILT','AGE OF BUILDING','BLOCK', 
                       'LOT', 'ADDRESS', 'ZIP CODE','RESIDENTIAL UNITS', 'COMMERCIAL UNITS', 'TOTAL UNITS',
                       'LAND SQUARE FEET', 'GROSS SQUARE FEET',  'BUILDING CLASS AT PRESENT',
                       'TAX CLASS AT PRESENT','SALE PRICE','SALE PRICE PER UNIT AREA']]
    
    return nyc
