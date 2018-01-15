'''
Created on 2018年1月15日

@author: Administrator
'''
import matplotlib.pyplot  as plt
import pandas as pd
from math import sqrt

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')

data2 = data.iloc[1,0:60]
data3 = data.iloc[2,0:60]
data21 = data.iloc[20,0:60]

mean2=0.0; mean3=0.0; mean21=0.0
numElt = len(data3)
for i in range(numElt):
    mean2+= data2[i]/numElt
    mean3+= data3[i]/numElt
    mean21+= data21[i]/numElt
    
var2=0.0; var3=0.0; var21=0.0
for i in range(numElt):
    var2+= (data2[i]-mean2)*(data2[i]-mean2)/numElt
    var3+= (data3[i]-mean3)*(data3[i]-mean3)/numElt
    var21+= (data21[i]-mean21)*(data21[i]-mean21)/numElt    
    
corr23=0.0; corr221=0.0
for i  in range(numElt):
    corr23 += (data2[i]-mean2)*(data3[i]-mean3)/(sqrt(var2*var3))*numElt
    corr221 += (data2[i]-mean2)*(data21[i]-mean21)/(sqrt(var2*var21))*numElt
    
print('corr23:%f ,corr221: %f' %(corr23,corr221))