'''
Created on 2018å¹?1æœ?15æ—?

@author: Administrator
'''
import matplotlib.pyplot  as plt
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')

data1 = data.iloc[1,0:60]
data2 = data.iloc[2,0:60]
data21 = data.iloc[20,0:60]
# print(float(data1))
plt.subplot(211)
plt.scatter(x=data1,y=data2,color='red',label='class1')
plt.ylabel('d2')
plt.subplot(212)
plt.scatter(x=data1,y=data21,color='green',label='class2')
plt.ylabel('d21')
plt.show()