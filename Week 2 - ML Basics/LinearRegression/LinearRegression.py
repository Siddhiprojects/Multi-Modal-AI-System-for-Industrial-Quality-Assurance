#Linear Regression single Variable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.DataFrame({"Area":[2600,3000,3200,3600,4000],"Price":[550000,565000,610000,680000,725000]})
plt.scatter(df.Area,df.Price,color = 'red', marker= '+')
plt.xlabel("Area")
plt.ylabel("price")
#plt.show()
reg = linear_model.LinearRegression() #creating an object for LinearRegression
reg.fit(df[['Area']],df.Price) #fit means you are training, first argument is a 2D array
#print(reg.predict([[3300]]))
#inside it is calculating best fit line y = mx+c reg.coeff_ & reg.intercept_
d = pd.DataFrame({"Area":[1000,1500,2000]})
p = reg.predict(d)
d["Price"]= p
#print(pd.concat([d,df]))
plt.plot(df.Area,reg.predict(df[['Area']]),color = 'blue')
#plt.show()


