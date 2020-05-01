#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:44:36 2019

@author: willie
"""

texte_initial = 'lycee dorian.'
mot_cle='ptsi'

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',\
          'n','o','p','q','r','s','t','u','v','w','x','y','z']

def nettoyage(L1):    
    L2=[]
    for caractere in L1:
        if caractere in alphabet:
            L2.append(caractere)
    return L2

print nettoyage(texte_initial)

def lettres_vers_entiers(L1):
    L2=[]
    for lettre in L1:
        L2.append(alphabet.index(lettre))
    return L2
        
print lettres_vers_entiers(nettoyage(texte_initial))

def chiffrement_vigenere(L,C):
    L2=[]
    i=0
    while i < (len(L)):
        L2.append(L[i]+C[i%len(C)])
        i=i+1
    return L2

print chiffrement_vigenere(\
	lettres_vers_entiers(nettoyage(texte_initial)),\
	lettres_vers_entiers(mot_cle)\
			)

def entiers_vers_lettres(L1):
    L2=[]
    for entier in L1:
        L2.append(alphabet[entier%len(alphabet)])
    return L2

texte_chiffre=entiers_vers_lettres(\
        chiffrement_vigenere(\
            lettres_vers_entiers(nettoyage(texte_initial)),\
            lettres_vers_entiers(mot_cle)\
                            )\
                    )
print texte_chiffre



