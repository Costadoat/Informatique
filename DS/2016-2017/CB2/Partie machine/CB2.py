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



# Préparation du fichier :
fichier = open('exercice2.csv','w')

lx=[0,0.1,0.5,0.9,1,1.2,1.7,2.1,2.2,2.6,2.9,3.2,3.3,3.7,3.9,4]
ly=[1.345,1.456332,2.7258,2.9097,3.00001,2.9981082,2.6532145,2.0001236814,1.5443,1.727642,1.96415,1.9025734,1.87655463,1.6432851,1.52563723,1.324561732]


for i in range(len(lx)):
    fichier.write(str(lx[i])+';'+str(ly[i])+'\n')
    
fichier.close()     

#==============================================================================
# Exercice 2 
#==============================================================================

# Q1   

import matplotlib.pyplot as plt 
 
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

# Q3
def trapeze(X,Y):
     I=0
     for i in range(1,len(X)):
         I=I+(X[i]-X[i-1])*(Y[i]+Y[i-1])/2.
     return(I)
     
# Q4
print trapeze(LX,LY)     