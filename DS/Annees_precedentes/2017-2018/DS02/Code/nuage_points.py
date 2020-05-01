# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 13:57:44 2017

@author: costa
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rd

fichier1=open('liste_coordonnees.csv','w')

nc=200
nd=200
ns=30
R=100
r1=10
r2=20
r3=15
a=0.5
b=-150
x0=150
xc=4
coord=[]

for i in range(nc):
    coord.append([R*np.cos(i*2*np.pi/nc)+r1*(rd.random()-0.5),R*np.sin(i*2*np.pi/nc)+r1*(rd.random()-0.5)])

for i in range(nd):
    xx=i+0
    coord.append([xx+r2*(rd.random()-0.5),a*xx+b+r2*(rd.random()-0.5)])

for i in range(ns):
    xx=0+x0
    yy=xc*i
    coord.append([xx+r3*(rd.random()-0.5),yy+r3*(rd.random()-0.5)])
    xx=xc*i+x0
    yy=0
    coord.append([xx+r3*(rd.random()-0.5),yy+r3*(rd.random()-0.5)])
    xx=xc*i+x0
    yy=xc*ns
    coord.append([xx+r3*(rd.random()-0.5),yy+r3*(rd.random()-0.5)])
    xx=xc*ns+x0
    yy=xc*i
    coord.append([xx+r3*(rd.random()-0.5),yy+r3*(rd.random()-0.5)])
    
plt.axis('equal')

coord.sort()

for i in range(len(coord)):
    fichier1.write(str(coord[i][0])+';'+str(coord[i][1])+'\n')
    plt.scatter(coord[i][0],coord[i][1],marker='x')

fichier1.close()