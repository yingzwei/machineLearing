'''
Created on 2018�?1�?15�?

@author: Administrator
'''
from matplotlib.pyplot import pcolor
import matplotlib.pyplot  as plt
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url,header=None,prefix= 'V')

for i in range(208):
    if data.iat[i,60] == 'M': # 根据索引查找�?
        pcolor = 'red'
    else:
        pcolor = 'blue'
    dataRow = data.iloc[i,0:60]
    dataRow.plot(color = pcolor)   
# dataRow = data.iloc[i,0:60]
# dataRow.plot(color = pcolor) 
plt.show()