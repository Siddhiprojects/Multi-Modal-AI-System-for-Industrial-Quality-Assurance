import pandas as pd
df = pd.read_csv("spam.csv")
df.groupby('Category').describe()
#print(df)
df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message,df.spam)
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_count = v.fit_transform(X_train.values)
X_train_count.toarray()[:2]
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train_count,y_train)
emails = [
    'Hey mohan, can we get together to watch footbal game tomorrow?',
    'Upto 20 discount on parking, exclusive offer just for you. Dont miss this reward!'
]
emails_count = v.transform(emails)
print(model.predict(emails_count))
#detects 2nd email a spam
X_test_count = v.transform(X_test)
print(model.score(X_test_count, y_test))
from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])
clf.fit(X_train, y_train)
print(clf.score(X_test,y_test))
print(clf.predict(emails))

#exercise
from sklearn import datasets
wine = datasets.load_wine()
import pandas as pd
df = pd.DataFrame(wine.data,columns=wine.feature_names)
df['target'] = wine.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=100)
from sklearn.naive_bayes import GaussianNB, MultinomialNB
model = GaussianNB()
model.fit(X_train,y_train)
print(model.score(X_test,y_test))
mn = MultinomialNB()
mn.fit(X_train,y_train)
print(mn.score(X_test,y_test))
