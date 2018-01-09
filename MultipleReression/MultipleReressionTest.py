import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

data = pd.read_csv('MultipleLinerReression.csv') 

X = data.values[:,:2]
x = data.values[:,2:-1]
Y = data.values[:,-1]
print(X)
print(x)
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