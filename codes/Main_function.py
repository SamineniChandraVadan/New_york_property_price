def main(Age,units,land_area,gross_area,Borough,Build_class,tax_class):

    X1 = [int(Age)]
    X2 = [int(units)]
    X3 = [int(land_area)]
    X4 = [int(gross_area)]
    X5 = Borough_fun(Borough)
    X6 = Build_class_fun(Build_class)
    X7 = tax_class_fun(tax_class)
    X8 = X1 + X2 + X3 + X4 + X5 + X6 + X7 
    #print(len(X1),len(X2),len(X3),len(X4),len(X5),len(X6),len(X7))
    
    ## Calling the data loading function
    cur_dir = os.getcwd()
    nyc,building_mapping,General_Building_Classes = loading_data(cur_dir)
    
    ## Calling the 
    df = cleaning_data(nyc,building_mapping)    
    dff,X,y = data_preperation_for_modelling(df)
    model,X_train, X_test, y_train, y_test = running_linear_model(X,y)
    
    
    columns_list = ['AGE OF BUILDING', 'TOTAL UNITS', 'LAND SQUARE FEET',
       'GROSS SQUARE FEET', 'BO_1', 'BO_2', 'BO_3', 'BO_4', 'BO_5',
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
        'TAX_1', 'TAX_2','TAX_4']

    dt = pd.DataFrame(columns = columns_list)
    dt.loc[1] = X8
    Price = model.predict(dt)    
    predicted_price = round(Price[0])
    print("***** Sale price per one unit for your property is $",predicted_price," *********")
    
    
    
    
 ##### Visualizing the data
    ## Here change the cur_dur based on the your directory
cur_dur = os.getcwd()
nyc,building_mapping,General_Building_Classes = loading_data(cur_dur)
df = cleaning_data(nyc,building_mapping)
#df = cleaning_data(nyc,building_mapping)
vis_data = clean_data_for_vis(df,building_mapping,General_Building_Classes)
data_distribution(vis_data)
avg_sale_price_borough(vis_data)
price_distribution(vis_data)
data_distribution_in_classes(vis_data)
variation_in_price_building_class(vis_data)
sale_price_distribution(vis_data)
price_variation_with_age(vis_data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 #### User Interface

#### Hello Now lets start having fun

ipywidgets.interact(main, Age = drop_down_Age ,
                                units = drop_down_units,
                               land_area = drop_down_Land_area,
                               gross_area = drop_down_gross_area,
                               Borough = drop_down_Borough,
                               Build_class = drop_down_building_class,
                               tax_class  = drop_down_tax_class)    
    
