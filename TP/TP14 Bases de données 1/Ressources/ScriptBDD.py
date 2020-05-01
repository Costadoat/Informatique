# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:13:54 2015

@author: willie
"""

import sqlite3
base = sqlite3.connect('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Cours et TP/TP 13/Fichiers et codes reponses/triangles.sqlite')
curseur = base.cursor()
res = curseur.execute("""SELECT * FROM triangles WHERE (ab+bc+ac)/3=42""")
foo = res.fetchall()
fichier=open('/home/willie/Travail/Mon Métier/PTSI/Cours et TD/Informatique/Cours et TP/TP 13/Fichiers et codes reponses/Reponse.csv','w')

for triangle in foo:
    for i in range(len(triangle)-1):
        fichier.write(str(triangle[i])+',')
    fichier.write(str(triangle[len(triangle)-1]))
    fichier.write('\n')
fichier.close()

base.close()
