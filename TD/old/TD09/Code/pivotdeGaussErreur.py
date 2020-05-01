# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""



def ligneRef(A,i) :
    n=len(A)
    maxi = abs(A[i,i])
    jmax = i
    for j in range(i+1,n) :
        if abs(A[j,i]) > maxi :
            maxi = abs(A[j,i])
            jmax = j
    return jmax

import copy
def echangeLignes (A,i,j) :
    A1=copy.deepcopy (A[i])
    A2=copy.deepcopy (A[j])
    A[j]=A1
    A[i]=A2
    
def transvection(A,i,j,alpha) :
    A[j]=A[j]-alpha*A[i]


def pivotGauss (A,B) :
    n=len(A)
    print n
    for i in range (n) :
        print i
        jmax = ligneRef (A,i )
        pivot=A[jmax,i]
        if pivot==0:
            return ( 'erreur' )
# echange l i g n e s i e t jmax dans A e t dans B
        echangeLignes(A,i,jmax)
        echangeLignes(B,i,jmax)
# n o rm a l i s a t i o n de l a l i g n e du p i v o t
        for j in range (n) :
            A[i,j] = A[i,j]/pivot
        B[i] = B[i]/pivot
# on e l im i n e l e s termes au d e s s u s e t en d e s s o u s du p i v o t
        for j in range (n) :
            print i,j
            if j != i :
                alpha=A[j,i]
                transvection (A,i,j,alpha)
                B[j]=B[j]-alpha*B[i]
                
    return B

A=np.array([[2.,3.],[1.,4.]])
B=np.array([1.,2.])

print pivotGauss(A,B)