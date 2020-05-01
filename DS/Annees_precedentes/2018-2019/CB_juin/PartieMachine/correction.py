#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:30:19 2019

@author: jg
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:52:24 2019
 
@author: jg
"""
 

#==============================================================================
# Exercice 1
#==============================================================================


#Q1

def permutation(A,i,j):
    t = A[i]
    A[i] = A[j]
    A[j] = t


#Q2

def transvection(A,i,j,x):
    n = len(A[0])
    for k in range(n):
        A[i][k] = A[i][k] + x*A[j][k]


#Q3
 
def recherche_pivot(A,i):
    n=len(A)
    maxi = abs(A[i][i])
    kmax = i
    for k in range(i+1,n):
        if abs(A[k][i]) > maxi:
            maxi = abs(A[k][i])
            kmax = k
    return kmax,maxi
 
 
#Q4                    
             
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
    
#Q5
   
A=[[1,1,1],[0,1,1],[0,0,1]]  
B=[[1,1,1],[1,1,1],[1,1,1]]  
 

print rang(A)




#==============================================================================
# Exercice 2
#==============================================================================

#Q1

def facto(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)


#Q5     
 
def sommef(n):
    N=str(n)
    somme=0
    for i in range(len(N)):
        somme=somme+facto(int(N[i]))
    return(somme)    
         
#Q6
    
n=0 
for i in range(100000):
    if sommef(i)==i:
        print(i)





#==============================================================================
# Exercice 3
#==============================================================================
 
#Q1

def sp(L):
    M=[]
    for i in range(len(L)):
        if i%2==0:
            M.append(L[-i/2-1])
        else:
            M.append(L[(i+1)/2-1])
    return(M)

#Q2
 
print(sp(range(1,7)))
print(sp(range(1,8))) 
 
 


#Q3

L=range(1,7)
for i in range(6):
    L=sp(L)
print(L)



#Q4  
 
def p(n):
    L=range(n)
    i=1
    Lorigine=L
    while sp(L)!=Lorigine:
        L=sp(L)
        i=i+1
    return(i)    
   

         
#Q5     
import matplotlib.pyplot as plt
 
X=range(1,100)
Y=[]
for i in X:
    Y.append(p(i)/float(i))        
     
plt.plot(X,Y)  

 
#Q6
print(Y.index(min(Y))+1)




