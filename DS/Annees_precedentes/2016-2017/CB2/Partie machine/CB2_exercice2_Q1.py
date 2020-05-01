    
#==============================================================================
# Exercice 2 
#==============================================================================

# Q1   

import matplotlib.pyplot as plt 
 
fichier = open('exercice2.csv','r')

LX=[]
LY=[]

for i in fichier:
    donnee=i.split(';')
    LX.append(float(donnee[0]))
    LY.append(float(donnee[1]))  
 
