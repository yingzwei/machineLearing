'''
Created on 2018年1月16日
计算相关度    R^2 计算函数
@author: Administrator
'''
import numpy as np
import pandas as pd
from math import sqrt as sqr

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')

data2 = data.iloc[1,0:60]
data3 = data.iloc[2,0:60]
data21 = data.iloc[20,0:60]

def ComputeCorrLation(X,Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0; varX = 0; varY = 0
    for i in range(len(X)):
        diffXbar = X[i] - xBar
        diffYbar = Y[i] - yBar
        SSR += (diffXbar * diffYbar)
        varX += diffXbar ** 2
        varY += diffYbar **2
    SST = sqr(varX * varY)
    return SSR / SST

Corr23 = ComputeCorrLation(data2, data3)
Corr23 = ComputeCorrLation(data2, data3)**2
Corr221 = ComputeCorrLation(data2, data21)
print('Corr23:%f, Corr221:%f' %(Corr23, Corr221))


# polynomial regression
def polyFit(x,y,degree):
    result = {}
    coeffs = np.polyfit(x.tolist(), y.tolist(), degree)
    # polynomial coefficients
    result['polynomial'] = coeffs.tolist()
    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)
    yBar = np.sum(y) / len(y)
    ssreg = np.sum((yhat-yBar)**2)
    sstot = np.sum((y-yBar)**2)
    result['determination'] = ssreg / sstot
    return result

print(polyFit(data2,data3,1))