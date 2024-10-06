# Tracé du visage

import matplotlib.pyplot as plt
import numpy as np

X1 = []
Y1 = []
Z1 = []

file = open("data.csv","r")
content=file.read()
file.close()

lignes=content.split("\n")

for ligne in lignes[:-1]:
    row=ligne.split(',')
    X1.append(float(row[0]))
    Y1.append(float(row[1]))
    Z1.append(float(row[2]))

X = np.asarray(X1)
Y = np.asarray(Y1)
Z = np.asarray(Z1)

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')
surf = ax.scatter(X, Y, Z)
plt.show()

# Test de personnalité

questions1 = [("Votre talent tient dans vos", "super-pouvoirs", "ressources"),
    ("Un animal est pour vous un", "symbole", "truc pas pratique lorsqu'on part en vacances")]

result=''

for question in questions1:
    question_string = "%s:\n\ta. %s\n\tb. %s\n[a/b]:  " % (question[0], question[1], question[2])
    answer = input(question_string).lower()
    while answer not in ("a", "b"):
        print("Please choose A or B")
        answer = input(question_string).lower()
    result = result + answer

if result == 'aa':
    print('Vous etes Spiderman !')
elif  result == 'ab':
    print('Vous etes Superman !')
elif  result == 'ba':
    print('Vous etes Batman !')
else:
    print('Vous etes Iron man !')


# Script pour tableau Kelly

import random as rd
import numpy as np
import matplotlib.pyplot as plt

largeur=82
hauteur=41
imagebase = np.ones([hauteur,largeur,3])

for j in range(largeur):
    spots=[]
    nb_points=-abs(j-(largeur//2))+(largeur//2)
    spots=rd.sample(range(41),nb_points)
    for i in spots:
        imagebase[i,j] = [0,0,0]

plt.imshow(imagebase)
plt.show()
