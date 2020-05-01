# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x=10*np.random.random_sample(10)
y1=2*x+3
y2=4*(np.random.random_sample(10)-0.5)
y=y1+y2

# initialisation
theta0=0.
theta1=0.

def h(x):
    return x*theta1+theta0

def J(x,y,theta0,theta1):
    j=0
    m=len(x)

    for i in range(m):
        j+=(h(x[i])-y[i])**2
    return j/(2*m)

def dJtheta0(x,y,theta0,theta1):
    j=0
    m=len(x)

    for i in range(m):
        j+=2*(h(x[i])-y[i])
    return j/(2*m)

def dJtheta1(x,y,theta0,theta1):
    j=0
    m=len(x)

    for i in range(m):
        j+=2*x[i]*(h(x[i])-y[i])
    return j/(2*m)

def dJ(d,x,y,theta0,theta1):
    j=0
    m=len(x)

    for i in range(m):
        if d==0
        j+=2*x**d*(h(x[i])-y[i])
    return j/(2*m)

alpha=0.01
dJ=1.
i=0

while dJ>10**(-3):
    J1=J(x,y,theta0,theta1)
    theta0+=-alpha*dJtheta0(x,y,theta0,theta1)
    theta1+=-alpha*dJtheta1(x,y,theta0,theta1)
    J2=J(x,y,theta0,theta1)
    dJ=J1-J2
    i+=1

while dJ>10**(-3):
    J1=J(x,y,theta0,theta1)
    theta0+=-alpha*dJtheta0(x,y,theta0,theta1)
    theta1+=-alpha*dJtheta1(x,y,theta0,theta1)
    J2=J(x,y,theta0,theta1)
    dJ=J1-J2
    i+=1

plt.scatter(x,y)
plt.plot(x,h(x))
print(str(theta1)+' *x+'+str(theta0),str(i)+' itérations')

plt.show()
