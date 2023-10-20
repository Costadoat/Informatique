#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:35:11 2020

@author: jg
"""


#Q1

def decoder(E,C):
    A=[]
    for i in range(len(E)):
        if C[i]!=0:
            A.append(E[i])
    return(A)        

print(decoder([2,3,5,7],[1,0,0,1]))


#Q2

def coder(E,A):
    C=[]
    for i in E:
        if i in A:
            C.append(1)
        else:
            C.append(0)
    return(C)   

print(coder([2,3,5,7],[2,7]))  


#Q3

def incrementer(C):
    I=[]
    for j in C:
        I.append(j)
    i=-1
    while i>-len(C) and C[i]==1:
        I[i]=0
        i=i-1
    I[i]=1    
    return(I)


#Q4

def parties(E):
    C=[0]*len(E)
    liste_parties=[]
    for i in range(2**len(E)):
        liste_parties.append(decoder(E,C))
        C=incrementer(C)
    return(liste_parties)   

print(parties(['a','b','c'])) 
    