# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 17:22:31 2018

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt

dx,dy=0.1,0.1
x,y,i=0,0,0
xt1,yt1,rt1,xt2,yt2=[],[],[],[],[]
k=3
xmin,xmax,ymin,ymax=0,0,0,0

def nb_diviseurs(n):
    i=0
    if n<5:
        if n in (2,3):
            return 0
        else:
            return 1
    # si n est pair et >2 (=2: cas traité ci-dessus), il ne peut pas être premier
    if n & 1 == 0:
        return 0
    # autres cas
    p=3
    r=np.sqrt(n)
    while p<=r:
        if n % p == 0:
            i+=1
        p+=2
    return i

while xmax<7:
    while x<=xmax:
        x+=dx
        i+=1
        r=nb_diviseurs(i)
        if r!=0:
            xt1.append(x)
            yt1.append(y)
            rt1.append(r*k)
        else:
            xt2.append(x)
            yt2.append(y)
    xmax=x
    while y<=ymax:
        y+=dy
        i+=1
        r=nb_diviseurs(i)
        if r!=0:
            xt1.append(x)
            yt1.append(y)
            rt1.append(r*k)
        else:
            xt2.append(x)
            yt2.append(y)
    ymax=y
    while x>=xmin:
        x+=-dx
        i+=1
        r=nb_diviseurs(i)
        if r!=0:
            xt1.append(x)
            yt1.append(y)
            rt1.append(r*k)
        else:
            xt2.append(x)
            yt2.append(y)
    xmin=x
    while y>=ymin:
        y+=-dy
        i+=1
        r=nb_diviseurs(i)
        if r!=0:
            xt1.append(x)
            yt1.append(y)
            rt1.append(r*k)
        else:
            xt2.append(x)
            yt2.append(y)
    ymin=y

print('Nombre max: '+str(i))

plt.figure(1)
plt.scatter(xt2,yt2,s=15)
plt.axis('equal')
plt.figure(2)
plt.scatter(xt1,yt1,s=rt1)
plt.axis('equal')
        