#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 08:36:51 2019

@author: shubham
"""

class LinearReg:
    def generror():
        return np.random.normal(loc=np.random.randint(50),size=n)/10


    def x_gen():
         return np.random.random(size=n)*20


    def y_gen():
        m=np.random.random()
        c=5
        return  m*x+c+error
        
    
    def derv_w(x,y,c,m,n):
        initial=y-m*x-c
        initial=np.transpose(initial)
        temp=-(initial)*x
        temp=np.sum(temp)
        return temp/n
    
    
    
    
    def derv_c(x,y,c,m,n):
        temp=-(y-m*x-c)
        temp=np.sum(temp)
        return temp/n


    def run():
        lam=0.001
        for i in range(8000):
        __m=m_new
        __c=c_new
        dcost_dm=derv_w(x,y,__c,__m,n)
        dcost_dc=derv_c(x,y,__c,__m,n)
        m_new=__m-lam*dcost_dm
        c_new=__c-lam*dcost_dc
        return c_new
        #if((np.absolute(m_ne
     