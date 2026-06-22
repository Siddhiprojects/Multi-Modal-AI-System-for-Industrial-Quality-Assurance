# k-nearest neighbours
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['target'] = iris.target
df['flower_name'] =df.target.apply(lambda x: iris.target_names[x])
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
X = df.drop(['target','flower_name'], axis='columns')
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test))
print(knn.predict([[4.8,3.0,1.5,0.3]]))

#Exercise
from sklearn.datasets import load_digits
digits = load_digits()
import pandas as pd
df = pd.DataFrame(digits.data,digits.target)
df['target'] = digits.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis='columns'), df.target, test_size=0.3, random_state=10)
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
print(knn.score(X_test,y_test))

from sklearn.model_selection import GridSearchCV
clf = GridSearchCV(KNeighborsClassifier(), {'n_neighbors' : [1,2,3,4,5,6,7,8,9]},
                    cv = 5, return_train_score=False)
clf.fit(X_train,y_train)
df = pd.DataFrame(clf.cv_results_)[['param_n_neighbors','mean_test_score']]
print(df)
#k = 5