import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('./Melbourne_housing_FULL.csv')
cols_to_use = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 'Regionname', 'Propertycount', 
               'Distance', 'CouncilArea', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price']
dataset = dataset[cols_to_use]
# Some feature's missing values can be treated as zero (another class for NA values or absence of that feature)
# like 0 for Propertycount, Bedroom2 will refer to other class of NA values
# like 0 for Car feature will mean that there's no car parking feature with house
cols_to_fill_zero = ['Propertycount', 'Distance', 'Bedroom2', 'Bathroom', 'Car']
dataset[cols_to_fill_zero] = dataset[cols_to_fill_zero].fillna(0)

# other continuous features can be imputed with mean for faster results since our focus is on Reducing overfitting
# using Lasso and Ridge Regression
dataset['Landsize'] = dataset['Landsize'].fillna(dataset.Landsize.mean())
dataset['BuildingArea'] = dataset['BuildingArea'].fillna(dataset.BuildingArea.mean())
dataset.dropna(inplace=True)
dataset = pd.get_dummies(dataset, drop_first=True)
X = dataset.drop('Price', axis=1)
y = dataset['Price']
from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=2)
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(train_X, train_y)
reg.score(test_X, test_y)
reg.score(train_X, train_y)
#Score is very low, normal regression is overfitting data
#Using Lasso (L1 Regularized) Regression Model
from sklearn import linear_model
lasso_reg = linear_model.Lasso(alpha=50, max_iter=100, tol=0.1)
lasso_reg.fit(train_X, train_y)
lasso_reg.score(test_X, test_y)
lasso_reg.score(train_X, train_y)
#Using Ridge (L2 Regularized) Regression Model
from sklearn.linear_model import Ridge
ridge_reg= Ridge(alpha=50, max_iter=100, tol=0.1)
ridge_reg.fit(train_X, train_y)
ridge_reg.score(test_X, test_y)
ridge_reg.score(train_X, train_y)
#We see that Lasso and Ridge Regularizations prove to be beneficial
#when our Simple Linear Regression Model overfits. 
#These results may not be that contrast but significant in most cases.
#Also that L1 & L2 Regularizations are used in Neural Networks too
