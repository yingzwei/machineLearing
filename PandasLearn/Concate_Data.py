'''
Created on 2018年1月10日
pandas 数据合并
@author: Administrator
'''
import pandas as pd
import numpy as np

''' 简单合并
df1 =  pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 =  pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 =  pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

# 合并函数concat，  axis=0 表示纵向
resrc = pd.concat([df1,df2,df3], axis=0, ignore_index=True)

print(resrc)
'''
''' 相同行列合并
#
df1 =  pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 =  pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[1,2,3])
df3 =  pd.DataFrame(np.ones((3,4))*2, columns=['c','d','e','f'], index=[1,2,3])

# 合并函数 concat，  join='inner'表示合并相同列行数据 or 'outer' 直接合并 没有数据行列以Nan填充
# 参数 join_axis=[df1.index] 数据已df1的索引进行合并
resrc = pd.concat([df1,df2,df3], join='inner', ignore_index=True)

print(resrc)
'''
# append
df1 =  pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 =  pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[1,2,3])
df3 =  pd.DataFrame(np.ones((3,4))*2, columns=['c','d','e','f'], index=[1,2,3])

res =df1.append(df2,ignore_index=True)
res1 = df1.append(df3)
series1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res2 =df1.append(series1,ignore_index=True)
print(res)