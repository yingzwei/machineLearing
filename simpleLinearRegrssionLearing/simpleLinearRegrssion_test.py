import numpy as np

def fitSLR(x,y):
    n = len(x)
    # 分子
    dinominator = 0
    # 分母
    numerator = 0
    for i in range(0,n):
        numerator +=(x[i] - np.mean(x))*(y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x))**2
    b1 = numerator/float(dinominator)  # 求斜率
    b0 = np.mean(y)/float(np.mean(x))  # 求截距
    return b0,b1

def predict(x,b0,b1):
    return b0+ x*b1

x=[1,3,2,1,3]
y=[14,24,18,17,27]

b0,b1 = fitSLR(x, y)

print('intercept—截距:%.2f, slope-斜率:%.2f' %(b0, b1))


x_test = 6
y_test = predict(x_test, b0, b1)

print('y_test:%.2f' % y_test)