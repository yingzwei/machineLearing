import pandas as pd
from sklearn import preprocessing 
from sklearn import tree
from sklearn.externals.six import StringIO


data = pd.read_csv('tree.csv')
# print(data.head(0))

featureList = []
labelList = []

for row in data:
    labelList.append(row[len(row)-1])

print(labelList)    

