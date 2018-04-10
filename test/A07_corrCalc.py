'''
Created on 2018å¹?1æœ?15æ—?

@author: Administrator
'''
from math import sqrt
import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')

data2 = data.iloc[1,0:60]
data3 = data.iloc[2,0:60]
data21 = data.iloc[20,0:60]

mean2=0.0; mean3=0.0; mean21=0.0
numElt = len(data3)
mean2 = np.mean(data2)
mean3 = np.mean(data3)
mean21 = np.mean(data21)
# print(mean2)
# print(mean3)
# print(mean21)
    
var2=0.0; var3=0.0; var21=0.0
for i in range(numElt):
    var2 += (data2[i]-mean2)*(data2[i]-mean2)
    var3 += (data3[i]-mean3)*(data3[i]-mean3)
    var21 += (data21[i]-mean21)*(data21[i]-mean21)   
# print(var2)   
# print(var3)   
# print(var21)   
corr23=0.0; corr221=0.0
for i  in range(numElt):
    corr23 += (data2[i]-mean2)*\
    (data3[i]-mean3)/(sqrt(var2*var3))
    corr221 += (data2[i]-mean2)*\
    (data21[i]-mean21)/(sqrt(var2*var21))
    
print('corr23:%f ,corr221: %f' %(corr23,corr221))