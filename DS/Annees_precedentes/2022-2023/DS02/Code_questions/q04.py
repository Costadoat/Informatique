### Donnée ###
compteurs=[]
for ligne in lignes[1:-1]:
    data=ligne.split(';')
    if [data[0],data[1],data[7],0] not in compteurs:
        compteurs.append([data[0],data[1],[float(d) for d in data[7].split(',')],0])

# Question 4:
print(len(compteurs))
