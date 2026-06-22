#Exercise first plot data on scatter plot to check if linear regression can be applied
import pandas as pd
import matplotlib.pyplot as plt
dfex = pd.read_csv("carprices.csv")
from sklearn.linear_model import LinearRegression
plt.scatter(dfex['Car Model'], dfex['Sell Price($)'])
plt.scatter(dfex['Mileage'], dfex['Sell Price($)'])
plt.scatter(dfex['Age(yrs)'], dfex['Sell Price($)'])
plt.show()
reg = LinearRegression()
dummies = pd.get_dummies(dfex['Car Model'])
merged = pd.concat([dfex,dummies], axis = 'columns')
x = merged.drop(['Car Model','Mercedez Benz C class','Sell Price($)'], axis = 'columns')
y = dfex['Sell Price($)']
reg.fit(x,y)
print(reg.predict([[45000,4,0,0]]))
print(reg.predict([[86000,7,0,1]]))
print(reg.score(x,y))
