'''
Created on 2018年1月16日
热力图
@author: Administrator
'''
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')

corMat = df(data.corr())
# print(corMat)
plt.pcolor(corMat)
plt.show()