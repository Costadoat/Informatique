#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:31:15 2021

@author: jg
"""

#==============================================================================
# Recherche séquentielle dans un tableau unidimensionnel : recherche du 2eme max
#==============================================================================

L=[1,0,-9,16,18,-10,4]

def DeuxiemeMax(L):
    Max=L[0]
    DeuxiemeMax=L[1]
    if Max<DeuxiemeMax:
        (Max,DeuxiemeMax)=(DeuxiemeMax,Max)
    for i in range(2,len(L)):
        if L[i]>Max:
            DeuxiemeMax=Max
            Max=L[i]
        elif:
            L[i]>DeuxiemeMax
            DeuxiemeMax=L[i]
    return(Max,DeuxiemeMax)        

#print(DeuxiemeMax(L))


#==============================================================================
# Recherche séquentielle dans un tableau unidimensionnel : Comptage des éléments 
# d’un tableau à l’aide d’un dictionnaire.
#==============================================================================

L=[1,1,3,3,1,4,1,1]

def Comptage(L):
    freq={}
    for i in L:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    return(freq)        

#print(Comptage(L))




#==============================================================================
# Boucles imbriquées : recherche des deux valeurs les plus proches dans un tableau. 
#==============================================================================


L=[13,2,7,1,0,19,-1]

def ValeursPlusProches(L):
    Mindifference=abs(L[0]-L[1])
    indices=[0,1]
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            difference=abs(L[i]-L[j])
            if Mindifference>difference:
                Mindifference=difference
                indices=[i,j]
    return(Mindifference,L[indices[0]],L[indices[1]])            
            
#print(ValeursPlusProches(L))           



#==============================================================================
# Boucles imbriquées : tri à bulles
#==============================================================================

def TriBulle(L):
    for i in range(len(L)):
        for j in range(0,len(L)-i-1):
            if L[j]>L[j+1]:
                (L[j],L[j+1])=(L[j+1],L[j])
    return(L)            
            
#print(TriBulle(L))        



#==============================================================================
# Fonctions récursives : Version récursive d’algorithmes dichotomiques. 
#==============================================================================

def f(x):
    return(x**2-2)

def dicho(a,b,f,n):
    if n == 0:
        return(a)
    c=(a+b)/2.
    if f(a)*f(c)<0:
        return(dicho(a,c,f,n-1))
    else:
        return(dicho(c,b,f,n-1))

#print(dicho(0,3,f,10))


#==============================================================================
# Fonctions récursives : Enumeration des sous-listes
#==============================================================================

L=[1,29,0]
      
        
        
def SousListe(L):
    if len(L)==0:
        return([[]])
    PremierTerme=L[0]
    AncienneSousListe=SousListe(L[1:])
    NouvelleSousListe=[]
    for i in AncienneSousListe:
        NouvelleSousListe.append([PremierTerme]+i)      
    return(NouvelleSousListe+AncienneSousListe)        
    
 
print(SousListe(L))






#==============================================================================
# Fonctions récursives : Enumeration des permutations
#==============================================================================



def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            nextList.append(newString)
    return nextList

#print(Permute('abcd'))
