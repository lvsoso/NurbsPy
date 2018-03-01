#!coding:UTF-8
'''
Created on 2018年2月28日

@author: m1834
'''

from Bezier import *
from Bezier.bezier.coefficient import Bersizer
import numpy as np
from Bezier.curve_math.matrix import convertBMToArr
import matplotlib.pyplot as plt

def BesizerMatrix(n):
    BM = []
    for i in range(n+1):
        _,y = Bersizer(i, n)
        BM.append(y)
    return BM
 
def calWeightMatrix(n,w):
    BM = BesizerMatrix(n)
    BM = convertBMToArr(BM)
    WM = convertBMToArr(w)
    weightMatrix = np.dot(WM,BM)
    return weightMatrix
 
def rationalBesizer(i, n, w):
    u = np.linspace(STARTU, ENDU, GLOBALOFFSETNUM)
    _,y = Bersizer(i, n)
    WM = calWeightMatrix(n, w)
    ru = []
    for idx in range(len(y)):
        molecular = w[i]*y[idx]
        denominator = WM[idx]
        ru.append(molecular/denominator)
    return (u,ru)
 
def rationalBesizerMatrix(n,w):
    res = []
    for i in range(n+1):
        _, ru = rationalBesizer(i, n, w)
        res.append(ru)
    return np.array(res)
 
def drawRationalBesizer(i, n, w):
    u, ru = rationalBesizer(i, n, w)
    plt.plot(u, ru)
    plt.show()
    
def drawRationalBesizerOnOneFig(n,w):
    res = []
    for i in range(n+1):
        u, ru = rationalBesizer(i, n, w)
        res.append(u)
        res.append(ru)
    plt.plot(*res)
    plt.show()

def RationalBesizerCurvePoint(n,w,x,y):
    RBM = rationalBesizerMatrix(n,w)
    mx = np.array(x)
    my = np.array(y)
    px = np.dot(mx,RBM)
    py = np.dot(my,RBM)
    return (px,py)

def drawRationalBesizerCurve(n,w,x,y):
    x,y = RationalBesizerCurvePoint(n, w, x, y)
    plt.plot(x,y)
    plt.show()
    
def drawUnitCicle(n = 2, w = [1,1,2],x = [1,1,0],y = [0,1,1]):
    x,y = RationalBesizerCurvePoint(n, w, x, y)
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    w = [1,3,7,1]
#     drawRationalBesizerOnOneFig(3, w)
    x = [0,2,12,15]
    y = [0,15,15,0]
    drawRationalBesizerCurve(3, w, x, y)
    drawUnitCicle()