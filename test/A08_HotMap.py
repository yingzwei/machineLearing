'''
Created on 2018�?1�?16�?
热力�?
@author: Administrator
'''
import matplotlib.pyplot as plt
from pandas import DataFrame as df
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'
data = pd.read_csv(url, header=None ,prefix= 'V')

corMat = df(data.corr())
# print(corMat)
plt.pcolor(corMat)
plt.show()