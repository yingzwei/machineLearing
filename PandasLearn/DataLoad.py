'''
Created on 2018年1月9日
数据读取
@author: Administrator
'''
import numpy as np
import pandas as pd

dates = pd.date_range('20180109',  periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates
                  ,columns=['A','B','C','D'])

print(df)
# 根据列名取数据
#print(df['A'],df.A)
# 根据索引取数据
#print(df[0:3])
# 根据label取数据
#print(df['20180109':'20180111'])
#print(df.loc['20180109',['A','C']])
# 根据索引取数据
#print(df.iloc[[1,3,5],1:3])

# 根据索引和标签筛选取数据
#print(df.ix[[1,3,5],['A','C']])

# 根据布尔索引筛选数据
print(df[df.A>8])