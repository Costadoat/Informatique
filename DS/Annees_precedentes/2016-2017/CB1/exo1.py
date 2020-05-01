# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 09:53:51 2016

@author: G
"""

def rect(a,b,c):
    A=a**2
    B=b**2
    C=c**2
    if A==B+C or B==A+C or C==A+B:
        return(True)
    else:
        return(False)
        


def triangle(p):
    L=[]
    for a in range(1,p+1):
        for b in range(1,p+1):
            for c in range(1,p+1):
                if a+b+c==p:
                    if rect(a,b,c):
                        L.append((a,b,c))
    return(L)                            


def triangle2(p):
    L=[]
    c=0
    for a in range(1,p//3+1):
        for b in range(a,(p-a)//2+1):
            c=c+1
            if rect(a,b,p-a-b):
                L.append((a,b,p-a-b))
    return(L,c)  

for p in range(12,60):
    print(triangle2(p),p**2/12)              