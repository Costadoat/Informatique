# Question 1:

file=open('resultats.csv','r')
contenu=file.read()
equipes=contenu.split('\n')

print(equipes[0])

# Question 2:

resultats=[]
for equipe in equipes[:-1]:
    resultats.append(equipe.split(';')[:-1])

print(resultats[0])

# Question 3:

tableau_points=[]

for id,equipe in enumerate(resultats):
    tableau_points.append([equipe[0]])
    points_total=0
    buts_total=0
    for match in equipe[1:]:
        points_match,buts_pour,buts_contre=match.split(':')
        points_total+=int(points_match)
        buts_total+=int(buts_pour)-int(buts_contre)
        tableau_points[id].append([points_total,buts_total])

print(tableau_points[0])

# Question 4:

import matplotlib.pyplot as plt

plt.plot([point for point,buts in tableau_points[0][1:]])
plt.show()

# Question 5:

import matplotlib.pyplot as plt

for equipe in tableau_points:
    plt.plot([point for point,buts in equipe[1:]], label=equipe[0])
plt.legend()
plt.show()

# Question 6:

def tri_selection(liste): 
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

liste=[4,5,2,3,6,1]
tri_selection(liste)
print(liste)

# Question 7:

points_derniere_journee=[]

for equipe in tableau_points:
        points_derniere_journee.append(equipe[-1][0])
print(points_derniere_journee)

# Question 8:
points_derniere_journee_tri=points_derniere_journee.copy()
tri_selection(points_derniere_journee_tri)
print(points_derniere_journee_tri)

# Question 9:

liste_equipes=[]

for equipe in tableau_points:
        liste_equipes.append(equipe[0])
print(liste_equipes)

# Question 10:

def tri_selection(liste,liste2): 
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
        liste2[i],liste2[jmin]=liste2[jmin],liste2[i]

points_derniere_journee_tri=points_derniere_journee.copy()
liste_equipes_tri=liste_equipes.copy()
tri_selection(points_derniere_journee_tri,liste_equipes_tri)
print(liste_equipes_tri)

# Question 11:

classement_journees=[]

for journee in range(len(tableau_points[0])-1):
    liste_journee=[]
    for equipe in tableau_points:
        liste_journee.append(equipe[journee+1][0])
    liste_equipes_journee=liste_equipes.copy()
    tri_selection(liste_journee,liste_equipes_journee)
    classement_journees.append(liste_equipes_journee)

print(classement_journees[0])
