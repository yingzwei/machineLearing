'''
Created on 2018年1月10日

@author: Administrator
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


series1 = pd.Series(np.random.randn(500), np.arange(500))
series1.cumsum()
#series1.plot()

# DataFrame
dataFrame1 = pd.DataFrame(np.random.rand(1000,4), index=np.arange(1000),
                          columns =list('ABCD'))
# bar,hist,box,box,kde,area,scatter,hexbin,pie
dataFrame1.cumsum()
ax = dataFrame1.plot.scatter(x='A',y='B',color='red',label='Class1')
dataFrame1.plot.scatter(x='A',y='C',color='Green',label='Class2', ax=ax)
plt.show()