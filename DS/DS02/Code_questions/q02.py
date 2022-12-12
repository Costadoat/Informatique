# Question 2:
creneaux=[0]*24

for ligne in lignes[1:-1]:
    data=ligne.split(';')
    creneaux[int(data[5][11:13])]+=float(data[4])
print(creneaux)
