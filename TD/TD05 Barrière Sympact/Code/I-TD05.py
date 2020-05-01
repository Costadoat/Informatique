# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Renaud.
"""

import numpy as np
import matplotlib.pyplot as plt

l1=0.17
m1=2.8
l2=1.
m2=1.
g=9.81
Jeq=m1*l1**2+m2*l2**2
K=0.45
theta0=np.pi/2.
Cf=4

def F(y,t):
    mP=(l1*m1+(l1+l2)*m2)*g*np.cos(y[1])
    yl=(K*(180/np.pi)*(-y[1]+theta0)-mP-Cf*y[0])/Jeq,y[0]
    return yl

def euler(F,y0,t):
    N = len(t)
    y=np.zeros((len(t),2))
    y[:0] = y0
    for i in range(N-1):
        dt=(t[i+1]-t[i])
        s = [j*dt for j in F(y[i],t[i])]
        y[i+1] = y[i]+s
    return y

	
t = np.linspace(0,5,100)	
y = euler(F,[0,0],t)
y1 = (180/np.pi)*y[:,1]
plt.plot(t,y1,label='Euler')
plt.legend(loc='upper left')
plt.show()