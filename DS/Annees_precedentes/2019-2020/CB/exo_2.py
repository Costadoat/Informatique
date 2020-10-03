#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:30:18 2020

@author: jg
"""

#Q1
def LDP(n):
    diviseurs=[]
    for i in range(1,n/2+1):
        if n%i==0:
            diviseurs.append(i)
    return(diviseurs)        
        
print(LDP(100))

#Q2
def SDP(n):
    return(sum(LDP(n)))

print(SDP(100))


#Q3
def parfaits(K):
    liste=[]
    for i in range(1,K):
        if SDP(i)==i:
            liste.append(i)
    return(liste)        

print(parfaits(2000))


#Q4
def amicaux(K):
    liste_amicaux=[]
    liste_SDP=[0]
    for i in range(1,K+1):
        liste_SDP.append(SDP(i))
    for q in range(1,K+1):
        for p in range(1,q):
            if liste_SDP[p]==q and liste_SDP[q]==p:
                liste_amicaux.append((p,q))
    return(liste_amicaux)

print(amicaux(5000))          