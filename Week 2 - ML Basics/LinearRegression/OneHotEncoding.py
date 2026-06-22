#Saving model using joblib and pickle
'''import pickle
with open('model_pickle','wb') as f:
    pickle.dump(model,f)
with open('model_pickel','rb') as f:
    mp = pickle.load(f)
mp.predict(5000)
'''
#large numpy array joblib is more efficient
'''from sklearn.externals import joblib
joblib.dump(reg,'reg_joblift')
mj = joblib.load('reg_joblib')'''

#using dummy columns
import pandas as pd
df = pd.read_csv("homeprices.csv")
dummies = pd.get_dummies(df.town) #creates dummy variables
#concate dummies with df
merged = pd.concat([df,dummies], axis = 'columns')
final = merged.drop(['town','west windsor'], axis = 'columns')
from sklearn.linear_model import LinearRegression
model = LinearRegression()
x = final.drop('price', axis = 'columns') #removing dependent variable
y = final.price
model.fit(x,y)
#look at x first to give paameters to model.predict 
# 2800 sq fit in robinsville
print(model.predict([2800,0,1]))
#3400 sq ft in west windsor
print(model.predict([3400,0,0]))
#to check accuracy model.score(x,y)

#one hot encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dfle = df
dfle.town =le.fit_transform(dfle.town)
x = df[['town','area']].values # gives 2D array
y = dfle.price
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0])
ohe.fit_transform(x).toarray()
X = x[:,1:]
model.fit(X,y)
print(model.predict([1,0,2800]))

#training testing
'''from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state= 10)
#random state is for same data set
reg.fit(x_train,y_train)
reg.predict(x_test)
reg.score(x_test, y_test)'''


