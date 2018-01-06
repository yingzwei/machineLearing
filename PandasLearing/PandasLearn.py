import pandas as pd
from sklearn import preprocessing 
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.feature_extraction import DictVectorizer
from numba.tests.test_deprecations import dummy
from statsmodels.genmod.tests.results.results_glm_poisson_weights import predicted


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
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print('dummyY:' + str(dummyY))

# using decision tree for classfication
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
print('clf' + str(clf))

with open("allElectronicInformationGainOri.dot", 'w') as f:
    f= tree.export_graphviz(clf, feature_names=vec.get_feature_names(),out_file=f)

oneRowx = dummyX[0,:]
print('oneRowX:' + str(oneRowx))

newRowX = oneRowx
newRowX[0] = 1
newRowX[1] = 0
print('newRowX:' + str(newRowX))

predictedY = clf.predict(newRowX)
print('predictedY:' + str(predictedY))