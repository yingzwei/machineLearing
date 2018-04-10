'''
Created on 2018å¹?1æœ?16æ—?

@author: Administrator
'''
import matplotlib.pyplot as plt
from pandas import DataFrame as df
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
abalone_data = pd.read_csv(url, header=None ,prefix= 'V')
abalone_data.columns=['sex','length','Diameter','height','Whole weight',
                      'Shucked weight','Viscera weight','Shell weight','Rings']
print(abalone_data.head())
pd.to_pickle(abalone_data,'./abalone.data')