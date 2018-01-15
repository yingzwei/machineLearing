'''
Created on 2018年1月12日

@author: Administrator
'''
import pandas as pd
import numpy as np


data = pd.read_pickle('outData.pkl')
# print(np.shape(data))

# type = [0]*3
col = 3
colData = []
for row in data:
#     print(row)
    colData.append(row[:,3])
colArray = np.array(colData)
# print(colArray)

colMean = np.mean(colArray) # 计算平均值
colstd = np.std(colArray)  # 计算标准偏差
#print(colMean)
#print(colstd)

# calculate quantile boundaries  计算4百分位数
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
print(percentBdry)

# calculate quantile boundaries  计算10百分位数
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))
print(percentBdry)

# the last column contains categorical variables
col = 60
colData =[]
for row in data:
    if row[:,col]==1:
        colData.append('R')
    else:
        colData.append('M')
unique = set(colData)
print(unique)

# count up the number of elements having each value
catDic = dict(zip(unique,range(len(unique))))
print(catDic)
catCount = [0]* 2
for elements in colData:
    catCount[catDic[elements]] +=1
print(catCount)