#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:12:08 2021

@author: jg
"""


#==============================================================================
# Exercice 1
#==============================================================================

#1
fichier = open("liste_nombres.csv", "r")

contenu=fichier.read()
fichier.close()

lignes=contenu.split('\n')

L=[]
for i in lignes:
    L.append(float(i)) 



#2
#print(L[0:30])


#3

def dicho(L, a):
    debut = 0
    fin = len(L) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if L[m] == a:
            return m
        elif L[m] < a:
            debut = m + 1
        else:
            fin = m - 1
    return False

#4
#print(dicho(L,1.56))
#print(dicho(L,2))


#5
somme=0
for i in L:
    somme=somme+i
#print(somme/len(L))    

#6
#print(L[len(L)//2])


#==============================================================================
# Exercice 2
#==============================================================================

#7
def maxi(L):
    maxi=L[0]
    position=0
    for i in range(1,len(L)):
        if L[i]>maxi:
            maxi=L[i]
            position=i
    return(maxi,position)

#8
def maxi_liste(L):
    maxi=L[0]
    position=[0]
    for i in range(1,len(L)):
        if L[i]>maxi:
            maxi=L[i]
            position=[i]
        elif L[i]==maxi:
            position.append(i)
    return(maxi,position)    

#9
#print(maxi_liste([9,1,3,9,2,9]))        


#==============================================================================
# Exercice 3
#==============================================================================

#10
bonbons=[[3,2.5],[1.5,1.5],[1.,0.9]]

#11

print(bonbons[2][0])
print(bonbons[2][1])

#12
B=11

i=0
achat=[]
while i<len(bonbons) and B>0:
    if bonbons[i][0]<B:
        achat.append(bonbons[i])
        B=B-bonbons[i][0]
    else:
        i=i+1
               
#13
Satisfaction_totale=0
for element in achat:
    Satisfaction_totale=Satisfaction_totale+element[1]
print(Satisfaction_totale)


#14
bonbons2=[]
for element in bonbons:
    bonbons2.append([element[1]/element[0],element[0],element[1]])

#15
bonbons2.sort(reverse=True)

#16
B=11
i=0
achat2=[]
while i<len(bonbons2) and B>0:
    if bonbons2[i][1]<B:
        achat2.append(bonbons2[i])
        B=B-bonbons2[i][1]
    else:
        i=i+1
print(achat2)        
   
#17
Satisfaction_totale2=0
for element in achat2:
    Satisfaction_totale2=Satisfaction_totale2+element[2]
print(Satisfaction_totale2)

#18
