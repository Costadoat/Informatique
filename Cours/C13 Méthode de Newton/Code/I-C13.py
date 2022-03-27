# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return -2*np.cos(x/5)+2.1

def df1(x):
    return 2/5.*np.sin(x/5)

def f2(x):
    return 0.05*x+0.8

def df2(x):
    return 0.05

def f(x):
    return f1(x)-f2(x)
    
def df(x):
    return df1(x)-df2(x)
    
x=np.linspace(0,10,100)
#plt.plot(x,f1(x))
#plt.plot(x,f2(x))
#plt.plot(x,f(x))
#plt.plot(x,x-x)

def methode_Newton(f,df,a,p) :
    x0=a
    i=1
    e=1.
    while abs(f(x0))>p :
        x1=x0-f(x0)/df(x0)
        e=x1-x0
        #plt.plot(x,df(x0)*(x-x0)+f(x0))
        x0=x1
        i=i+1
    return x1,i

def methode_dichotomie(f,p,b):
    a=0
    i=1
    while (b-a)>p :
        if f(a)*f((a+b)/2)<=0:
            a, b=a, (a+b)/2.
        else:
            a, b=(a+b)/2., b
        i=i+1
        e=b-a
    return a,i

a=10.
p=10**(-6)
print(methode_Newton(f,df,a,p))
print(methode_dichotomie(f,p,a))