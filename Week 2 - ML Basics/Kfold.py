from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
#K-fold cross validation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.3)
#Logistic Regression
lr = LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train, y_train)
print(lr.score(X_test, y_test))
#0.9115191986644408
#SVM
svm = SVC(gamma='auto')
svm.fit(X_train, y_train)
print(svm.score(X_test, y_test))
#0.4273789649415693
#Random Forest
rf = RandomForestClassifier(n_estimators=40)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))
#0.9181969949916527
from sklearn.model_selection import KFold
kf = KFold(n_splits=3) #no of fold
for train_index , test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index,test_index)
def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return print(model.score(X_test, y_test))

from sklearn.model_selection import StratifiedKFold
folds = StratifiedKFold(n_splits=3)
scores_logistic = []
scores_svm = []
scores_rf = []

for train_index, test_index in folds.split(digits.data,digits.target):
     X_train, X_test, y_train, y_test = digits.data[train_index], digits.data[test_index], \
                                       digits.target[train_index], digits.target[test_index]
     scores_logistic.append(get_score(LogisticRegression(), X_train, X_test, y_train, y_test))  
     scores_svm.append(get_score(SVC(), X_train, X_test, y_train, y_test))
     scores_rf.append(get_score(RandomForestClassifier(n_estimators=40), X_train, X_test, y_train, y_test))

from sklearn.model_selection import cross_val_score
#Logistic regression model performance using cross_val_score
print(cross_val_score(LogisticRegression(), digits.data, digits.target))
#first argument is classifier, 2nd is x, 3rd is y,
print(cross_val_score(SVC(), digits.data, digits.target))
print(cross_val_score(RandomForestClassifier(n_estimators=40),digits.data, digits.target))

#Parameter tuning

#Exercise
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np
iris = load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import cross_val_score
print(np.average(cross_val_score(LogisticRegression(),x,y)))
print(np.average(cross_val_score(DecisionTreeClassifier(),x,y)))
print(np.average(cross_val_score(RandomForestClassifier(),x,y)))
print(np.average(cross_val_score(SVC(),x,y)))
#best accuracy of logisticregression