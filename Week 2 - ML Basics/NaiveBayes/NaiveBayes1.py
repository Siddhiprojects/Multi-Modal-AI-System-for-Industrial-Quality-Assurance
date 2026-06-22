import pandas as pd
df = pd.read_csv("titanic.csv")
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
inputs = df.drop('Survived',axis='columns') #independent variables
target = df.Survived #dependent vairables
#sex column is text
dummies = pd.get_dummies(inputs.Sex)
inputs = pd.concat([inputs,dummies],axis='columns')
inputs.drop(['Sex','male'],axis='columns',inplace=True)
inputs.Age = inputs.Age.fillna(inputs.Age.mean())
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))

#Calculate the score using cross validation
from sklearn.model_selection import cross_val_score
print(cross_val_score(GaussianNB(),X_train, y_train))
