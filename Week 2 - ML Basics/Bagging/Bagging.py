#We will use pima indian diabetes dataset to predict if a person has a diabetes or not 
#based on certain features such as blood pressure, skin thickness, age etc. 
#We will train a standalone model first and then use bagging ensemble technique to check how it can improve the performance of the model
import pandas as pd
df = pd.read_csv("diabetes.csv")
X = df.drop("Outcome",axis="columns")
y = df.Outcome
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, stratify=y, random_state=10)
from sklearn.model_selection import cross_val_score
#train using stand alone model
from sklearn.tree import DecisionTreeClassifier
scores = cross_val_score(DecisionTreeClassifier(), X, y, cv=5)
print(scores.mean())
#training using bagging
from sklearn.ensemble import BaggingClassifier
bag_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(), 
    n_estimators=100, 
    max_samples=0.8, 
    oob_score=True,
    random_state=0
)
bag_model.fit(X_train, y_train)
print(bag_model.oob_score_)
print(bag_model.score(X_test, y_test))
scores = cross_val_score(bag_model, X, y, cv=5)
print(scores.mean())
from sklearn.ensemble import RandomForestClassifier
scores = cross_val_score(RandomForestClassifier(n_estimators=50), X, y, cv=5)
print(scores.mean())

