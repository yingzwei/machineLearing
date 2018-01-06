import pandas as pd
from sklearn import preprocessing 
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.feature_extraction import DictVectorizer
from numba.tests.test_deprecations import dummy


data = pd.read_csv('tree.csv')
# print(data.head(0))
heads = data.columns

featureList = []
labelList = []

for row in data.values:
    labelList.append(row[len(row)-1])
    rowDict = {}
    for i in range(1, len(row)-1):
        rowDict[heads[i]] = row[i]
    featureList.append(rowDict)
print(featureList)    

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()


print('dummyX:' + str(dummyX))
print(vec.get_feature_names())

# vectorize class labels