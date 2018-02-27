#!coding:UTF-8
'''
Created on 2018年2月27日

@author: m1834
'''

import numpy as np  
import matplotlib.pyplot as plt  
import mpl_toolkits.mplot3d
from Bezier import *
from Bezier.curve_math.factoral import power
# x,y=np.mgrid[-2:2:20j,-2:2:20j]  
# z=x*np.exp(-x**2-y**2)  
#   
# ax=plt.subplot(111,projection='3d')  
# ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)  
# ax.set_xlabel('x')  
# ax.set_ylabel('y')  
# ax.set_zlabel('z')  
#   
# plt.show()  

def unitCircle():
    u = np.linspace(0,1,GLOBALOFFSETNUM)
    px = [(1 - power(ui, 2))/(1 + pow(ui, 2)) for ui in u]
    py = [2*ui/(1 + pow(ui, 2)) for ui in u]
    return (px,py)

def drawUnitCircle():
    x,y = unitCircle()
    plt.plot(x,y)
    plt.show()
    
if __name__ == "__main__":
    drawUnitCircle()