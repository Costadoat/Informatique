# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""

import numpy

l1=0.2
l2=0.1
l3=0.1
l4=0.35
l5=0.05
l6=0.4
F=2000.

A=[[1.,0.,-1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,1.,0.,-1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[-(2*l5+l6),0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,-1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,1.,0.,-1.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,-l2,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,-1.,0.,-1.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,0.,-1.,0.,-1.,1.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,l6,0.,0.,0.,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,1.,0.,0.,0.],
[0.,0.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,1.,0.,0.],
[0.,0.,0.,0.,l5,l2+l3+l4,0.,0.,0.,l3,0.,0.,0.,0.,0.],
[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,1.,0.],
[0.,-1.,0.,0.,0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,1.],
[0.,-(l3+l4),0.,0.,0.,0.,0.,l3,0.,0.,0.,0.,0.,0.,0.] ]

B=[0.,0.,0.,F,0.,-l1*F,0.,0.,0.,0.,0.,0.,0.,0.,0.]

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
    
def recherche_pivot(A, j0):
    n = len(A) 
    imax = j0 
    for i in range(j0+1, n):
        if abs(A[i][j0]) > abs(A[imax][j0]):
            imax = i
    return imax

def triangle(A,b):
    n =len(b)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/ A[i][i]
    return x
    
def resolution_systeme(A,b):
    n = len(A)

    for i in range(n-1):
        i0 = recherche_pivot(A,i)
        permutation(A,i,i0)
        permutation(b,i,i0) 
        
        for k in range(i+1,n):
            x = A[k][i]/A[i][i]
            transvection(A,k,i,-x)
            transvection(b,k,i,-x) 
            
    return triangle(A,b)

print resolution_systeme(A,Y)

x = numpy.linalg.solve(A,Y)
print x