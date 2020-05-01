# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 13:57:44 2017

@author: willie
"""

import matplotlib.pyplot as plt

fichier1=open('liste_coordonnees.csv','r')

coord=[]

for ligne in fichier1.readlines():
    coord.append(ligne.strip().split(';'))

coord.sort()

for i in range(len(coord)):
    plt.scatter(coord[i][0],coord[i][1],marker='x')

plt.legend(prop={'size':12})
plt.axis('equal')
plt.savefig('../img/Figure2.png')
plt.show()

fichier1.close()