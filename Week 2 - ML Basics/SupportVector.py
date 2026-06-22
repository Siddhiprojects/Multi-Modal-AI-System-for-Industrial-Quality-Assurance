'''import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns = iris.featurenames)
df['target'] = iris.target
df['flowername'] = df.target.apply(lambda x: iris.target_names[x])
from sklearn.model_selection import train_test_split
x = df.drop(['target','flowername'], axis = "columns")
y = df.target
x_train , x_test , y_train  , y_test = train_test_split(x,y,test_size= 0.2)
from sklearn.svm import SVC
model = SVC()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))'''

#Exercise
import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()
df = pd.DataFrame(digits.data,digits.target)
df['target'] = digits.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('target',axis='columns'), df.target, test_size=0.3)
from sklearn.svm import SVC
rbf_model = SVC(kernel='rbf')
print(len(X_train))
#1257
print(len(X_test))
#540
rbf_model.fit(X_train, y_train)
'''SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)'''
print(rbf_model.score(X_test,y_test))
#0.57592592592592595
#Using Linear kernel

linear_model = SVC(kernel='linear')
linear_model.fit(X_train,y_train)
'''SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)'''
print(linear_model.score(X_test,y_test))
#0.97407407407407409