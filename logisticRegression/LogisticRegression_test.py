'''
Created on 2018年1月11日

@author: Administrator
'''
import numpy as np

def genData(numpoints, bias, variance):
    x = np.zeros(shape=(numpoints,2))
    y = np.zeros(shape=numpoints)
    # basically a straight line
    for i in range(0, numpoints):
        # bias feature
        x[i][0]=1
        x[i][1]=i
        y[i] = (i+bias)+np.random.uniform(0,1)*variance
    return x,y

def gradientDescent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose() # transpose()矩阵转置  同.T
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta) #dot 矩阵点乘
        loss = hypothesis - y
    
        cost = np.sum(loss ** 2) / (2 * m)
        print('Iteration %d | Cost:%f' %(i, cost))
        
        gradient = np.dot(xTrans, loss)/m
        theta = theta - alpha * gradient
        
    return theta

x, y = genData(200, 10, 5)
m, n = np.shape(x)
# print(x)
# print(y)
numIterations = 100000
alpha = 0.000005
theta = np.ones(n)
theta = gradientDescent(x, y, theta, alpha, m, numIterations)
print(theta)