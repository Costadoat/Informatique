#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:39:00 2020

@author: jg
"""


#Q2
fichier=open('algo-pi.txt','r')
decpi=(fichier.read()).strip().split()[0]


#Q3
print('les premieres decimales de pi sont '+decpi[0:9])

print('les dernieres decimales sont '+decpi[-10:-1])

print('le fichier contient '+str(len(decpi))+' decimales')

#Q4
def estIci(P,M,i):
    reponse=-1
    j=0
    while j<len(M) and P[i+j]==M[j]:
        j=j+1
    if j==len(M):
        reponse=True
    return(reponse)

#Q5
def trouve(P,M):
    i=0
    while i<len(P)-len(M) and estIci(P,M,i)==-1:
        i=i+1
    if i<len(P)-len(M):
        return(i)
    else:
        return(-1)

#Q6
print trouve(decpi,'14159')
print decpi.find('14159')  
print trouve(decpi,'123456')
print trouve(decpi,'12345')  
print trouve(decpi,'1789') 
    
#Q7
def trouve2(P,M):
    position=[]
    i=0
    while i<len(P)-len(M):
        while i<len(P)-len(M) and estIci(P,M,i)==-1:
            i=i+1
        position.append(i)
        i=i+1
    return(position, len(position))
           
    
    
print(trouve2(decpi,'14159'))


    