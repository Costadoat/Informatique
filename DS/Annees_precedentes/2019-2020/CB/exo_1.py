#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:00:56 2020

@author: jg
"""

import matplotlib.pyplot as plt
import numpy as np


#Q1
def Suite(n,u0):
    U=[u0]
    u=u0
    for i in range(n-1):
        if u%2==0:
            u=u/2
        else:
            u=3*u+1
        U.append(u)
    return(U)  


plt.plot(range(50),Suite(50,18),'.')


#Q3
def vol(u0):
    u=u0
    n=0
    while u!=1:
        n=n+1
        if u%2==0:
            u=u/2
        else:
            u=3*u+1
    return(n)        
        
print(vol(18))

#Q4
N=1000
Vol=[]
for i in range(1,N+1):
        Vol.append(vol(i))


plt.plot(range(1,N+1),Vol(N),'.')

#Q5
plt.hist(Vol(N))
