# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:37:42 2015

@author: G
"""
#==============================================================================
# Exercice 6, Suite de Fibonacci
#==============================================================================

u=0
v=1
for i in range(9):
    (u,v)=(v,u+v)
print(v)


#==============================================================================
# Exercice 7
#==============================================================================

#import random
#
#nombre=random.randrange(10)                     # la variable 'nombre' est un entier 
#                                                # pris au hasard entre 0 et 9
#compteur=1                                                
#essai=input('entrer une valeur entre 0 et 9 ')   # la variable 'essai' est un nombre 
#                                                # entré par l'utilisateur
#while essai!=nombre:
#   essai=input('entrer une nouvelle valeur ')
#   compteur=compteur+1
#print('Vous avez gagné en ',compteur,' coups')


#==============================================================================
# Exercice 8
#==============================================================================

a=14
b=3
print(a%b)
while a>b:
    a=a-b
print(a)


#==============================================================================
# Exercice 9
#==============================================================================

n=input('entrer une valeur entière ')
p=0
k=1
if n%k == 0 :
   while k<=n :
      k = k+1  
   p=p+1   
print(p) 


#==============================================================================
# Exercice 11, Crible d'Eratosthene
#==============================================================================

from math import *
n=100


premiers=[]
nombres = []
N=int(sqrt(n))+1                    # N est l'entier strictement superieur a sqrt(n)

for i in range(2,n+1):
    nombres.append(True)           # nombres=[True,True,...] : on y stocke l'information True : le nombre est premier ou False : il ne l'est pas
for i in range(2,N+1):               # i parcourt les entiers de 2 à N
    if nombres[i-2]==True:         # si i n'est pas False, 
        premiers.append(i)         # alors c'est un nombre premier : on le stocke dans la liste
        for j in range(2*i,n+1,i): # les multiples de i entre 2i et n
            nombres[j-2] = False   # sont alors marqués comme False
                                    # si i n'est pas False, 
            
for i in range(N+1,n+1):            # on ajoute a la liste 'premiers' les nombres marqués True
    if nombres[i-2]==True:         
        premiers.append(i)             
print(premiers)
