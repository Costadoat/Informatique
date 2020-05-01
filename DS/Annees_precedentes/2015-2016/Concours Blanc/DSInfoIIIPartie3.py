# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 18:07:04 2014

@author: willie
"""

from math import exp

# Definition de la fonction
def f(x):
    return x**3+2*x**2+3*x-4

def g(x):
    return x**3+2*x**2+3*x-6


def dicho(fonction, a, b, eps):
    #global m
    u=min(a,b)
    v=max(a,b)
    i=0
    while(v-u) > eps and i < 1:
        i=i+1
        m=(u+v)/2
        if fonction(u)*fonction(m)<0:
            v=m
        else:
            u=m
#        print u,v
    return m
#
a=0.5
b=1.4

eps=0.00001

appel=input()

m=dicho(appel,a,b,eps)
print appel(m)

# la procedure dicho a retourne m
print('resultat dichotomie : '+str(m))