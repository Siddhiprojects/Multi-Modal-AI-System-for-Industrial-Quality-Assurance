import pandas as pd
s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
df = pd.DataFrame({"names":['Harry','Ron','Hermione'], "age":[12,13,12]})
print(s)
print(df)
#pd.read_cv
#df.head(),df.tail(), df.describe(),df.info(), df["column"],df[["column1","column2"...]]
#df.iloc[rowindex], df.dropna(), df.fillna(0, inplace=True) changes original
#df.rename(columns = {dictonary}), df["column"][rowindex], len(df) , df.drop
#df["zeroes"]= [0 for i in range(len(df))]
'''def fx(a):
    return a+1
df["new column"]= df["old column"].apply(fx)'''
# df.to_csv(data/export.csv, index = False0
#pd.concat([df1,df2])
