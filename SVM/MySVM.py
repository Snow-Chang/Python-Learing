# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:50:45 2018

@author: 常雪峰
"""
import numpy as np
from numpy import linalg
import cvxopt
import cvxopt.solvers
import pylab as pl
# 首先实现生成数据的类
class GenData(object):
    def liner_data(self):
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
    
    def gen_non_lin_separable_data(self):
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

    def gen_lin_separable_overlap_data(self):
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
class SVM(object):
              
    def kernelGen(self,x,y,kernel_type = 'liner',p=3):
        if kernel_type is 'liner':
            return np.dot(x,y)
        elif kernel_type is 'polynomial':
            return (1 + np.dot(x, y)) ** p
        else :
            return np.exp(-linalg.norm(x-y)**2 / (2 * (p ** 2)))
    
    def fit(self,X,y,kernel_type = 'liner',p=3):
        row,col = np.shape(X)
        K = np.zeros([row,row])
        for i in range (row):
            for j in range(row):
                K[i,j] = self.kernelGen(X[i],X[j],kernel_type,p)
        
        P = cvxopt.matrix(np.outer(y,y)*K)
        q = cvxopt.matrix(np.ones(row)*-1)
        A = cvxopt.matrix(y,(1,row))
        b = cvxopt.matrix(0.0)
        G = cvxopt.matrix(np.diag(np.ones(row) * -1))
        h = cvxopt.matrix(np.zeros(row))
        solution = cvxopt.solvers.qp(P, q, G, h, A, b)
        alafa = np.ravel(solution['x'])
        sv = alafa>1e-5
        index = np.arange(row)[sv]
        self.alafa = alafa[sv]
        self.sv_x = X[sv]  # sv's data
        self.sv_y = y[sv]  # sv's labels
        print("%d support vectors out of %d points" % (len(self.alafa), row))
        
        self.b = 0
        for n in range(len(self.alafa)):
            self.b += self.sv_y[n]
            self.b -= np.sum(self.alafa * self.sv_y * K[index[n],sv])
        self.b /= len(self.alafa)
        
    def project(self,X,kernel_type='liner',p=3):
        y_predict = np.zeros(len(X))
        for i in range(len(X)):
            s = 0
            for alafa, sv_y, sv_x in zip(self.alafa, self.sv_y, self.sv_x):
                s += alafa * sv_y * self.kernelGen(X[i],sv_x,kernel_type,p)
            y_predict[i] = s
        return y_predict + self.b
        
    def predict(self,X,kernel_type,p):
        return np.sign(self.project(X,kernel_type,p))
    
class TestAndTrain(object):
    
    def split_train(self,X1, y1, X2, y2):
        X1_train = X1[:90]
        y1_train = y1[:90]
        X2_train = X2[:90]
        y2_train = y2[:90]
        X_train = np.vstack((X1_train, X2_train))
        y_train = np.hstack((y1_train, y2_train))
        return X_train, y_train

    def split_test(self,X1, y1, X2, y2):
        X1_test = X1[90:]
        y1_test = y1[90:]
        X2_test = X2[90:]
        y2_test = y2[90:]
        X_test = np.vstack((X1_test, X2_test))
        y_test = np.hstack((y1_test, y2_test))
        return X_test, y_test
    
    def plot_contour(self,X1_train, X2_train, clf):
        # 作training sample数据点的图
        pl.plot(X1_train[:,0], X1_train[:,1], "ro")
        pl.plot(X2_train[:,0], X2_train[:,1], "bo")
        # 做support vectors 的图
        pl.scatter(clf.sv_x[:,0], clf.sv_x[:,1], s=100, c="g")
        X1, X2 = np.meshgrid(np.linspace(-6,6,50), np.linspace(-6,6,50))
        X = np.array([[x1, x2] for x1, x2 in zip(np.ravel(X1), np.ravel(X2))])
        Z = clf.project(X).reshape(X1.shape)
        # pl.contour做等值线图
        pl.contour(X1, X2, Z, [0.0], colors='k', linewidths=1, origin='lower')
        pl.contour(X1, X2, Z + 1, [0.0], colors='grey', linewidths=1, origin='lower')
        pl.contour(X1, X2, Z - 1, [0.0], colors='grey', linewidths=1, origin='lower')

        pl.axis("tight")
        pl.show()
        
    def trainSVM (self,X_train,y_train,X_test,y_test,kernel_type = 'liner',p=3):
        clf = SVM()
        clf.fit(X_train, y_train,kernel_type,p)
        y_predict = clf.predict(X_test,kernel_type,p)
        correct = np.sum(y_predict == y_test)
        print("%d out of %d predictions correct" % (correct, len(y_predict)))

        self.plot_contour(X_train[y_train==1], X_train[y_train==-1], clf)
    
        
if __name__ == "__main__":
    
    def liner_test():
        gen = GenData()
        tt = TestAndTrain()
        X1, y1, X2, y2 = gen.liner_data()
        X_train, y_train = tt.split_train(X1, y1, X2, y2)
        X_test, y_test = tt.split_test(X1, y1, X2, y2)
        tt.trainSVM(X_train,y_train,X_test,y_test,'liner')
        
    def soft_test():
        gen = GenData()
        tt = TestAndTrain()
        X1, y1, X2, y2 = gen.gen_lin_separable_overlap_data()
        X_train, y_train = tt.split_train(X1, y1, X2, y2)
        X_test, y_test = tt.split_test(X1, y1, X2, y2)
        tt.trainSVM(X_train,y_train,X_test,y_test,'polynomial')
        
        
    def nonliner_test():
        gen = GenData()
        tt = TestAndTrain()
        X1, y1, X2, y2 = gen.gen_non_lin_separable_data()
        X_train, y_train = tt.split_train(X1, y1, X2, y2)
        X_test, y_test = tt.split_test(X1, y1, X2, y2)
        tt.trainSVM(X_train,y_train,X_test,y_test,'gaussion',5)
        
    nonliner_test()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        