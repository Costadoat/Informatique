#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:47:07 2019

@author: jg
"""

import matplotlib.pyplot as plt

L=range(1,7)

def sp(L):
    M=[]
    for i in range(len(L)):
        if i%2==0:
            M.append(L[-i/2-1])
        else:
            M.append(L[(i+1)/2-1])
    return(M)

print(sp(range(1,7)))
print(sp(range(1,8))) 


for i in range(6):
    L=sp(L)
print(L)  

def p(L):
    n=1
    Lorigine=L
    while sp(L)!=Lorigine:
        L=sp(L)
        n=n+1
    return(n)    
           
    

X=range(1,100)
Y=[]
for i in X:
    Y.append(p(range(0,i))/float(i))        
    
plt.plot(X,Y)  

print(Y.index(min(Y)))  