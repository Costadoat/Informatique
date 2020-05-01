# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:59:40 2017

@author: G
"""

#==============================================================================
#  Exercice 1
#==============================================================================

# Q1 : q=quotient=987, reste=6. 
# Si on recommence, avec 987, on trouve quotient=98, reste=7
# la suite des restes est constituee des chiffres de n

# Q2
print 9**3+8**3+7**3+6**3

# Q3
def somcube(n):
    s=0
    q=n
    while q>0:
        r=q%10
        q=q//10
        s=s+r**3
    return(s)        

for n in range(1001):
    if somcube(n)==n:
        print n

def somcube2(n):
    s=0
    n=str(n)
    for i in n:
        s=s+int(i)**3
    return(s) 

 

#==============================================================================
# Exercice 2 
#==============================================================================

# Q1   

import matplotlib.pyplot as plt 

#fichier = open('/home/prof/Ressources/CB2/exercice2.csv','r')
 
fichier = open('exercice2.csv','r')

LX=[]
LY=[]

for i in fichier:
    donnee=i.split(';')
    LX.append(float(donnee[0]))
    LY.append(float(donnee[1]))  
 

# Q2   
fichier.close()    
plt.plot(LX,LY,'*')
plt.plot(LX,LY)
plt.show()
plt.clf()


# Q3
def trapeze(X,Y):
     I=0
     for i in range(1,len(X)):
         I=I+(X[i]-X[i-1])*(Y[i]+Y[i-1])/2.
     return(I)
     
# Q4
print trapeze(LX,LY) 

#==============================================================================
# Exercice 3
#==============================================================================

import numpy as np


# Q1    

def g(x):
    if x>=0 and x<1:
        return x
    elif x>=1 and x<2:
        return 1

# Q2

gv=np.vectorize(g)
X=np.arange(0,1.99,0.01)  
plt.plot(X,gv(X))  
plt.show()
plt.clf() 

# Q3

def f(x):
    if x>=0 and x<2:
        return g(x)
    elif x>=2:
        return x**(0.5)*f(x-2)
        
# Q4

fv=np.vectorize(f)
XX=np.arange(0,6,0.01)  
plt.plot(XX,fv(XX))  
plt.show()
plt.clf()   


# Q6

eps=0.01
a=5
b=6
while b-a>eps:
    c  =  (a+b)/2.
    if f(c)>4:
        b  =  c
    else:
        a=c
print c        