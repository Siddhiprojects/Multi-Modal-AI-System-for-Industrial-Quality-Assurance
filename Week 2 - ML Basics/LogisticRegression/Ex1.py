#Exercise
import pandas as pd
df2 = pd.read_csv("HR_comma_sep.csv")
#Data Analysis and Visualisation
left = df2[df2.left==1]
retained = df2[df2.left==0]
df2.groupby('left').mean()
#Variables: Satisfaction, avg work hours, promotion, Salary
subdf = df2[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
salary_dummies = pd.get_dummies(subdf.salary, prefix="salary")
df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')
df_with_dummies.drop('salary',axis='columns',inplace=True)
X = df_with_dummies
y = df2.left
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.3)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
model.predict(X_test)
print(model.score(X_test,y_test))