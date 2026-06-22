#Exercise predict for year 2020
import pandas as pd
from sklearn import linear_model
Canadadf = pd.read_csv("canada_per_capita_income.csv")
pre = linear_model.LinearRegression()

pre.fit(Canadadf[['year']], Canadadf["per capita income (US$)"])
#print(pre.predict([[2020]])) #ANS :[41288.69409442]

#Linear Regression in Multiple Variables
df2 = pd.DataFrame({"area":[2600,3000,3200,3600,4000],"bedrooms":[3,4,3.5,3,5],"age":[20,15,18,30,8],"price":[550000,565000,610000,680000,725000]})                  
#for null values just fillna median which can be calculated with math module
regr = linear_model.LinearRegression()
regr.fit(df2[["area","bedrooms","age"]],df2.price)
print(regr.predict([[3000,3,40]]))
