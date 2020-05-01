# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 16:15:37 2016

@author: costa
"""

####################PREPARATION###########################

#Preparation fichier
import os
import numpy as np

def lecture():
    yf=[]

    fichier = open("departements.csv", "r")
    contenu = fichier.read()

    lignes=contenu.split("\n")
    for ligne in lignes:
        coord=ligne.split(";")
        yf.append([coord[0],coord[1],coord[2],float(coord[3]),float(coord[4])])
    return yf
    
####################CORRECTION###########################


yf=lecture()

print yf