# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:26:39 2019

@author: Renaud
"""

fichier=open('Classement.txt','r')
contenu=fichier.read()
print(contenu)
equipes=contenu.split('\n')
liste_equipes=[]
for equipe in equipes:
    data=equipe.split(',')
    matchs_joues=int(data[1])+int(data[2])+int(data[3])
    points=4*int(data[1])+2*int(data[2])+int(data[4])
    liste_equipes.append([data[0],points,matchs_joues]+[int(d) for d in data[1:]])

max=[0,0]
classement=[]
for l in range(len(liste_equipes)):
    for i,equipe in enumerate(liste_equipes):
        if equipe[1]>max[0]:
            max=[equipe[1],equipe[-1]]
            imax=i
        elif equipe[1]==max[0]:
            if equipe[-1]>max[1]:
                max=[equipe[1],equipe[-1]]
                imax=i
    classement.append(liste_equipes[imax])
    liste_equipes[imax]=['Done',0,0,0,0,0,0,0]
    max=[0,0]

for equipe in classement:
    print(equipe)
    

