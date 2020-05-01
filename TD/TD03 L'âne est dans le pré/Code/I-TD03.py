# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:06:34 2016

@author: Renaud
"""


import numpy as np
import matplotlib.pyplot as plt

long=200
larg=200
corde=20
pre=np.zeros((long, larg),'i')

def manger(x,y):
    for i in range(long):
        for j in range(larg):
            if (i-x)**2+(j-y)**2<corde**2 and pre[i,j]!=0:
                pre[i,j]=2
            if (i-x)**2+(j-y)**2<corde**2 and pre[i,j]==0:
                pre[i,j]=1
    return pre

def analyse(pre):
    k,h=0,0    
    x1,y1,x2,y2 = [],[],[],[]
    for i in range(long):
        for j in range(larg):
            if pre[i,j] == 1:
                k=k+1
                x1.append(i)
                y1.append(j)
            if pre[i,j] == 2:
                h=h+1
                x2.append(i)
                y2.append(j)
    return x1,y1,x2,y2,k,h

def pourcent(k):
    return 100*(k)/(long*larg)

def calcul_classique(x0,y0,inc):
    x=x0
    y=y0
    while y+corde < larg:
        while x+corde < long:
            pre=manger(x,y)
            x=x+inc
        x=x0
        y=y+inc
    return pre

def calcul_quinconce(x0,y0,inc):
    u=0
    x=x0
    y=y0
    while y+corde+inc/2 < larg:
        while x+corde < long:
            u=u+1
            if (u % 2 == 0):
                pre=manger(x,y+inc/2)
            else:
                pre=manger(x,y)
            x=x+inc
        x=x0
        u=0
        y=y+inc
    return pre

pre=calcul_classique(20,20,35)
#pre=calcul_quinconce(20,20,34.9)

##########Recuperer la matrice si pas trouvee #####################
fichier = open('D:\Documents\Dorian\Prepa\Informatique\TD03\Pre.txt','w')

for i in range(long):
    for j in range(larg):
        fichier.write('%s,%s,%s\n' % (i,j,pre[i,j]))
fichier.close()

fichier = open('D:\Documents\Dorian\Prepa\Informatique\TD03\Pre.txt','r')

for ligne in fichier: # on lit ligne par ligne
    liste=ligne.split(',')
    i,j=liste[0],liste[1]
    pre[i,j]=liste[2]

fichier.close() 
####################################################################

x1,y1,x2,y2,k,h=analyse(pre)
print'Surface couverte %s %%' % pourcent(k+h)
print'Surface couverte 2 fois %s %%' % pourcent(h)

plt.scatter(x1,y1,s=1,color='green')
plt.scatter(x2,y2,s=1,color='red')
plt.axis('equal')
plt.xlim(0, long)
plt.ylim(0, larg)
plt.show()