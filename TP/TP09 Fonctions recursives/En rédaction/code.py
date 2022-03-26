#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 18:29:47 2022

@author: jg
"""

#==============================================================================
# Puissance
#==============================================================================

def f(x,p):
    if p==0:
        return(1)
    else:    
        return(x*f(x,p-1))	

print(f(5,3))    


#==============================================================================
# Pyramide
#==============================================================================

def pyramide(n):
    if n==0:
        return('')
    else:
        print(n*'*')
        return(pyramide(n-1))
        
#print(pyramide(3))


#==============================================================================
# Dichotomie
#==============================================================================

def dicho(f,a,b,n):
    c=(a+b)/2.
    if n==0:
        return(c)
    else:
        if f(a)*f(c)<0:
            return(dicho(f,a,c,n-1))
        else:
            return(dicho(f,c,b,n-1))
   
def g(x):
    return(x**2-2)            
#print(dicho(g,0,2,5))


#==============================================================================
# Exponentiation rapide
#==============================================================================

def exp_rapide(x,n):
    if n==0:
        return(1)
    else:
        if n%2==0:
            return(exp_rapide(x**2,n//2))
        else:
            return(x*exp_rapide(x**2,(n-1)//2))


import time 


x=1230
p=502

start=time.time()
(exp_rapide(x,p))
end=time.time()
print(end-start)
        

start=time.time()
(f(x,p))
end=time.time()
print(end-start)    
        


#==============================================================================
# Sous-listes
#==============================================================================

def SousListe(L):
    if len(L)==0:
        return([[]])
    DernierTerme=L[len(L)-1]
    AncienneSousListe=SousListe(L[0:len(L)-1])
    NouvelleSousListe=[]
    for i in AncienneSousListe:
        NouvelleSousListe.append(i+[DernierTerme])      
    return(NouvelleSousListe+AncienneSousListe) 

L=[1,2,3,4]
#print(len(SousListe(L))==2**len(L))

#==============================================================================
# Rendu-monnaie
#==============================================================================

monnaie_euro=[50,20,10,5,2,1]

def rendu(m,L):
    if m==0:
        return(L)
    else:
        i=0
        while i<len(monnaie_euro) and m<monnaie_euro[i]:
            i=i+1   
        L[i]=L[i]+1
        m=m-monnaie_euro[i]
        return(rendu(m,L))

   
 
#print(rendu(216,len(monnaie_euro)*[0]))           