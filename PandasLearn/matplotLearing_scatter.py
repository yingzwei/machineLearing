import matplotlib.pyplot as plt
import numpy as np

n = 5
X = np.arange(n)
# uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内。
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# print(Y1)
# print(X)

plt.bar(X, Y1, facecolor='red', edgecolor='white', alpha=.7)
plt.bar(X, Y2, facecolor='green', edgecolor='white', alpha=.7)

for x, y in zip(X, Y1):
    plt.text(x + 0.1, y + 0.2, 'x%s:%.1f' % (n, y), ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.1, y + 0.3, 'z%s:%.1f' % (n, y), ha='center', va='bottom')

plt.show()
