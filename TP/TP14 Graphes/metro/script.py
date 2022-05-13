#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 11:07:39 2022

@author: jg
"""

fichier = open("data_nom.txt", "r")
fichier2 = open("data_arete.txt", "r")
resultat = open("dico.csv", "w")

tableau=fichier.read()
tableau2=fichier2.read()

fichier.close()
fichier2.close()

lignes=tableau.split('\n')
nom=[]
for i in lignes:
    ligne=[int(i[0:4]),i[4:]]
    nom.append(ligne)
    
lignes2=tableau2.split('\n')    
arete=[]
for i in lignes2:
    ligne=i.split( )
    arete.append([int(ligne[0]),int(ligne[1]),float(ligne[2])])
    

resultat1=open("data_nom.csv",'w')
resultat2=open("data_arete.csv",'w')

for i in nom:
    resultat1.write(str(i[0])+str(',')+str(i[1])+str('\n'))
    
for i in arete:
    resultat2.write(str(i[0])+str(',')+str(i[1])+str(',')+str(i[2])+str('\n'))

resultat1.close()
resultat2.close()    