'''
Created on 2018å¹?1æœ?11æ—?

@author: Administrator
'''
import numpy as np
import pandas as pd
import re
import urllib.request as req


data = req.urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data')
# print(data.read())
xList = []
label = []
for line in data:
    row = str(line).strip().split(",")
    l = len(row)
#     print(l)
    xRow = np.zeros(shape=l)
#     print(xRow)
    for i in range(0,l):
        r = row[i]
        a =  re.sub("\-*\d+(?:\.\d+)?", "", r)
#         print(a)
        if a.find('M') != -1 :
            xRow[i] =0
        elif a.find('R') != -1 :
            xRow[i] =1 
        else:
            a = r.replace(a,'')
#             print(a)
            xRow[i] = float('%.4f' %float(a))
    xList.append(xRow)

mat_list = np.mat(xList)
print(np.shape(mat_list))
print(mat_list)

pd.to_pickle(mat_list,'./outData.pkl')
