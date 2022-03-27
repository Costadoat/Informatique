# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""

import numpy
       
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
    
def resolution_systeme(A0,b0):
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
    
A = [ [2.,2.,-3.,4.], [-2.,-1.,-3.,2.], [6.,4.,4.,5.] , [1.,5.,3.,2.] ]
b = [2.,-5.,16.,11.]
print(resolution_systeme(A,b))

x = numpy.linalg.solve(A,b)
print(x[0],x[1],x[2],x[3])
