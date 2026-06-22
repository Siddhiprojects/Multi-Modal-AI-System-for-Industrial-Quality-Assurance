#It matters in which order you split the tree
#Low entropy low degree of randomness
import pandas as pd
df = pd.read_csv("salaries.csv")
inputs = df.drop(['salary_more_then_100k'])
target = df['salary_more_then_100k']
from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])
#add new dummies column using labelencoder on a specific column
inputs_n = inputs.drop(['company','job','degree'],axis='columns')
#make the data as required using dummy
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)
print(model.score(inputs_n,target)) # it would be 1 because its the same set you train
print(model.predict([[2,2,1]]))


