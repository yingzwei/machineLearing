'''
Created on 2018年1月15日
分类问题标签与实数值属性之间的相关性
@author: Administrator
'''
import pandas as pd
import matplotlib.pyplot as plt
from random import uniform

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')
# print(data)
target = []
for i in range(208):
    if data.iat[i,60] =='M':
        target.append(1.0)
    else:
        target.append(0.0)
        
dataRow = data.iloc[0:208,35]
print(dataRow.describe())
# print(len(dataRow))
# print(len(target))
plt.subplot(211)
plt.scatter(dataRow,target)


target1 = []
for i in range(208):
    if data.iat[i,60] =='M':
        target1.append(1+uniform(-0.1,0.1))
    else:
        target1.append(0.0+uniform(-0.1,0.1))
        
dataRow1 = data.iloc[0:208,35]
plt.subplot(212)
plt.scatter(dataRow1,target1, alpha = 0.5)
plt.show()