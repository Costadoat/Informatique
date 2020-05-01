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
    n=len(resultats_equipes)
    for i in range(n):
        if int(resultats_equipes[i][2])!= int (resultats_equipes[i][3])+int (resultats_equipes[i][4])+int(resultats_equipes[i][5]):
            return "problème nb match"
        a=0
        for j in range(0,4):
             a+=points[j]*int(resultats_equipes[i][j+3]) 
        if int(resultats_equipes[i][1])!= a:
            return "problème nb points"
        if int(resultats_equipes[i][9])!=int(resultats_equipes[i][7])-int(resultats_equipes[i][8]):
            return"problème goal-average"

    classement=[]
    rc=resultats_equipes
    while rc !=[]:
        m=len(rc)
        imax=0
        for i in range(1,m):
            if int(rc[i][1])>int(rc[imax][1]) or int(rc[i][1])==int(rc[imax][1]) and int(rc[i][9])>int(rc[imax][9]):
                imax=i
        classement.append(rc[imax])
        rc.remove(rc[imax])    
    return classement






print   generer_classement(resultats_equipes,points)