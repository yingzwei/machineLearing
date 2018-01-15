# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.xlim(-2, 2)
plt.ylim(-3, 3)
# 添加坐标标签名
# plt.xlabel(r'x axis')
# plt.ylabel(r'y axis')
# 更改plt显示坐标
new_ticks = np.linspace(-2, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-3, -1, 1, 2, 3]
           , [r'$real\ bad$', r'$bad$', r'$\alpha$', r'$good$'r'$real\ good$'])

# 获取当前坐标轴 gca = get current axis
ax = plt.gca()
# 将上、有边框隐藏
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 位移左、下边框
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

plt.plot(x, y1, label='qu xian')
plt.plot(x, y2, color='red', linestyle='--', linewidth=1.0, label='xie xian')
# 添加曲线名称注释

plt.legend()

# 添加点注释
# x0 = 0.7
# y0 = 2 * x0 + 1
# plt.scatter(x0, y0, color='green')
# plt.plot([x0, x0], [y0, 0], lw=1.0, color='green', ls='--')
#
# plt.annotate(r'$2*x=%s$' % y0, xy=[x0, y0], xycoords='data', xytext=[20, -20], textcoords='offset points', fontsize=14,
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='green'))

plt.show()
