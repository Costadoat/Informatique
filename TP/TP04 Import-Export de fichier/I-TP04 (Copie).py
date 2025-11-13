# coding: utf-8
import matplotlib.pyplot as plt
import math as m

file=open('temperature-quotidienne-departementale_complet.csv','r')
filew=open('temperature-quotidienne-departementale.csv','w')
contenu=file.read()
file.close()

dep=['75','93']
year=['2018','2019']

lignes=contenu.split('\n')
temperatures=[]
count=0
for ligne in lignes[1:]:
    data=ligne.split(';')
    if data[0][1:5] in year and data[1] in dep:
        filew.write(ligne+'\n')
        count+=1

print(count)


