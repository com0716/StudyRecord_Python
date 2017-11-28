# --*--coding:utf-8--*--

'''
@version:python 2.7
@author:com0716
@file:MatplotlibDemo.py
@time:2017/11/28 22:07
'''

def plotDemo():
    from matplotlib import pyplot as plt

    # 支持中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 支持负号
    plt.rcParams['axes.unicode_minus'] = False

    # 开始画图
    fig = plt.figure()

    # 1行1列中的第一个
    ax = fig.add_subplot(1,1,1)

    x = [1, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5, 6]
    #ax.plot(x, y, c='red', label='y')
    ax.plot(x, y, c='red', label=u'y值')

    # 设置横轴标签、纵轴标签、图标题
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')
    ax.set_title('x-y line')
    ax.legend(fontsize=10)

    plt.show()



if __name__ == '__main__':
    plotDemo()

