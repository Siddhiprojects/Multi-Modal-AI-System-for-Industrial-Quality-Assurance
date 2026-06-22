#Binary Classification
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("insurance_data.csv")
plt.scatter(df.age,df.bought_insurance, marker = '+', color = 'red')
#plt.show()
# split into training and test set
from sklearn.model_selection import train_test_split
x = df[['age']]
y = df.bought_insurance
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
print(model.predict(x_test))
print(model.score(x_test,y_test))
print(model.predict_proba(x_test))


