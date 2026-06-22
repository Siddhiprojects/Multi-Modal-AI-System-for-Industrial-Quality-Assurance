#Multiclass Classification
from sklearn.datasets import load_digits
digits = load_digits()
import matplotlib.pyplot as plt #sklearn already has datasets for practise
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, test_size=0.2)
model.fit(X_train, y_train)
model.score(X_test, y_test)
model.predict(digits.data[0:5])
#confusion methods for checking about the score
y_predicted = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predicted)
print(cm)#This gives array
#better to visualise this
#Exercise
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
from sklearn.model_selection import train_test_split
iris = load_iris()
x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target, test_size=0.1)
model.fit(x_train,y_train)
print(iris.target[67])
print(model.predict([iris.data[67]]))
#to know target classes iris.target_names()
