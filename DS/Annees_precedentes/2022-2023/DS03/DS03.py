# Question 1
file=open('athlete_events.csv','r')
contenu=file.read()
lignes=contenu.split('\n')
file.close()
print(lignes[5135])

# Question 2
countries=[]
for ligne in lignes[:-1]:
    data=ligne.split(";")
    if data[8]=='"1992 Winter"':
        if data[6] not in countries:
            countries.append(data[6])
print(countries[:6])

# Question 3
countries=[]
points=[]
for ligne in lignes[:-1]:
    data=ligne.split(";")
    if data[8]=='"1992 Winter"':
        if data[6] not in countries:
            countries.append(data[6])
            points.append([data[6],0])
print(points[:6])

# Question 4
for ligne in lignes[:-1]:
    data=ligne.split(";")
    if data[8]=='"1992 Winter"':
        index_pays=countries.index(data[6])
        if data[14]=='"Gold"':
            points[index_pays][1]+=3
        elif data[14]=='"Silver"':
            points[index_pays][1]+=2
        elif data[14]=='"Bronze"':
            points[index_pays][1]+=1
print(points[:6])

# Question 5
listepoints=[]
for point in points:
   if point[1]!=0:
       listepoints.append(point[1])
print(listepoints)

# Question 6
def tri(liste): # tri sélection
    # Parcours de 1 à la taille de la liste
    for i in range(len(liste)-1):
        # Initialiser le min
        min=liste[i]
        jmin=i
        for j in range(i, len(liste)):
        # Chercher le min
            if liste[j]<min:
                jmin=j
                min=liste[j]
        # Permuter le min et l'élément i
        liste[i],liste[jmin]=liste[jmin],liste[i]

tri(listepoints)
print(listepoints)

# Question 7
def inversion(liste):
    # Parcours de 1 à la taille de la liste
    for i in range(len(liste)//2):
        # Initialiser le min
        liste[i],liste[-i-1]=liste[-i-1],liste[i]

inversion(listepoints)
print(listepoints)

# Question 8
classement=[]
for lpoint in listepoints:
    i=0
    while lpoint!=points[i][1] or points[i] in classement:
        i+=1
    classement.append(points[i])
print(classement)

# Question 9
countries=[]
points=[]
for ligne in lignes[:-1]:
    data=ligne.split(";")
    if data[8]=='"1992 Winter"':
        if data[6] not in countries:
            countries.append(data[6])
            points.append([data[6],[0,0,0]])

event=[[],[],[]]            
for ligne in lignes[:-1]:
    data=ligne.split(";")
    if data[8]=='"1992 Winter"':
        index_pays=countries.index(data[6])
        if data[14]=='"Gold"' and data[13] not in event[0]:
            points[index_pays][1][0]+=1
            event[0].append(data[13])
        elif data[14]=='"Silver"' and data[13] not in event[1]:
            points[index_pays][1][1]+=1
            event[1].append(data[13])
        elif data[14]=='"Bronze"' and data[13] not in event[2]:
            points[index_pays][1][2]+=1
            event[2].append(data[13])

def tri2(liste): # tri sélection
    # Parcours de 1 à la taille de la liste
    for i in range(len(liste)-1):
        # Initialiser le min
        min=liste[i][1]
        jmin=i
        for j in range(i, len(liste)):
        # Chercher le min
            if liste[j][1][0]<min[0] or liste[j][1][0]==min[0] and liste[j][1][1]<min[1] or liste[j][1][0]==min[0] and liste[j][1][1]==min[1] and liste[j][1][2]<min[2]:
                jmin=j
                min=liste[j][1]
        # Permuter le min et l'élément i
        liste[i],liste[jmin]=liste[jmin],liste[i]
    
tri2(points)
inversion(points)
for idx,point in enumerate(points):
    if point[1]!=[0,0,0]:
        print(idx+1,point)


