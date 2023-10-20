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





#==============================================================================
# Exercice 3
#==============================================================================



#14
bonbons2=[]
for element in bonbons:
    bonbons2.append([element[1]/element[0],element[0],element[1]])
