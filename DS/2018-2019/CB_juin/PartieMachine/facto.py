#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:56:18 2019

@author: jg
"""

def facto(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)    



def sommef(n):
    N=str(n)
    somme=0
    for i in range(len(N)):
        somme=somme+facto(int(N[i]))
    return(somme)    
        
   
n=0

for i in range(100000):
    if sommef(i)==i:
        print(i)