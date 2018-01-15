'''
Created on 2018年1月15日

@author: Administrator
'''
import matplotlib.pyplot  as plt
import pandas as pd
from matplotlib.pyplot import pcolor

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url,header=None,prefix= 'V')

for i in range(208):
    if data.iat[i,60] == 'M': # 根据索引查找值
        pcolor = 'red'
    else:
        pcolor = 'blue'
    dataRow = data.iloc[i,0:60]
    dataRow.plot(color = pcolor)   
# dataRow = data.iloc[i,0:60]
# dataRow.plot(color = pcolor) 
plt.show()