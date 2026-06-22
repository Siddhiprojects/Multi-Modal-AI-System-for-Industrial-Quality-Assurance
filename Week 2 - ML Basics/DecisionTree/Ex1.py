#Exercise
import pandas as pd
df2 = pd.read_csv("titanic.csv")
x = df2.drop(['Survived','PassengerId','Name', 'SibSp','Parch','Ticket','Cabin','Embarked'], axis = "columns")
y = df2['Survived']
from sklearn.preprocessing import LabelEncoder
le_Sex = LabelEncoder()
x['Sex_n'] = le_Sex.fit_transform(x['Sex'])
x_n = x.drop(['Sex'], axis = "columns")
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(x_n,y)
print(model.score(x_n,y))
