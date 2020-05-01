# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x=np.sort(10*np.random.random_sample(10))
y1=2*x**3+2*x**2+2*x+2000
y2=10000*(np.random.random_sample(10)-0.5)
y=y1+y2

n=4
# initialisation
theta=np.zeros(n)
theta_temp=np.zeros(n)

def h(x,theta):
    h=0
    for i in range(len(theta)):
        h+=theta[i]*x**i
    return h

def J(x,y,theta):
    j=0
    m=len(x)

    for i in range(m):
        j+=(h(x[i],theta)-y[i])**2
    return j/(2*m)

def dJ(d,x,y,theta):
    j=0
    m=len(x)

    for i in range(m):
        j+=2*x[i]**d*(h(x[i],theta)-y[i])
    return j/(2*m)

deltaJ=100.
iterations=0
alpha0=10**-6
alpha=alpha0

while np.abs(deltaJ)>10:
    J1=J(x,y,theta)
    for i in range(n):
        theta_temp[i]+=-alpha*dJ(i,x,y,theta)
    theta[:]=theta_temp[:]
    J2=J(x,y,theta)
    deltaJ=J1-J2
    alpha=np.abs(deltaJ)/10**5.
    if alpha>alpha0:
        alpha=alpha0
    print(np.abs(deltaJ),alpha)
    iterations+=1

plt.scatter(x,y)
x=np.linspace(0,10,1000)
plt.plot(x,h(x,theta))
print(theta,iterations,deltaJ)

plt.show()
