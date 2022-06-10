#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:25:19 2022

@author: jg
"""

#==============================================================================
# Exercice 1
#==============================================================================

# Question 1

LX=[1,0,-1,0,1]
LY=[0,1,0,-1,0]

# Question 4

fichier = open("/home/eleve/Ressources/PTSI/num-points.csv", "r")

contenu=fichier.read()
fichier.close()

lignes=contenu.split('\n')

T=[]
LX=[]
LY=[]

for i in lignes:
    i=i.split(',')
    T.append(float(i[0]))
    LX.append(float(i[1])) 
    LY.append(float(i[2]))


#==============================================================================
# Exercice 2
#==============================================================================

# Question 1
def K(n):
    if n==0:
        return(1)
    else:
        somme=0
        for i in range(n):
            somme=somme+K(i)*K(n-1-i)
        return(somme)
    
# Question 3
def fact(n):
    if n==0:
        return(1)
    else:
        res=1
        for i in range(1,n+1):
            res=res*i
        return(res)


#==============================================================================
# Exercice 3
#==============================================================================

# Question 3
def less(L1,L2):
    return(L1[0]<L2[0] or (L1[0]==L2[0] and L2[1]<=L2[1]))

# Question 4
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


# Question 5
from math import pi
A=[-pi+i*pi/100 for i in range(0,201)]   

# Question 6
from math import cos,sin
B=[[(20+cos(10*a))*cos(a),(20+cos(10*a))*sin(a)] for a in A]


#==============================================================================
# Exercice 4
#==============================================================================

# Question 1
def comptage(S):
    dico={}
    for i in S:
        if i in dico:
            dico[i]=dico[i]+1
        else:
            dico[i]=1
    return(dico)

print(comptage('aaaaggbbbzdaaa'))

# Question 2       
def nbelem(S):
    return(len(comptage(S))) 

print(nbelem('aaaaggbbbzdaaa'))

# Question 3
def nbits(n):
    p=1
    while 2**p<n:
        p=p+1
    return(p)    
