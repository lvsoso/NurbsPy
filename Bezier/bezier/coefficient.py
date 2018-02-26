#!coding:UTF-8
'''
Created on 2018年2月25日

@author: m1834
'''

from Bezier.curve_math.factoral import factoral,power
from Bezier import *
import matplotlib.pyplot as plt
import numpy as np

# # 简单的绘图
# x = np.linspace(0, 2 * np.pi, 50)
# plt.plot(x, np.sin(x)) # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
# plt.show() # 显示图形

def bersizer(i,n,u):
    c1 = factoral(n)
    c2 = factoral(i)
    c3 = factoral(n-i)
    c = c1/(c2*c3)
    u1 = power(u, i)
    u2 = power(1-u, n-i)
    return c*u1*u2

def Bersizer(i,n):
    x = np.linspace(STARTU, ENDU, GLOBALOFFSETNUM)
    y = [bersizer(i, n, u) for u in x]
    return (x,y)

def bersizerDerivative(i,n,u):
    firstNum = 0
    secondNum = 0
    if i != 0:
        firstNum = bersizer(i-1, n-1, u)
    if i != n:
        secondNum = bersizer(i, n-1, u)
    return n*(firstNum - secondNum) 

def BersizerDerivative(i,n):
    x = np.linspace(STARTU, ENDU, GLOBALOFFSETNUM)
    y = [bersizerDerivative(i, n, u) for u in x]
    return (x,y)

def drawBersizer(i,n):
    x,y = Bersizer(i, n)
    plt.plot(x, y) 
    plt.show()
    
def drawOnOneFig(n):
    res = []
    for i in range(n+1):
        x,y = Bersizer(i, n)
        res.append(x)
        res.append(y)
    plt.plot(*res)
    plt.show()

def drawBersizerDerivative(i,n):
    x,y = BersizerDerivative(i, n)
    plt.plot(x, y) 
    plt.show()
    
def drawBersizerDerivativeOnOneFig(n):
    res = []
    for i in range(n+1):
        x,y = BersizerDerivative(i, n)
        res.append(x)
        res.append(y)
    plt.plot(*res)
    plt.show()

if __name__ == "__main__":
    drawOnOneFig(10)
    drawBersizerDerivativeOnOneFig(3)