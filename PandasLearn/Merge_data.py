'''
Created on 2018年1月10日

@author: Administrator
'''
import pandas as pd

left_df =  pd.DataFrame({'key':['K0','K1','K2','K3'],
                         'A':['A0','A1','A2','A3'],
                         'B':['B0','B1','B2','B3']})
right_df =  pd.DataFrame({'key':['K0','K1','K2','K3'],
                         'C':['C0','C1','C2','C3'],
                         'D':['D0','D1','D2','D3']})
# print(left_df)
# print(right_df)
res = pd.merge(left_df,right_df,on='key')
print(res)