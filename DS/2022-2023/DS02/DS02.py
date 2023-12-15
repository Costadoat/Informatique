import matplotlib.pyplot as plt

# Question 1:
file_in=open('comptage-velo-donnees-compteurs_light.csv','r')
contenu=file_in.read()
file_in.close()
lignes=contenu.split('\n')
print(lignes[0])
print(lignes[1])

# Question 2:
creneaux=[0]*24

for ligne in lignes[1:-1]:
    data=ligne.split(';')
    creneaux[int(data[5][11:13])]+=float(data[4])
print(creneaux)

# Question 3:
#plt.plot(creneaux)
#plt.show()

### Donnée ###
compteurs=[]
for ligne in lignes[1:-1]:
    data=ligne.split(';')
    data_compteur=[data[0],data[1],[float(d) for d in data[7].split(',')],0]
    if data_compteur not in compteurs:
        compteurs.append(data_compteur)
        
# Question 4:
print(len(compteurs))

# Question 5:
for ligne in lignes[1:-1]:
    data=ligne.split(';')
    for compteur in compteurs:
        if compteur[0]==data[0]:
            compteur[3]+=float(data[4])

### Donnée ###    
def distance(lieu1, lieu2):
    return ((lieu1[0]-lieu2[0])**2+(lieu1[1]-lieu2[1])**2)**(1/2)

# Question 6:
dorian=['0','74 Av. Philippe Auguste',[48.854576520866964, 2.3926308459105954],0]
print(distance(dorian[2],compteurs[0][2]))

# Question 7:
def get_five_more_close(hub):
    d=0
    five_more_close=[]
    while len(five_more_close)<5:
        d+=0.0001
        for compteur in compteurs:
            if distance(compteur[2],hub[2])<d and compteur not in five_more_close and compteur!=hub:
                five_more_close.append(compteur)
    return five_more_close

print(get_five_more_close(dorian))
    
# Question 8:
def get_max(compteurs):
    max=0
    for compteur in compteurs:
        if compteur[3]>max:
            max=compteur[3]
            plus_gros_hub=compteur
    return plus_gros_hub

print(get_max(compteurs))

# Question 9:
print(get_max(get_five_more_close(dorian)))

# Question 10:
parcours=[dorian]
for i in range(10):
    parcours.append(get_max(get_five_more_close(parcours[i])))
print(parcours)


# Question 11:
def get_five_more_close_v2(hub,exclude):
    d=0
    five_more_close=[]
    while len(five_more_close)<5:
        d+=0.0001
        for compteur in compteurs:
            if distance(compteur[2],hub[2])<d and compteur not in five_more_close and compteur not in exclude:
                five_more_close.append(compteur)
    return five_more_close

parcours=[dorian]
for i in range(10):
    parcours.append(get_max(get_five_more_close_v2(parcours[i],parcours)))
print(parcours)

