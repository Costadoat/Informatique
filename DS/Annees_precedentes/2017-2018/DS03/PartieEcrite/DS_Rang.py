#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 08:13:01 2018

@author: jg
"""

import numpy as np

C=np.array([[1/2.,1,1],[1/3.,0,1],[1/6.,1,0]])

def transvection(C,i,k,a):
    C[k]=C[k]-a*C[i]
    
def echangeLigne(C,i,k):
    n=len(C)
    for j in range(n):
        C[i,j],C[k,j]=C[k,j],C[i,j]
    
def LigneRef(C,i):
    n=len(C)
    kmax=i
    for k in range(i,n):
        if abs(C[k,i])>abs(C[kmax,i]):
            kmax=i
    return(kmax)
     
        

def rang(C):
    n=len(C)
    rang=n # on part du rang maximal.
    for i in range(n):
        kmax=LigneRef(C,i) # On recherche la ligne de reference, qui aura le pivot le plsu grand en valeur absolue
        if C[kmax,i]==0 : # si le pivot est nul, la matrice a une colonne nulle
            rang=rang-1 # on diminue la valeur du rang de 1
        else :
            echangeLigne(C,i,kmax) # sinon, on échelonne la matrice.
            for k in range(i+1,n):
                transvection(C,i,k,C[k,i]/float(C[i,i]))
    return(rang)                
                
            
print(C)       
print(rang(C)) 
print C
      
