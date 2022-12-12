# Question 5:
for ligne in lignes[1:-1]:
    data=ligne.split(';')
    for compteur in compteurs:
        if compteur[0]==data[0]:
            compteur[3]+=float(data[4])
