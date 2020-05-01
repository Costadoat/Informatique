#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:52:24 2019

@author: jg
"""


import numpy as np

def recherche_pivot(A,i):
    n=len(A)
    maxi = abs(A[i][i])
    kmax = i
    for k in range(i+1,n):
        if abs(A[k][i]) > maxi:
            maxi = abs(A[k][i])
            kmax = k
    return kmax,maxi


def permutation(A,i,j):
    t = A[i]
    A[i] = A[j]
    A[j] = t
        

def transvection(A,i,j,x):
    # si vecteur
    if type(A[0]) != list:
        A[i] = A[i] + x*A[j]
    else:
        n = len(A[0])
        for k in range(n):
            A[i][k] = A[i][k] + x*A[j][k]
            
            
def rang(A):
    n=len(A)
    rang=n
    for i in range(n):
        i0 = recherche_pivot(A,i)[0]
        pivot=recherche_pivot(A,i)[1]
        if pivot==0:
            rang=rang-1
        else :   
            permutation(A,i,i0) 
            for k in range(i+1,n):
                x = A[k][i]/A[i][i]
                transvection(A,k,i,-x)
    return rang
   
  
A=[[1,1,1],[1,1,1],[1,1,1]]  

print rang(A)  