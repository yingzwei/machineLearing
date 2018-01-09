'''
Created on 2018年1月9日
数据处理
@author: Administrator
'''
import numpy as np
import pandas as pd

dates = pd.date_range('20180109',  periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates
                  ,columns=['A','B','C','D'])

df.iloc[0,1] = np.nan
df.iloc[2,3] = np.nan
# 添加列数据
x = df.iloc[:,0]
#print(x)
x_category = [0,0,0]
x_dummy=[]
for row in x:
    if row<4:
        x_category[0]=1
    if 4<=row & row<=15:
        x_category[1]=1
    if row>15:
        x_category[2]=1
    x_dummy.append(x_category)
    x_category = [0,0,0]
# 将数列转换为矩阵
x_mat = np.mat(x_dummy)
# 给pandas添加列
df['E'] = x_mat[:,0]
df['F'] = x_mat[:,1]
df['G'] = x_mat[:,2]
print(x_mat)
print(df)
# # 检查数据集中是否有数据缺失
# print(np.any(df.isnull())==True)
# # 逐行检查数据集中是否有数据缺失
# print(df.isnull())
# 
# # axis=1 代表列  axis=0 代表行
# print(df.dropna(axis=1, how='any'))