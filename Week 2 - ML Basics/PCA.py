#Principal Component Analysis is technique used to reduce dimensions
#identifing features that are important
#Faster training and inference, data visualisation becomes easier
#PCA is a process of figuring out most important features 
# or principal components that has the most impact on the target variable
#PCA(n_components = x)
#Scale features before applying PCA
#Accuracy might drop
from sklearn.datasets import load_digits
import pandas as pd
dataset = load_digits()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
X = df
y = dataset.target
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=30)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
from sklearn.decomposition import PCA
pca = PCA(0.95)
X_pca = pca.fit_transform(X)
X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=30)
#use components such that 95% of variance is retained
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter = 1000)
model.fit(X_train_pca, y_train)
print(model.score(X_test_pca, y_test))
#Bias is a measurement of how accurately a model 
#can capture a pattern in a training dataset