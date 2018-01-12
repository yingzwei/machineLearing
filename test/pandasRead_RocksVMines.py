'''
Created on 2018年1月12日

@author: Administrator
'''
import pandas as pd
import numpy as np


data = pd.read_pickle('outData.pkl')
# print(np.shape(data))

type = [0]*3
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

# calculate quantile boundaries  计算分数边界