# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import scipy.optimize as resol
import scipy.integrate as integr
import matplotlib.pyplot as plt

def f(x):
	return x**2 - 3

print(resol.fsolve(f, -1.))
print(resol.fsolve(f, 1.))

def f(v): 
	return v[0]**2-v[1]**2-2, 2*v[0]-v[1]-3
	
sol=resol.root(f,[0,0])
print(sol.success)
print(sol.x)

sol=resol.root(f,[3,3])
print(sol.success)
print(sol.x)

def f(x) :
	return np.exp(-x)

x=np.linspace(0.001,10,21)
plt.plot(x,f(x))
plt.show()

print(integr.quad(f, 1, 3))
print(integr.quad(f, 0, np.inf))

E=5
R=200
C=50*10**(-6)
def f(u, t) :
	return E-u/(R*C)
 
T=np.arange(0,0.2,0.001)
X= integr.odeint(f,0,T)
#print(X)
plt.plot(T,X)
plt.show()


def f(x, t) :
    return np.array([-t*x[0], x[0]+0.2*x[1]])
    
T = np.arange(0, 5.01, 0.01)
X = integr.odeint(f, np.array([2.,1.]), T)
#print(X)
plt.plot(X[ :,0], X[ :,1])
plt.show()

a = 6 + 2j
b = 9 - 1j
print(a*b)
print(a.real)
print(a.imag)
print(abs(a))
