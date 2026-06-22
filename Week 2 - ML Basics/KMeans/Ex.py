#exercise
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
iris = load_iris()
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(iris.data, columns = iris.feature_names)
df.drop(['sepal length (cm)','sepal width (cm)'], axis = "columns", inplace = True)
#print(df)
km = KMeans(n_clusters=3)
yp = km.fit_predict(df)
df['Clusters'] = yp
#print(df)
'''df0 = df[df['Clusters']==0]
df1 = df[df['Clusters']==1]
df2 = df[df['Clusters']==2]
plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'], color = 'red')
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'], color = 'blue')
plt.scatter(df2['petal length (cm)'],df2['petal width (cm)'], color = 'green')
#plt.show()'''
#Trying scaling
scale = MinMaxScaler()
scale.fit(df[['petal width (cm)']])
df['petal width (cm)']= scale.transform(df[['petal width (cm)']])
df['petal length (cm)']= scale.fit_transform(df[['petal length (cm)']])
#print(df)
km = KMeans(n_clusters=3)
yp = km.fit_predict(df)
df['Clusters']= yp
'''df0 = df[df['Clusters']==0]
df1 = df[df['Clusters']==1]
df2 = df[df['Clusters']==2]
plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'], color = 'red')
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'], color = 'blue')
plt.scatter(df2['petal length (cm)'],df2['petal width (cm)'], color = 'green')
plt.show()'''
#Scaling is giving same plot
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df)
    sse.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)
plt.show()
#elbow at k = 3

