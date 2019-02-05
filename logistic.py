#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 08:45:16 2019

@author: shubham
"""


import numpy as np

#logistic regression
class logistic_regrssion:
    def __init__(self,lr=0.01,iteration=10000,fit_intercept=True):
        self.lr=lr
        self.iteration=iteration
        self.fit_intercept=fit_intercept
     
    def _add_intercept(self,x):
        intercept=np.ones((x.shape[0],1))
        return np.concatenate((x,intercept),axis=1)
    
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))
    
    def loss(self,h,y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    def fit(self,x,y):
        if self.fit_intercept:
            x=self._add_intercept(x)
            
        self.theta=np.zeros(x.shape[1])
        z=np.dot(x,self.theta)
        h=self.sigmoid(z)
            
        for i in range(self.iteration):
            
            gradient=np.dot(x.T,(h-y))/len(y)
            self.theta-=self.lr*gradient
            z=np.dot(x,self.theta)
            h=self.sigmoid(z)
            
            loss=self.loss(h,y)
            
        print(loss)
        
    def predict(self,x):
        if self.fit_intercept:
            x=self._add_itercept(x)
        temp=self.sigmoid(np.dot(x,self.theta))    
        return temp.round() 
    def predit_prob(self,x):
        if self.fit_intercept:
            x=self._add_intercept(x)
            return self.sigmoid(np.dot(x,self.theta))  
