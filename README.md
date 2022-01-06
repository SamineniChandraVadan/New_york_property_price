# Newyork property price prediction 
<ins> </ins>
> This repository consists of all the files of the property price prediction project, related to my Python course 

# Table of Contents
- [Overview](#Overview)
  - [1. Problem overview](#Problem-overview)
  - [2. Solution](#Solution)

- [Data](#Data)
- [Data Visualization](#Data_Visualization)
- [Model](#Model)
- User-Intetface (#User_Interface)

## Overview
<ins> </ins>

### Problem-overview
Productivity gap in the real estate industry costs the global economy $1.63 trillion a year, Global Construction sector ($25/hr) versus Global economy (($37/hr)
Here is a comparision of the annual increase in the productivity of few Industries :
  * Construction sector - 1%
  * Global economy  - 2.8%
  * Manufacturing - 3.6% 

One of the cause for the lack of productivity is : construction firms and contractors are more focused on optimizing up-front pricing to maintain margins than measuring and improving productivity. Inexperienced owners and buyers find it difficult to navigate an opaque marketplace

### Solution
Increase in market transparency → Data-driven insights that helps firms offer more standardized products at lower price points
Firms can focus more on improving supply chain, engineering practices, onsite execution, automation, re-skilling the workforce, etc. which will address the productivity issue


## Data
<ins> </ins>
The data used is Newyork sales data for the years 2016 and 2017 from the government website. The data gives information about the property like : 
* Location information
* Building Class as defined for NYC
* Tax Class
* Number of residential and Commercial Units
* Total number of units
* Total and Land gross area in sft
* Year of built
* Year sold
* `Sale Price of the Property `

Two more data sets are created for standardising and eliminating the unwanted building classes

## Data_Visualization
<ins> </ins>

*Queens has the highest number of sales from the data*

<img src="https://user-images.githubusercontent.com/51246077/148449044-55a6e911-f344-44fd-bae4-72c59dd62a86.png" width="600" height="300">


*Average Sale price per Borough is highest in Manhattan*

<img src="https://user-images.githubusercontent.com/51246077/148449054-c2fd5db4-c47b-48d9-b55d-c86ee6b551a6.png" width="600" height="300">


* Density and Distribution of Prices for each Borough is as follows *

<img src="https://user-images.githubusercontent.com/51246077/148450333-2b08e8b5-f23a-415a-bcc8-b1ac73f0a87b.png" width="600" height="300">

* All the Borough has right skewed distribution
* Manhattan and Brooklyn have the maximum variation in sale price
* Variation in sale prioce of Bronx and Staten Island are similar



* Variation of Median Sale Price in important building classes across Boroughs *

Key:
R: Residential, Condos, & Commercial
A: 1 Family Homes, Townhouses, & Mansions
B: 2 Family Homes
C: 3 or More Family Homes and Walk Ups
D: Elevator Apartments

![image](https://user-images.githubusercontent.com/51246077/148450683-3063395d-c060-46b6-a74d-d1bcec01d52c.png)




* Distribution of important Building classes *

<img src="https://user-images.githubusercontent.com/51246077/148450977-d0c4929c-3ec9-49c2-81d0-62a7547c210b.png" width="600" height="300">

* 3 Building Classes are barely sold in Stated Island


* Variation of sale price based on the Age of the Building *
<img src="https://user-images.githubusercontent.com/51246077/148451398-5077a8e1-0b64-4e20-8f2e-3e302b9be00c.png" width="600" height="300">



## Model 
<ins> </ins>

A linear model regression was used on the direct sale price and also after transforming the target variable with log transformation. The transformation helped in getting normal distribution for the target variable


![image](https://user-images.githubusercontent.com/51246077/148451814-953f74be-3d66-4812-9212-e9054f34b52e.png)


* Performance comparision of models with original and transformed target variable * 
![image](https://user-images.githubusercontent.com/51246077/148452148-88202c4c-6b8b-467b-9693-dd569ff4dc0e.png)


Sale Price RMSE : 393535.09
RMSE/ STD DEV : 0.8171


Log Sale Price RMSE : 0.2049
RMSE/ STD DEV : 0.71515



## User_Interface
<ins> </ins>

A user interface was built in the Jupyter Notebook to ease the process of inputting the values to run the model
Using the inteface the user can explore the model and price prediction by varying the inputs
This also lets user the variation of predicted price by varying the amneties and helps the companies to make designs that maximizes their `revenue` or `profit`







