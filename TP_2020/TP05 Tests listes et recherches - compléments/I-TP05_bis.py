# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:05:29 2015

@author: willie
"""
## Calendrier grégorien

def nombre_de_jours_annees_classiques(jour,mois,annee):
  m = [31,28,31,30,31,30,31,31,30,31,30,31]
  nbjours = (annee-1600)*365 # nombre de jours ecoules pour les annees entieres
  for i in range(mois-1): # mois numerotes de 1 a 12 ; liste indexee de 0 a 11
    nbjours = nbjours + m[i]  # nombre de jours ecoules pour les mois entiers
  nbjours = nbjours + jour - 1 # nombre de jours ecoules pour le mois en cours
  return nbjours
  
def bissextile(annee):
  if annee % 4 == 0:
    if annee % 100 == 0:
      if annee % 400 == 0: 
        bissex = True # annee multiple de 400
      else:
        bissex = False # annee multiple de 4 et de 100 mais pas de 400
    else:
      bissex = True # annee multiple de 4 mais pas de 100
  else:
    bissex = False # annee non multiple de 4
  return bissex
    
def nombre_de_jours_toutes_annees(jour,mois,annee):
  m = [31,28,31,30,31,30,31,31,30,31,30,31]
  nbjours = 0
  for an in range(1600,annee): # pour tous les ans entierement ecoules
    if bissextile(an):
      nbjours = nbjours + 366 # si annee bissextile on ajoute 366
    else:
      nbjours = nbjours + 365 # sinon on ajoute 365
  for i in range(mois-1): 
    nbjours = nbjours + m[i] # nombre de jours ecoules pour les mois termines
  if (mois > 3 or mois == 3) and bissextile(annee):
    nbjours = nbjours + 1 # on ajoute 1 si fevrier est termine et annee en cours bissextile
  nbjours = nbjours + jour - 1 # nombre de jours ecoules pour le mois en cours
  return nbjours  

date=(2,3,1608)
jour=date[0]
mois=date[1]
annee=date[2]
  
print nombre_de_jours_annees_classiques(jour,mois,annee)
print nombre_de_jours_toutes_annees(jour,mois,annee)

jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

print(jours[
( nombre_de_jours_toutes_annees(1,4,1587) 
- nombre_de_jours_toutes_annees(1,1,2001) ) % 7
])

print(jours[
( nombre_de_jours_toutes_annees(24,11,2015) 
- nombre_de_jours_toutes_annees(1,1,2001) ) % 7
])

## Carré magique
def verif_carre_1(T):
  n = len(T) #nombre de lignes/colonnes
  ## DETERMINATION DES SOMMES
  resu_somme=[]
  # Boucles sur les lignes
  for i in range(n):
    somme=0
    for j in range(n):
      somme = somme + T[i][j]
    resu_somme.append(somme)
  # Boucles sur les colonnes
  for j in range(n):
    somme=0
    for i in range(n):
      somme = somme + T[i][j]
    resu_somme.append(somme)
  # diagonale 1
  somme=0
  for i in range(n):
    somme = somme + T[i][i]
  resu_somme.append(somme)
  # diagonale 2
  somme=0
  for i in range(n):
    somme = somme + T[i][n-1-i]
  resu_somme.append(somme)

  ##VERIFICATION DU CARRE
  #On verifie que chaque element de la liste est
  #egal au premier element de la liste
  for i in range(1,len(resu_somme)):
    if resu_somme[i] != resu_somme[0]:
      return False # on sort de la fonction en renvoyant False
  # sinon le carre est magique on renvoie True
  return True

def verif_carre_2(T):
  n = len(T) #nombre de lignes/colonnes
  ## DETERMINATION DES SOMMES
  resu_somme=[]
  # Boucles sur les lignes
  for i in range(n):
    somme=0
    for j in range(n):
      somme = somme + T[i][j]
    resu_somme.append(somme)
    # comparaison du dernier element avec le dernier
    if resu_somme[i] != resu_somme[0]:
      return False # on sort de la fonction en renvoyant False
  # Boucles sur les colonnes
  for j in range(n):
    somme=0
    for i in range(n):
      somme = somme + T[i][j]
    resu_somme.append(somme)
    # comparaison du dernier element avec le dernier
    if resu_somme[i] != resu_somme[0]:
      return False # on sort de la fonction en renvoyant False
  # diagonale 1
  somme=0
  for i in range(n):
    somme = somme + T[i][i]
  resu_somme.append(somme)
  # comparaison du dernier element avec le dernier
  if resu_somme[i] != resu_somme[0]:
    return False # on sort de la fonction en renvoyant False
  # diagonale 2
  somme=0
  # comparaison du dernier element avec le dernier
  if resu_somme[i] != resu_somme[0]:
    return False # on sort de la fonction en renvoyant False
  for i in range(n):
    somme = somme + T[i][n-1-i]
  resu_somme.append(somme)
# sinon le carre est magique, on renvoie True
  return True
  
T1 = [ [2,7,6] , [9,5,1] , [4,3,7] ]

resultat1=verif_carre_1(T1)

resultat2=verif_carre_2(T1)

print resultat1, resultat2

