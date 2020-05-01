# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt

print(np.pi)

print(np.array([1,2,3,4,5,6]))

print(np.array([1,2,3,4,5,6],'d'))

print(np.array([1,2,3,4,5,6],'D'))

print(np.array([[0,1],[1,0]],'d'))

print(np.zeros((3,3),'d'))

print(np.identity(4,'d'))

print(0.125*np.identity(3,'d'))

print(np.identity(2,'d') + np.array([[1,1],[1,2]]))

print(np.dot(np.identity(2),np.ones((2,2))))

v = np.array([3,4],'d')

print(np.sqrt(np.dot(v,v)))

a=np.array([1,2,3])
b=np.array([3,2,1])
print(np.multiply(a,b))

m = np.array([[1,2],[3,4]])

print(m.T)

print(np.linspace(0,1,20))

x = np.linspace(0,2*np.pi)
plt.plot(x,np.cos(x))


A = np.array([[1,1,1],[0,2,5],[2,5,-1]])
b = np.array([6,-4,27])
print(np.linalg.solve(A,b))

A = np.array([[13,-4],[-4,7]],'d')
print(np.linalg.eigvalsh(A))

print(np.linalg.eigh(A))

t0,t1,t2,t3=0,2,6,8
i=100
k=10

x1=np.linspace(t0,t1-(t1-t0)/i,i)
x2=np.linspace(t1,t2-(t2-t1)/i,i)
x3=np.linspace(t2,t3-(t3-t2)/i,i)

yyy1=k*np.ones(i)
yyy2=0*np.ones(i)
yyy3=-k*np.ones(i)
yyy=np.concatenate((yyy1,yyy2,yyy3))

yy1=k*x1
yy2=k*x1[i-1]*np.ones(i)
yy3=-k*(x3-x2[i-1])+yy2
yy=np.concatenate((yy1,yy2,yy3))

y1=k*np.multiply(x1,x1)/2
y2=y1[i-1]+(x2-x1[i-1])*yy2
y3=y2[i-1]-k*np.multiply(x3-x2[i-1],x3-x2[i-1])/2+np.multiply(yy2,x3-x2[i-1])

y=np.concatenate((y1,y2,y3))

x=np.concatenate((x1,x2,x3))
plt.plot(x,yyy)
plt.plot(x,yy)
plt.plot(x,y)