#!coding:UTF-8
'''
Created on 2018年2月26日

@author: m1834
'''
from Bezier.bezier.coefficient import Bersizer

import matplotlib.pyplot as plt
import numpy as np

def BersizerMatrix(n):
    res = []
    for i in range(n+1):
        _,y = Bersizer(i, n)
        res.append(y)
    return res

def convertBMToArr(bm):
    return np.array(bm)

def calCurvePoint(x,y,n):
    bm = BersizerMatrix(n)
    BM = convertBMToArr(bm)
    
    px = convertBMToArr(x)
    py = convertBMToArr(y)
    
    resx = np.dot(px,BM)
    resy = np.dot(py,BM)
    return (resx,resy)

def drawBesizeCurve(x,y,controlPoints =None, controlPoint = False,controlLine = False):
    px = py = 0
    if controlPoints:
        px,py = controlPoints
    if controlPoints and controlPoint:
        plt.scatter(px, py)
    if controlPoints and controlLine:
        plt.plot(px,py)
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    x = [1,10,15]
    y = [2,20,15]
    n = 2
    resx,resy = calCurvePoint(x, y, n)
    drawBesizeCurve(resx,resy,(x,y),True,True)