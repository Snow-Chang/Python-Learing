# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:17:10 2018

@author: 常雪峰
"""

import numpy as np
from numpy import linalg
import pylab as pl
class LinerModel():
    # 生成数据类
    def Gendata(self):
        mean = 0
        std = 5
        L = 100
        n = np.random.normal(mean,std,L)
        x0 = np.linspace(1,L,L)
        y = 1.5*x0+1
        x1 = x0+n
        return x1,y
    
    def LR(self,X,y):
        w = np.dot(X,y)/np.dot(X,X)
        b = ((y-w*X).sum())/len(X)
        return w,b

if __name__ == '__main__':
    lm = LinerModel()
    x,y = lm.Gendata()
    pl.plot(x,y,'.')
    w,b = lm.LR(x,y)
    x0 = np.linspace(1,100,100)
    pl.plot(x0,w*x0+b,'r')
    