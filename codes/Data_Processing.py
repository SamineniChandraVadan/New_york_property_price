def clean_data_for_vis(nyc_data,building_mapping,General_Building_Classes) :
    
    nyc_data['BROAD BUILDING CLASS'] = nyc_data['BUILDING CLASS AT TIME OF SALE'].str[0]
    # CREATING A KEY FOR THE BUILDING CLASSES. THE SINGLE LETTER FOLLOWED BY A IS NOT INTUITIVE
    nyc_data = pd.merge(nyc_data,building_mapping, left_on='BUILDING CLASS AT TIME OF SALE', right_on='Building Code').drop(columns=['Building Code'])

    # CREATING A KEY FOR THE BROAD BUILDING CLASSES
    nyc_data = pd.merge(nyc_data, General_Building_Classes, left_on = "BROAD BUILDING CLASS", right_on = "BUILDING CODE").drop(columns = ["BUILDING CODE"])

    # ADDING AN AGE COLUMN FOR HOW OLD THE BUILDING IS TO HELP WITH FURTHER ANALYSIS
    nyc_data['SALE DATE'] = pd.to_datetime(nyc_data['SALE DATE'])
    nyc_data['AGE OF BUILDING'] = nyc_data['SALE DATE'].dt.year - nyc_data['YEAR BUILT']

    # THE EXACT AGE IS TOO SPECIFIC FOR ANAYLSIS SO WE ASSIGN RANGES
    nyc_data.loc[nyc_data['AGE OF BUILDING'] <= 75, 'AGE RANGE'] = '0 to 75'
    nyc_data.loc[(nyc_data['AGE OF BUILDING'] > 75) & (nyc_data['AGE OF BUILDING'] <= 100), 'AGE RANGE'] = '75 to 100'
    nyc_data.loc[(nyc_data['AGE OF BUILDING'] > 100) & (nyc_data['AGE OF BUILDING'] <= 125), 'AGE RANGE'] = '100 to 125'
    nyc_data.loc[(nyc_data['AGE OF BUILDING'] > 125) & (nyc_data['AGE OF BUILDING'] <= 150), 'AGE RANGE'] = '125 to 150'
    nyc_data.loc[nyc_data['AGE OF BUILDING'] > 150, 'AGE RANGE'] = 'Over 150'
    nyc_data['BOROUGH'] = nyc_data['BOROUGH'].astype(str)
    nyc_data['BOROUGH'].replace({'1':'Manhattan','2':'Bronx','3':'Brooklyn','4':'Queens','5':'Staten Island'},inplace=True)
    nyc_data['BOROUGH'].replace({'1':'Manhattan','2':'Bronx','3':'Brooklyn','4':'Queens','5':'Staten Island'},inplace=True)

    # The Sale Price has a large variance owing to varying building types, number of units, size, etc.
    # Hence, we should standardize the Sale Price 
    # We can do this by getting the Sale Price per Unit Area
    nyc_data['SALE PRICE PER UNIT AREA'] = nyc_data['SALE PRICE'] / nyc_data['GROSS SQUARE FEET']
    
    df = nyc_data[['BOROUGH','ZIP CODE', 'TAX CLASS AT TIME OF SALE', 'BUILDING CLASS AT TIME OF SALE',
                          'BROAD BUILDING CLASS', 'BROAD DESCRIPTION',
                         'SALE DATE','YEAR BUILT','AGE OF BUILDING', 'AGE RANGE', 'RESIDENTIAL UNITS',
                         'COMMERCIAL UNITS', 'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET',
                         'SALE PRICE','SALE PRICE PER UNIT AREA']]

    return df
    
    











def data_preperation_for_modelling(df):     
        
    # Getting the summary metrics of sale price per unit for each bulding class category
    df1 = df.groupby('BUILDING CLASS CATEGORY')[['SALE PRICE PER UNIT AREA']].mean().reset_index()
    df2 = df.groupby('BUILDING CLASS CATEGORY')[['SALE PRICE PER UNIT AREA']].count().reset_index()
    df3 = pd.merge(left=df1,right = df2,on = 'BUILDING CLASS CATEGORY')
    
    # Renaming the columns
    df3.columns = ['BUILDING CLASS CATEGORY', 'SALE PRICE PER UNIT AREA', 'COUNT']
    
    
    ## One hot encoding the data to prepare for modelling
        # Creating the onehot_encoode function
    def onehot_encode(df, columns, prefixes):
        df = df.copy()

        for column, prefix in zip(columns, prefixes):
            dummies = pd.get_dummies(df[column], prefix=prefix)
            df = pd.concat([df, dummies], axis=1)
            df = df.drop(column, axis=1)

        return df

        # Running the onehot_encode function 
    df_model = onehot_encode(df,
            columns=['BOROUGH','BUILDING CLASS CATEGORY', 'TAX CLASS AT TIME OF SALE'],
            prefixes=['BO', 'BCC', 'TAX'])


    ## 
    dff = df_model[[ 'AGE OF BUILDING', 'TOTAL UNITS',
           'LAND SQUARE FEET', 'GROSS SQUARE FEET','SALE PRICE', 
           'BO_1', 'BO_2', 'BO_3', 'BO_4', 'BO_5',
           'BCC_01 ONE FAMILY DWELLINGS                    ',
           'BCC_02 TWO FAMILY DWELLINGS                    ',
           'BCC_03 THREE FAMILY DWELLINGS                  ',
           'BCC_04 TAX CLASS 1 CONDOS                      ',
           'BCC_05 TAX CLASS 1 VACANT LAND                 ',
           'BCC_06 TAX CLASS 1 - OTHER                     ',
           'BCC_07 RENTALS - WALKUP APARTMENTS             ',
           'BCC_08 RENTALS - ELEVATOR APARTMENTS           ',
           'BCC_09 COOPS - WALKUP APARTMENTS               ',
           'BCC_10 COOPS - ELEVATOR APARTMENTS             ',
           'BCC_11 SPECIAL CONDO BILLING LOTS              ',
           'BCC_11A CONDO-RENTALS                           ',
           'BCC_12 CONDOS - WALKUP APARTMENTS              ',
           'BCC_13 CONDOS - ELEVATOR APARTMENTS            ',
           'BCC_14 RENTALS - 4-10 UNIT                     ',
           'BCC_15 CONDOS - 2-10 UNIT RESIDENTIAL          ',
           'BCC_16 CONDOS - 2-10 UNIT WITH COMMERCIAL UNIT ',
           'BCC_17 CONDO COOPS                             ',
           'BCC_21 OFFICE BUILDINGS                        ',
           'BCC_22 STORE BUILDINGS                         ',
           'BCC_23 LOFT BUILDINGS                          ',
           'BCC_26 OTHER HOTELS                            ',
           'BCC_27 FACTORIES                               ',
           'BCC_28 COMMERCIAL CONDOS                       ',
           'BCC_29 COMMERCIAL GARAGES                      ',
           'BCC_30 WAREHOUSES                              ',
           'BCC_31 COMMERCIAL VACANT LAND                  ',
           'BCC_32 HOSPITAL AND HEALTH FACILITIES          ',
           'BCC_33 EDUCATIONAL FACILITIES                  ',
           'BCC_34 THEATRES                                ',
           'BCC_35 INDOOR PUBLIC AND CULTURAL FACILITIES   ',
           'BCC_36 OUTDOOR RECREATIONAL FACILITIES         ',
           'BCC_37 RELIGIOUS FACILITIES                    ',
           'BCC_38 ASYLUMS AND HOMES                       ',
           'BCC_41 TAX CLASS 4 - OTHER                     ',
           'BCC_42 CONDO CULTURAL/MEDICAL/EDUCATIONAL/ETC  ',
           'BCC_43 CONDO OFFICE BUILDINGS                  ',
           'BCC_44 CONDO PARKING                           ',
           'BCC_45 CONDO HOTELS                            ',
           'BCC_46 CONDO STORE BUILDINGS                   ',
           'BCC_47 CONDO NON-BUSINESS STORAGE              ',
           'BCC_48 CONDO TERRACES/GARDENS/CABANAS          ', 
           'TAX_1', 'TAX_2',
           'TAX_4']]
    
    ## Removing the outliers from the response variable
    dff = dff[dff['SALE PRICE']< 2500000]

    ## Defining the response variable and other predictors and returning the final prepared data
    y = dff['SALE PRICE']
    X = dff.drop(columns = ['SALE PRICE'])

    return (dff,X,y)
    
    
    
    
    
    
    
