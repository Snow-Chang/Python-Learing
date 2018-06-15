# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 18:57:59 2018

@author: 常雪峰
"""

import numpy as np
from numpy import linalg
import cvxopt
import pylab as pl

# 实现生成数据的类
class GenData():
    def lin_data(self):
        '''
        生成线性SVM的数据：两组标记为1和-1的数据为长为L
        协方差矩阵为cov，均值为mean1的二维高斯分布
        '''
        mean1 = np.array([0, 2])
        mean2 = np.array([2, 0])
        cov = [[0.8,0.6],[0.6,0.8]]
        X1 = np.random.multivariate_normal(mean1,cov,100)
        y1 = np.ones(100)
        X2 = np.random.multivariate_normal(mean2,cov,100)
        y2 = np.ones(100)*(-1)
        return X1,y1,X2,y2
    
    def nlin_data(self):
        mean1 = [-1, 2]
        mean2 = [1, -1]
        mean3 = [4, -4]
        mean4 = [-4, 4]
        cov = [[1.0,0.8], [0.8, 1.0]]
        X1 = np.random.multivariate_normal(mean1, cov, 50)
        X1 = np.vstack((X1, np.random.multivariate_normal(mean3, cov, 50)))
        y1 = np.ones(len(X1))
        X2 = np.random.multivariate_normal(mean2, cov, 50)
        X2 = np.vstack((X2, np.random.multivariate_normal(mean4, cov, 50)))
        y2 = np.ones(len(X2)) * -1
        return X1, y1, X2, y2

    def lin_overlap_data(self):
        # generate training data in the 2-d case
        mean1 = np.array([0, 2])
        mean2 = np.array([2, 0])
        cov = np.array([[1.5, 1.0], [1.0, 1.5]])
        X1 = np.random.multivariate_normal(mean1, cov, 100)
        y1 = np.ones(len(X1))
        X2 = np.random.multivariate_normal(mean2, cov, 100)
        y2 = np.ones(len(X2)) * -1
        return X1, y1, X2, y2

# 实现SVM算法的类
class SVM(X,y,kernel_type='liner',p=3,C=None):
    '''
    
    '''
    def __init__(self,X,y,kernel_type='liner',p=3,C=None):
        self.X = X
        self.y = y
        self.kernel_type = kernel_type
        self.p = p
        self.C = C
        if self.C is not None: self.C = float(self.C) 
    
    def kernelGen(self):
        if self.kernel_type is 'liner':
            return np.dot(self.X,self.y)
        elif self.kernel_type is 'polynomial':
            return (1 + np.dot(self.X, self.y)) ** self.p
        else :
            return np.exp(-linalg.norm(self.X-self.y)**2 / (2 * (self.p ** 2)))
        
    def 