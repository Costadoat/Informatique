# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:59:19 2017

@author: willie
"""

def algorithme(f,a,b,eps):
    while (b-a)>2*eps:
        c=(float(a)+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        print a,b
    return ((a+b)/2)

def carre(x):
    return(x**2-3)

print algorithme(carre,2,3,0.15)

