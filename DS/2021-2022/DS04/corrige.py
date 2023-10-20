#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:53:31 2022

@author: jg
"""

#==============================================================================
# Ligne polygonale
#==============================================================================

# Q1
LX=[1,0,-1,0,1]
LY=[0,1,0,-1,0]

# Q2 
import matplotlib.pyplot as plt
#plt.plot(LX,LY)
#plt.show()

# Q3
Longueur = 0
for i in range(len(LX)-1):
    Longueur_arc=((LX[i+1]-LX[i])**2+(LY[i+1]-LY[i])**2)**(0.5)
    Longueur=Longueur+Longueur_arc

print(Longueur)

#Q4

#fichier = open("num-points-willie.csv", "r")
fichier = open("num-points.csv", "r")

contenu=fichier.read()
fichier.close()

lignes=contenu.split('\n')

T=[]
LX=[]
LY=[]

#for i in lignes:
for i in lignes:
    i=i.split(',')
    T.append(float(i[0]))
    LX.append(float(i[1])) 
    LY.append(float(i[2]))


#Q5
i=0
while i<len(T)-1 and T[i]<T[i+1]:
    i=i+1
print(i==len(T)-1)

#Q6
Longueur = 0
for i in range(len(LX)-1):
    Longueur_arc=((LX[i+1]-LX[i])**2+(LY[i+1]-LY[i])**2)**(0.5)
    Longueur=Longueur+Longueur_arc  

print(Longueur)

#Q7
print('vitesse moyenne : ',Longueur/(T[-1]-T[0]))


#==============================================================================
# Exercice K_n, L_n
#==============================================================================

#Q1
def K(n):
    if n==0:
        return(1)
    else:
        somme=0
        for i in range(n):
            somme=somme+K(i)*K(n-1-i)
        return(somme)
    
    
#Q3
def fact(n):
    if n==0:
        return(1)
    else:
        res=1
        for i in range(1,n+1):
            res=res*i
        return(res)   

# Q4
def LK(n):
     return(1./(n+1)*fact(2*n)/fact(n)**2)
    

#Q5
#for i in range(10):
#    print(K(i)==LK(i))
    
    

#==============================================================================
# Exercice de tri    
#==============================================================================
compteur=0
def ordonner(L):
    global compteur
    compteur+=1
    if len(L)<=1 :
        return(L)
    e0=L[0]
    n=1
    Linf,Lsup=[],[]
    for ei in L[1:]:
        if ei==e0:
            n=n+1
        elif ei<e0:
            Linf.append(ei)
        else :
            Lsup.append(ei)
    return(ordonner(Linf)+n*[e0]+ordonner(Lsup))        

print(ordonner([5,3,10,7,7,2]),compteur)


# Q3
def less(L1,L2):
    return(L1[0]<L2[0] or (L1[0]==L2[0] and L1[1]<=L2[1]))

# Q4
def ordonnerDansR2(L):
    if len(L)<=1 :
        return(L)
    e0=L[0]
    n=1
    Linf,Lsup=[],[]
    for ei in L[1:]:
        if ei==e0:
            n=n+1
        elif less(ei,e0):
            Linf.append(ei)
        else :
            Lsup.append(ei)
    return(ordonnerDansR2(Linf)+n*[e0]+ordonnerDansR2(Lsup))  


# Q5
from math import pi

A=[-pi+i*pi/100 for i in range(0,201)]

# Q6
from math import cos,sin
B=[[(20+cos(10*a))*cos(a),(20+cos(10*a))*sin(a)] for a in A]

#Q7
B=ordonnerDansR2(B)

#Q8
import matplotlib.pyplot as plt


X=[]
Y=[]
for (x,y) in B:
    X.append(x)
    Y.append(y)
    
    
#plt.plot(X,Y)
#plt.axis('equal')    
#plt.show()


#==============================================================================
#  Nombres de bits
#==============================================================================

#Q1
def comptage(S):
    dico={}
    for i in S:
        if i in dico:
            dico[i]=dico[i]+1
        else:
            dico[i]=1
    return(dico)

print(comptage('aaaaggbbbzdaaa'))

#Q2        
def nbelem(S):
    return(len(comptage(S))) 

print(nbelem('aaaaggbbbzdaaa'))

#Q3
def nbits(n):
    p=1
    while 2**p<n:
        p=p+1
    return(p)    

print(nbits(5))

#Q4
def nbtotalbits(S):
    return(nbits(nbelem(S)))

print(nbtotalbits('aaaaggbbbzdaaa'))

#Q5
def coupures(S):
     liste=[]
     for i in range(1,len(S)):
         if S[i] != S[i-1]:
             liste.append(i)
     return liste

print(coupures('aaaaggbbbzdaaa'))
    
#def coupures(S):
#    coupures=[1]
#    for i in range(1,len(S)):
#        if S[i]==S[i-1]:
#            coupures[-1]=coupures[-1]+1
#        else:
#            coupures.append(1)
#    return(coupures)   
            
    
