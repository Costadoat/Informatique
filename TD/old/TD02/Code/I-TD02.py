# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.07*x**3-x**2+6*x-1
def df(x):
    return 3*x*2-4*x+6
a=10
p=10**(-6)

def methode_Newton(f,df,a,p) :
    x0=a
    i=1
    e=1.
    while abs(e)>p :
        x1=x0-f(x0)/df(x0)
        e=x1-x0
        #plt.plot(x,df(x0)*(x-x0)+f(x0))
        x0=x1
        i=i+1
    return x1,1

def methode_dichotomie(f,p,b):
    a=0
    i=1
    while (b-a)>p :
        if f(a)*f((a+b)/2)<=0:
            a, b=a, (a+b)/2.
        else:
            a, b=(a+b)/2., b
        i=i+1
    return a,1
    
print(methode_Newton(f,df,a,p))
print(methode_dichotomie(f,p,a))
    
def racine_carree(a):
    
    def f(x):
        return x*x-a
    def df(x):
        return 2*x
        
    return methode_Newton(f,df,0.1,10**(-6))

print(racine_carree(16))