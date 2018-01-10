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
#print(res)

left_Kes_df =  pd.DataFrame({'key1':['K0','K0','K1','K2'],
                             'key2':['K0','K1','K0','K1'],
                             'A':['A0','A1','A2','A3'],
                             'B':['B0','B1','B2','B3']})
right_Kes_df =  pd.DataFrame({'key1':['K0','K1','K1','K2'],
                              'key2':['K0','K0','K0','K3'],
                              'C':['C0','C1','C2','C3'],
                              'D':['D0','D1','D2','D3']})
# how= inner,outer,left,right
res_Kes = pd.merge(left_Kes_df,right_Kes_df, on=['key1','key2'], how='outer')
#print(res_Kes)

# 根据索引index 进行数据合并
left_index_df =  pd.DataFrame({'A':['A0','A1','A2','A3'],
                             'B':['B0','B1','B2','B3']},
                             index=['K0','K1','K1','K2'])
right_index_df =  pd.DataFrame({'B':['C0','C1','C2','C3'],
                              'C':['D0','D1','D2','D3']},
                              index=['K0','K1','K1','K2'])
res_index = pd.merge(left_index_df, right_index_df, how='outer', left_index=True, right_index=True)
print(res_index)



