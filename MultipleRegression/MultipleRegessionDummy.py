'''
Created on 2018骞�1鏈�9鏃�

@author: Administrator
'''
import numpy as np
import pandas as pd
from sklearn import linear_model

data = pd.read_csv('MultipleLinerRegression.csv') 
#print(data)

x_category = data.values[:,2:-1]
x_dummy = []
# print(x_category)
for row in x_category:
    emp = [0,0,0]
    if row==0:
        emp[0]=1
    if row==1:
        emp[1]=1
    if row==2:
        emp[2]=1
    x_dummy.append(emp)

dummy_x = np.mat(x_dummy)
data['car'] = dummy_x[:,0]
data['suv'] = dummy_x[:,1]
data['svm'] = dummy_x[:,1]
# 鍒犻櫎'category'鍒楀悕鐨勬暟鎹�
#data.drop('category', axis=1, inplace=True)
X = data.iloc[:,[0,1,4,5,6]]
Y = data.iloc[:,3]
# print(Y)
# print(X)
regr= linear_model.LinearRegression()
regr.fit(X, Y)
# print('coefficients:')
# print(regr.coef_)
# print('intercept:')
# print(regr.intercept_)

xPred = [100,4,0,1,0]
yPred = regr.predict([xPred])
print('预测所需时间为:')
print(yPred)
#