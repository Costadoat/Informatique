# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import matplotlib.pyplot as plt

e=6
R=300
C=10*10**(-3)

def F(y,t):
    return y #Cauchy
    #return (e-y)/(R*C) #Condensateur


def euler(F,y0,t):
    N = len(t)
    y = [0]*N
    y[0] = y0
    for i in range(N-1):
        y[i+1] = y[i]+(t[i+1]-t[i])*F(y[i],t[i])
    return y

t = np.linspace(0,5,50)
y = euler(F,1,t)
z = np.exp(t)
plt.plot(t,y,label='Euler')
plt.plot(t,z,label='exp(t)')
plt.legend(loc='upper left')
plt.show()
