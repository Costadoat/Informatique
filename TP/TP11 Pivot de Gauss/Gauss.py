# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:04:23 2016

@author: G
"""

# Pivot de Gauss
# on veut resoudre AX = B, A etant n x n et supposee inversible

import numpy as np

# recherche du pivot maximal dans la colonne i, en lignes i, i+1, ..., n
# renvoie le numero de la ligne du pivot
def ligneRef(A,i):
    n=len(A)
    maxi = abs(A[i,i])
    kmax = i
    for k in range(i+1,n):
        if abs(A[k,i]) > maxi:
            maxi = abs(A[k,i])
            kmax = k
    return kmax
    
	
def echangeLignes(A,i,k):
    n=len(A)
    for p in range(n):
        x = A[i,p]
        A[i,p] = A[k,p]
        A[k,p] = x
    
        
def transvection(A,i,k,alpha):
    n=len(A)
    for j in range(n):
        A[k,j]=A[k,j]-alpha*A[i,j]    
        

def pivotGauss(A,B):
    n=len(A)
    for i in range(n):
        kmax = ligneRef(A,i)
        pivot=A[kmax,i]   
        if pivot==0:
            return('erreur')
        # echange lignes i et kmax dans A et dans B
        echangeLignes(A,i,kmax)
        b = B[kmax]
        B[kmax] = B[i]
        B[i] = b
        # normalisation de la ligne du pivot
        for j in range(n):
            A[i,j] = A[i,j]/pivot   
        B[i] = B[i]/pivot
        # on elimine les termes au dessus et en dessous du pivot
        for k in range(n):
            if k != i:
                alpha=A[k,i]
                transvection(A,i,k,alpha)  
                B[k]=B[k]-alpha*B[i]       
    return B

# exemple

A = np.array([[1,3,9],[-11,1,2.3],[7,2.,2]])
B = np.array([7,8.0,1])
print(pivotGauss(np.copy(A),np.copy(B)))

# avec SciPy

from scipy import linalg
#print linalg.solve(np.copy(A),np.copy(B))


# Inversion d une matrice 

def inverse(A):
    n=len(A)
    #I est la matrice identite de taille n
    # toutes les operations effectuees sur A sont faites sur I
    I=np.eye(n)
    for i in range(n):
        kmax = ligneRef(A,i)
        pivot=A[kmax,i]  
        print pivot
        if pivot==0:
            return('erreur')
        # echange lignes i et jmax dans A et dans B
        echangeLignes(A,i,kmax)
        echangeLignes(I,i,kmax)
        # normalisation de la ligne du pivot
        for j in range(n):
            A[i,j] = A[i,j]/pivot   
            I[i,j] = I[i,j]/pivot
        # on elimine les termes au dessus et en dessous du pivot
        for k in range(n):
            if k != i:
                alpha=A[k,i]
                transvection(A,i,k,alpha)  
                transvection(I,i,k,alpha)       
    return I

# exemple

A = np.array([[10,21.],[1/3.+1/7.,1.]])
#print inverse(np.copy(A))

# avec numpy

#print(np.linalg.matrix_power(A,-1))
        
