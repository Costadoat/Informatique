# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 09:50:22 2017

@author: costa
"""

fichier1=open('liste_eleves.csv','r')
contenu=fichier1.read()
fichier1.close()
fichier2=open('liste_login.csv','w')
liste_eleves=contenu.split('\n')
liste=[]
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for eleve in liste_eleves:
    data=eleve.split(';')
    login=data[1][0].lower()+data[0][:7].lower()
    passwd=''
    for i in range(3):
        passwd+=str(abc.index(data[1][i].lower()))
    fichier2.write(data[0]+";"+data[1]+";"+login+";"+passwd+"\n")
fichier2.close()
    
