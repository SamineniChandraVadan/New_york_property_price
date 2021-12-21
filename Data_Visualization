def data_distribution(df):    
    labels = [BOROUGH for BOROUGH, df in df.groupby('BOROUGH')]
    values = df['BOROUGH'].groupby(df['BOROUGH']).count()
    plt.pie(values, labels = labels, autopct='%.2f%%')
    plt.title("The Distribution of 56,689 Property Sales in New York", size = 14)
    plt.show()
    
    






def avg_sale_price_borough(df):    
    xaxis = [BOROUGH for BOROUGH, df in df.groupby('BOROUGH')]
    values = df['SALE PRICE'].groupby(df['BOROUGH']).mean()
    plt.bar(xaxis, values)
    plt.title('Average Sale Price Per Borough', size = 14)
    plt.ylabel('Average Sale Price in $1,000,000', size = 12)
    plt.xlabel('Boroughs', size = 12)
    plt.grid()
    plt.show()
    
    
    
    
 def price_distribution(df):
    df_temp = df[df['SALE PRICE'] < 3000000]
    viz=sns.violinplot(data=df_temp, x='BOROUGH', y='SALE PRICE')
    viz.set_title('Density and distribution of prices for each Borough')
    plt.xlabel('BOROUGH')
    plt.ylabel('SALE PRICE')
    plt.show()
    
    
    
    
    
def data_distribution_in_classes(df):
    
    df2 = df.loc[(df['BROAD BUILDING CLASS'] == 'R') | (df['BROAD BUILDING CLASS'] == 'A') | 
                 (df['BROAD BUILDING CLASS'] == 'D') | (df['BROAD BUILDING CLASS'] == 'B') |
                 (df['BROAD BUILDING CLASS'] == 'C')]

    xaxis = [BOROUGH for BOROUGH, df in df.groupby('BOROUGH')]

    pos = np.arange(5)

    y1 = df.loc[df['BROAD BUILDING CLASS'] == 'R'].groupby(['BOROUGH']).count()['BROAD BUILDING CLASS']
    y2 = df.loc[df['BROAD BUILDING CLASS'] == 'A'].groupby(['BOROUGH']).count()['BROAD BUILDING CLASS']
    y3 = df.loc[df['BROAD BUILDING CLASS'] == 'D'].groupby(['BOROUGH']).count()['BROAD BUILDING CLASS']
    y4 = df.loc[df['BROAD BUILDING CLASS'] == 'B'].groupby(['BOROUGH']).count()['BROAD BUILDING CLASS']
    y5 = df.loc[df['BROAD BUILDING CLASS'] == 'C'].groupby(['BOROUGH']).count()['BROAD BUILDING CLASS']

    plt.bar(pos, y1, label = 'Residential, Condos, & Commercial')
    plt.bar(pos, y2, label = '1 Family, Townhouses, Mansions', bottom = y1)
    plt.bar(pos, y3, label = 'Elevator Apartments', bottom = np.add(y1,y2))
    plt.bar(pos, y4, label = '2 Family Homes', bottom = np.add(np.add(y2,y3),y1))
    plt.bar(pos, y5, label = '3 or More Family Homes and Walk Ups', bottom = np.add(np.add(np.add(y3,y4),y2),y1))


    plt.ylabel('Number of Properties', size = 12)
    plt.xlabel('Boroughs', size = 12)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1), ncol=1)
    plt.title('The Distribution of the 5 Classes of Buildings', size = 14)
    plt.xticks(pos, xaxis)
    plt.show()
    
    
  
  
  
  
  
  
  
  
def variation_in_price_building_class(df):
    fig = plt.figure(figsize=(12,10))
    fig.subplots_adjust(hspace=1, wspace=0.75)

    plt.subplot(1,5,1)
    df[df["BROAD BUILDING CLASS"] == "R"].groupby(["BOROUGH"])['SALE PRICE'].median().sort_values(ascending=True).head(40).plot.barh(color="skyblue")
    plt.xticks(rotation=50, size=10, ha='right')
    plt.yticks(size=10, rotation=50)
    plt.title(label='Class R Median Prices', size=12, color='purple')
    plt.xlim(0,1000000)


    plt.subplot(1,5,2)
    df[df["BROAD BUILDING CLASS"] == "A"].groupby(["BOROUGH"])['SALE PRICE'].median().sort_values(ascending=True).head(40).plot.barh(color="skyblue")
    plt.xticks(rotation=50, size=10, ha='right')
    plt.yticks(size=10, rotation=50)
    plt.title(label='Class A Median Prices', size=12, color='purple')
    plt.xlim(0,1000000)

    plt.subplot(1,5,3)
    df[df["BROAD BUILDING CLASS"] == "D"].groupby(["BOROUGH"])['SALE PRICE'].median().sort_values(ascending=True).head(40).plot.barh(color="skyblue")
    plt.xticks(rotation=50, size=10, ha='right')
    plt.yticks(size=10, rotation=50)
    plt.xlabel("Median Price in New York", size=15, color='brown')
    plt.title(label='Class D Median Prices', size=12, color='purple')
    plt.xlim(0,1000000)

    plt.subplot(1,5,4)
    df[df["BROAD BUILDING CLASS"] == "B"].groupby(["BOROUGH"])['SALE PRICE'].median().sort_values(ascending=True).head(40).plot.barh(color="skyblue")
    plt.xticks(rotation=50, size=10, ha='right')
    plt.yticks(size=10, rotation=50)
    plt.title(label='Class B Median Prices', size=12, color='purple')
    plt.xlim(0,1000000)
    
    plt.subplot(1,5,5)
    df[df["BROAD BUILDING CLASS"] == "C"].groupby(["BOROUGH"])['SALE PRICE'].median().sort_values(ascending=True).head(40).plot.barh(color="skyblue")
    plt.xticks(rotation=50, size=10, ha='right')
    plt.yticks(size=10, rotation=50)
    plt.title(label='Class C Median Prices', size=12, color='purple')
    plt.xlim(0,1000000)


    plt.show()
    
    
    
    
    
    
    
    
    
def sale_price_distribution(df):
    df3 = df[df['BOROUGH'].isin(['Manhattan','Brooklyn','Queens'])]

    xaxis = [BOROUGH for BOROUGH, df3 in df3.groupby('BOROUGH')]

    pos = np.arange(3)

    dfR = df3.loc[df3['BROAD BUILDING CLASS'] == 'R']
    dfA = df3.loc[df3['BROAD BUILDING CLASS'] == 'A']
    dfD = df3.loc[df3['BROAD BUILDING CLASS'] == 'D']
    dfB = df3.loc[df3['BROAD BUILDING CLASS'] == 'B']
    dfC = df3.loc[df3['BROAD BUILDING CLASS'] == 'C']

    y1 = dfR['SALE PRICE'].groupby(dfR['BOROUGH']).mean()
    y2 = dfA['SALE PRICE'].groupby(dfA['BOROUGH']).mean()
    y3 = dfD['SALE PRICE'].groupby(dfD['BOROUGH']).mean()
    y4 = dfB['SALE PRICE'].groupby(dfB['BOROUGH']).mean()
    y5 = dfC['SALE PRICE'].groupby(dfC['BOROUGH']).mean()

    width = 0.1

    plt.bar(pos - 0.1, y1, width, label = 'Residential, Condos, & Commercial')
    #plt.plot(pos, y2, label = '1 Family, Townhouses, Mansions')
    plt.bar(pos, y3, width,  label = 'Elevator Apartments')
    #plt.plot(pos, y4, label = '2 Family Homes')
    plt.bar(pos + 0.1, y5, width, label = '3 or More Family Homes and Walk Ups')


    plt.ylabel('Sale Price', size = 12)
    plt.xlabel('Boroughs', size= 12)
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1), ncol=1)
    plt.title('Sale Price of the 3 Classes of Buildings', size = 14)

    plt.xticks(pos, xaxis)
    plt.show()
    
    
    
    
    

def price_variation_with_age(df):
    df3 = df[df['BOROUGH'].isin(['Manhattan','Brooklyn','Queens'])]
    #notreal = df3[df3['AGE OF BUILDING'] > 500]
    df3 = df3[df3['AGE OF BUILDING'] < 70]
    #df3 = df3.drop(i)

    dfRandM = df3.loc[(df['BROAD BUILDING CLASS'] == 'R') & (df3['BOROUGH'] == 'Manhattan')]
    dfRandQ = df3.loc[(df['BROAD BUILDING CLASS'] == 'R') & (df3['BOROUGH'] == 'Queens')]
    dfRandBK = df3.loc[(df['BROAD BUILDING CLASS'] == 'R') & (df3['BOROUGH'] == 'Brooklyn')]



    xaxis1 = [AGE for AGE, dfRandM in dfRandM.groupby(['AGE OF BUILDING'])]
    xaxis2 = [AGE for AGE, dfRandQ in dfRandQ.groupby(['AGE OF BUILDING'])]
    xaxis3 = [AGE for AGE, dfRandBK in dfRandBK.groupby(['AGE OF BUILDING'])]


    y1 = dfRandM['SALE PRICE PER UNIT AREA'].groupby(dfRandM['AGE OF BUILDING']).mean()
    y2 = dfRandQ['SALE PRICE PER UNIT AREA'].groupby(dfRandQ['AGE OF BUILDING']).mean()
    y3 = dfRandBK['SALE PRICE PER UNIT AREA'].groupby(dfRandBK['AGE OF BUILDING']).mean()


    plt.plot(xaxis1, y1, label = 'Manhattan')
    plt.plot(xaxis2, y2, label = 'Queens')
    plt.plot(xaxis3, y3, label = 'Brooklyn')

    plt.legend(loc = "upper right", )
    plt.xlabel('Age of Building')
    plt.ylabel('Average Sale Price per Square Foot $')
    plt.title('Average Sale Price per Square Foot for Building Class R for Different Age')

    plt.show()
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
  
  
  
  
  
