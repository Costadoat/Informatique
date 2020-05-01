# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 09:41:45 2018

@author: costa
"""

points=[4,2,0,1]

fichier = open("classement.csv", "r")
contenu=fichier.read()
lignes=contenu.split('\n')
resultats_equipes=[]
for ligne in lignes[:-1]:
    equipe=ligne.split(';')
    resultats_equipes.append(equipe)

def generer_classement(resultats_equipes,points):
    classement=resultats_equipes
    return classement

print generer_classement(resultats_equipes,points)