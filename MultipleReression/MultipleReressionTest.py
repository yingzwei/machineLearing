import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

data = pd.read_csv('MultipleLinerReression.csv') 
print(data)
X = data.values[:,:2]
x = data.values[:,2:-1]
Y = data.values[:,-1]
# x_dummy = np.zeros(,3)
print(X)
# print(x_dummy)
print(Y)

regr= linear_model.LinearRegression()
regr.fit(X, Y)
print('coefficients:')
print(regr.coef_)
print('intercept:')
print(regr.intercept_)

xPred = [100,4]
yPred = regr.predict([xPred])
print('Predicted y:')
print(yPred)
#