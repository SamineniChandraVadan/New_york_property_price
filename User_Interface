## Creating the interface for the user to give input
drop_down_Age = ipywidgets.IntSlider(min = 0, max =200, value= 5,step = 1, descrition = 'Age',disabled = False,)

drop_down_units = ipywidgets.IntSlider(min = 0, max = 200, value = 1,step = 1, descrition = 'Units',disabled = False,)

drop_down_Land_area = ipywidgets.IntSlider(min = 0, max = 20000, value = 200,step = 100, descrition = 'Land area',disabled = False,)

drop_down_gross_area = ipywidgets.IntSlider(min = 0, max = 20000, value = 200,step = 100, descrition = 'Gross area',disabled = False,)

drop_down_Borough = ipywidgets.Dropdown(options = ['Manhattan','Bronx','Brooklyn','Queens','Staten Island'],value='Manhattan' ,descrition = 'BOROUGH',disabled = False,)

Build_class = ['ONE FAMILY DWELLINGS','TWO FAMILY DWELLINGS','THREE FAMILY DWELLINGS','TAX CLASS 1 CONDOS','TAX CLASS 1 VACANT LAND','TAX CLASS 1 - OTHER','RENTALS - WALKUP APARTMENTS','RENTALS - ELEVATOR APARTMENTS','COOPS - WALKUP APARTMENTS','COOPS - ELEVATOR APARTMENTS','SPECIAL CONDO BILLING LOTS','A CONDO-RENTALS','CONDOS - WALKUP APARTMENTS','CONDOS - ELEVATOR APARTMENTS','RENTALS - 4-10 UNIT','CONDOS - 2-10 UNIT RESIDENTIAL','CONDOS - 2-10 UNIT WITH COMMERCIAL UNIT','CONDO COOPS','OFFICE BUILDINGS','STORE BUILDINGS','LOFT BUILDINGS','OTHER HOTELS','FACTORIES','COMMERCIAL CONDOS','COMMERCIAL GARAGES','WAREHOUSES','COMMERCIAL VACANT LAND','HOSPITAL AND HEALTH FACILITIES','EDUCATIONAL FACILITIES','THEATRES','INDOOR PUBLIC AND CULTURAL FACILITIES','OUTDOOR RECREATIONAL FACILITIES','RELIGIOUS FACILITIES','ASYLUMS AND HOMES','TAX CLASS 4 - OTHER','CONDO CULTURAL/MEDICAL/EDUCATIONAL/ETC','CONDO OFFICE BUILDINGS','CONDO PARKING','CONDO HOTELS','CONDO STORE BUILDINGS','CONDO NON-BUSINESS STORAGE','BCC_48 CONDO TERRACES/GARDENS/CABANAS']
drop_down_building_class = ipywidgets.Dropdown(options = Build_class,value='ONE FAMILY DWELLINGS' ,descrition = 'Building description',disabled = False,)

drop_down_tax_class = ipywidgets.Dropdown(options = [1,2,4],value=1 ,descrition = 'Tax class',disabled = False,)


## defining age input function
def Age(x):
    L = [int(x)]
    return L


## defining borough input function and defining them in a one hot encoding
def Borough_fun(x):
    L = ['Manhattan','Bronx','Brooklyn','Queens','Staten Island']
    l = len(L)    
    I = L.index(x)
    L2 = list(np.zeros(l,dtype = int))
    L2[I] = 1      
    return L2

## Defining Building class input function function
def Build_class_fun(x) :
    L = ['ONE FAMILY DWELLINGS','TWO FAMILY DWELLINGS','THREE FAMILY DWELLINGS','TAX CLASS 1 CONDOS','TAX CLASS 1 VACANT LAND','TAX CLASS 1 - OTHER','RENTALS - WALKUP APARTMENTS','RENTALS - ELEVATOR APARTMENTS','COOPS - WALKUP APARTMENTS','COOPS - ELEVATOR APARTMENTS','SPECIAL CONDO BILLING LOTS','A CONDO-RENTALS','CONDOS - WALKUP APARTMENTS','CONDOS - ELEVATOR APARTMENTS','RENTALS - 4-10 UNIT','CONDOS - 2-10 UNIT RESIDENTIAL','CONDOS - 2-10 UNIT WITH COMMERCIAL UNIT','CONDO COOPS','OFFICE BUILDINGS','STORE BUILDINGS','LOFT BUILDINGS','OTHER HOTELS','FACTORIES','COMMERCIAL CONDOS','COMMERCIAL GARAGES','WAREHOUSES','COMMERCIAL VACANT LAND','HOSPITAL AND HEALTH FACILITIES','EDUCATIONAL FACILITIES','THEATRES','INDOOR PUBLIC AND CULTURAL FACILITIES','OUTDOOR RECREATIONAL FACILITIES','RELIGIOUS FACILITIES','ASYLUMS AND HOMES','TAX CLASS 4 - OTHER','CONDO CULTURAL/MEDICAL/EDUCATIONAL/ETC','CONDO OFFICE BUILDINGS','CONDO PARKING','CONDO HOTELS','CONDO STORE BUILDINGS','CONDO NON-BUSINESS STORAGE','BCC_48 CONDO TERRACES/GARDENS/CABANAS']
    I = L.index(x)
    L2 = list(np.zeros(len(L),dtype = int))
    L2[I] = 1
    return L2


## Defining Tax class input function

def tax_class_fun(x):
    L = [1,2,4]
    l = len(L)
    I = L.index(x)
    L2 = list(np.zeros(l,dtype = int))
    L2[I] = 1
    return L2
    
    
   



