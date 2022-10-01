#Question 1:

fichier_postes=open('postesSynop.csv','r')
contenu_postes=fichier_postes.read()
fichier_postes.close()
lignes_postes=contenu_postes.split('\n')
entetes_postes=lignes_postes[0].split(';')
postes=lignes_postes[1:]
print(entetes_postes)


#Question 2:
print(postes[3])

# Question 3:

def distance_ville(ville1,ville2):
    return ((ville1[0]-ville2[0])**2+(ville1[1]-ville2[1])**2)**(1/2)

paris=[48.85,2.34]

# Question 4:

min=distance_ville(paris,[0,0])
for poste in postes[:-1]:
    poste=poste.split(';')
    coord_ville=[float(poste[2]),float(poste[3])]
    if distance_ville(paris,coord_ville)<min:
        ville_plus_proche=poste[:2]
        min=distance_ville(paris,coord_ville)
    
print(ville_plus_proche)

# Question 5:

max=0
for poste in postes[:-1]:
    poste=poste.split(';')
    coord_ville=[float(poste[2]),float(poste[3])]
    if distance_ville(paris,coord_ville)>min:
        ville_plus_loin=poste[:2]
        max=distance_ville(paris,coord_ville)
print(ville_plus_loin)

#############################################################################
####Code perso pour générer fichiers#########################################
#############################################################################

for mois in ['07','08']:
    fichier_in=open('synop.2022'+mois+'.csv','r')
    fichier_out=open('synop.2022'+mois+'01.csv','w')
    contenu=fichier_in.read()
    fichier_in.close()
    lignes=contenu.split('\n')
    entetes=lignes[0]
    fichier_out.write(entetes+'\n')
    data=lignes[1:-1]
    for idx,donnees_jour in enumerate(data):
        data_jour=donnees_jour.split(';')
        if data_jour[1][8:]=='000000':
            fichier_out.write(donnees_jour+'\n')
    fichier_out.close()

#############################################################################

fichier=open('synop.20220701.csv','r')
contenu=fichier.read()
lignes=contenu.split('\n')
entetes=lignes[0].split(';')
data=lignes[1:]
print(entetes)
print(entetes.index('rr24'))
fichier.close()

print(entetes[42])

precip=[]
for mois in ['07','08']:    
    fichier=open('synop.2022'+mois+'01.csv','r')
    contenu=fichier.read()
    fichier.close()
    lignes=contenu.split('\n')
    data=lignes[1:]
    for idx,donnees_jour in enumerate(data):
        donnees_jour=donnees_jour.split(';')
        if donnees_jour[0]==ville_plus_proche[0]:
            precip.append([donnees_jour[1][:8],donnees_jour[42]])

#print(precip)

# Question 6:

precip2=[]
for prec in precip:
    if prec[1]!='mq':
        if float(prec[1])>0:
            precip2.append(prec)

print(precip2)

# Question 7:

jours_pluie=0
for prec in precip:
    if prec[1]!='mq':
        if float(prec[1])>0:
            jours_pluie+=1

print(jours_pluie,len(precip2))

# Question 8:

if (clock>180000 and clock<180100):
    if hydro<30:
        pompe=2
    else:
        pompe=1
elif hydro<5:
    pompe=3

