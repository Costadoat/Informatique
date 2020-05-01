#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:03:39 2019

@author: jg
"""

Lp=[1,1,7]
x0=0

def evalu(Lp,x0):
    deg=len(Lp)-1
    s=0
    for i in range(deg+1):
        s=s+Lp[i]*x0**i
    return(s) 


def evalu2(Lp,x0):
    deg=len(Lp)-1
    s=0
    x=1
    for i in range(deg+1):
        s=s+Lp[i]*x
        x=x*x0
    return(s)    

def evalu3(Lp,x0):
    deg=len(Lp)-1
    s=Lp[deg]
    for i in range(1,deg+1):
        s=x0*s+Lp[deg-i]
    return(s)   

print(evalu(Lp,x0))
print(evalu2(Lp,x0))
print(evalu3(Lp,x0))