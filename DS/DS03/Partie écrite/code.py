#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:08:31 2021

@author: jg
"""

import numpy as np
import matplotlib.pyplot as plt


def somme_ligne(A,i):
    n=len(A[0])
    somme=0
    for j in range(n):
        somme=somme+A[i,j]
    return(somme)

def somme_colonne(A,j):
    n=len(A[0])
    somme=0
    for i in range(n):
        somme=somme+A[i,j]
    return(somme) 
    

def test(A):
    n=len(A[0])
    sigma=somme_ligne(A,0)
    numero_ligne=1
    while numero_ligne<n and somme_ligne(A,numero_ligne)==sigma:
        numero_ligne=numero_ligne+1
    numero_colonne=0
    while numero_colonne<n and somme_colonne(A,numero_colonne)==sigma:
        numero_colonne=numero_colonne+1
    if numero_colonne==numero_ligne and numero_ligne==n:
        return(sigma)
    else:
        return(False)

print(test(A))
