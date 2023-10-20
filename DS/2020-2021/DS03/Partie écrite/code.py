#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:08:31 2021

@author: jg
"""

import numpy as np
import matplotlib.pyplot as plt


A=np.array([[1,2],[2,1]])

B=np.array([[1,2,5],[2,1,0],[6,7,8]])

def somme_ligne(A,i):
    n=len(A[0])
    somme=0
    for j in range(n):
        somme=somme+A[i,j]
    return(somme)

def somme_colonne(A,j):
    n=len(A[0])
    somme=0
    for i in range(n):
        somme=somme+A[i,j]
    return(somme) 
    

def test(A):
    n=len(A[0])
    sigma=somme_ligne(A,0)
    numero_ligne=1
    while numero_ligne<n and somme_ligne(A,numero_ligne)==sigma:
        numero_ligne=numero_ligne+1
    numero_colonne=0
    while numero_colonne<n and somme_colonne(A,numero_colonne)==sigma:
        numero_colonne=numero_colonne+1
    if numero_colonne==numero_ligne and numero_ligne==n:
        return(sigma)
    else:
        return(False)

print(test(A))


def essai(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if somme_ligne(A,i)!=somme_colonne(A,j):
                return(False)

def test2(A):
    s=sum(A[0,:])
    for i in range(len(A)):
        if somme_ligne(A,i)!=s or somme_colonne(A,i)!=s:
            return(False)
        
        
print(test2(A),test2(B))        