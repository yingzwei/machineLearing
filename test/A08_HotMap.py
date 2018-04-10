'''
Created on 2018å¹?1æœ?16æ—?
çƒ­åŠ›å›?
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