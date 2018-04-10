'''
Created on 2018�?1�?15�?

@author: Administrator
'''
import pandas as pd
import pylab
import scipy.stats as sta


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data'

data = pd.read_csv(url,header=None,prefix= 'V')
print(data.tail())
print(data.describe())  # 统计dataFrame中均值�?�标准偏差�?�最小�?��??4百分位数、最大�??
sta.probplot(data.iloc[:,3], dist='norm',plot =pylab)
pylab.show()