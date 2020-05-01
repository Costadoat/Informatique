#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:36:12 2018

@author: jg
"""

import numpy as np
import matplotlib.pyplot as plt



#==============================================================================
# Exercice 2 sur le produit de matrices     
#==============================================================================
 
# Q1

A=[[2,1,3],[0,-1,7]]

print 'le coefficient ligne 1 et colonne 2 de A est :', A[1][2]

# Q2
def taille(A):
    return([len(A),len(A[0])]) # A[0] est la 1ere ligne. Sa taille renvoie le nombre de colonne

# Q3    

def compatible(A,B):
    return(taille(A)[1]==taille(B)[0])

B=[[2],[0],[1]]

# Q4

def produit(A,B):
    if compatible(A,B): 
        n=taille(A)[0]
        p=taille(A)[1]
        l=taille(B)[1]
        C=[]  # on initialise C
        for i in range(n):
            ligne=[] # on initialise la ligne i 
            for j in range(l):
                somme=0
                for k in range(p):
                    somme=somme+A[i][k]*B[k][j]
                ligne.append(somme) # on complete la ligne avec le terme c_ij
            C.append(ligne) # on complete la matrice avec la ligne i    
        return(C)
    else:
        return(False)


#==============================================================================
# Exercice 3 sur les nombres narcisses
#==============================================================================

# Q1
n=93084
print 9**5+3**5+0**5+8**5+4**5==n

# Q2
print type(str(n)),len(str(n)),str(n)[3]
# str(n) est une chaine de caractere
# len(str(n)) renvoie le nombre de chiffres de n
# str(n)[3] renvoie le chiffre en position 3 du nombre

# Q3

def narcisse(n):
    sommeChiffre=0 # on initialise la somme des chiffres 
    longueur=len(str(n))
    for i in str(n):
        sommeChiffre=sommeChiffre+int(i)**longueur
    if sommeChiffre==n:
        return(True)
    else:
        return(False)

# Q4

for i in range(1,10001):
    if narcisse(i): # si le nombre est narcisse, on l affiche
        print i



    


#==============================================================================
# Exercice 4 sur l'ensemble de Julia
#==============================================================================

# Q1

n=10
c=0.5
u=0
print 'u',0,'=',u
for i in range(n):
    u=u**2+c
    print 'u',i+1,'=',u

# Q2

m=10
M=20

# k existe. on constate que u6<20 et u7>20. Donc k=7 (qui est bien inférieur à 10)

  
# Q3 a

def f(c):
    u=0
    n=0
    while (n<=m and abs(u)<=M): # tant que l'indice est petit et la valeur de un aussi,
        u=u**2+c # on calcule le terme suivant
        n=n+1
    return(n) # a la fin, si la condition n a jamais ete remplie, n vaut m+1

# Q3 b

print f(0.5)


# Q3 c

F=np.vectorize(f)
LX=np.linspace(-1,2,400)
plt.plot(LX,F(LX))



    


#==============================================================================
# Exercice 5 sur le calcul des parties de E
#==============================================================================

E=[1,7,4,11]
L=[0,1,0,1]


# Q1

def partie(E,L):
    liste=[]
    n=len(E)
    for i in range(n):
        if L[i]==1:
            liste.append(E[i])
    return(liste)

print partie(E,L)

# Q2
# 23 s ecrit : 10111 en binaire


# Q3
def binaire(k):
    liste=[]
    while k !=0:
        liste=[k%2]+liste
        k=k//2
    return(liste) 

print binaire(23)
print bin(23)  


#Q4

def P(E):
    n=len(E)
    cardPE=2**n
    listeParties=[]
    for i in range(cardPE):
        nombre=[0]*(n-len(binaire(i)))+binaire(i)
        listeParties.append(partie(E,nombre))
    return(listeParties)    
            
print(P(E))       