# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent 
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des 
# tests automatiquement et sans effort: il suffira de decommenter la ligne #if 
# #if __name__ == '__main__': testeur.fais_tests('...') 
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est 
# ***absolument primordial*** de lancer l'execution dans le menu via 
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon 
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)
# ***************************************************************************


# On importe la batterie de tests uniquement a l'execution du fichier et non 
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP13 as testeur


# ***************************************************************************
# Quelques histoires de triangles
# ***************************************************************************

triangles_01 = '''Produit des cotes pour perimetre superieur ou egal a 100'''
triangles_02 = '''Longueurs AB,AC et BC pour minimum precedent'''
triangles_03 = '''Tous les triangles rectangles en A'''
triangles_04 = '''Le nombre de triangles rectangles en A'''
triangles_05 = '''Le maximum des perimetres des triangles rectangles en A'''
triangles_06 = '''Tous les triangles equilateraux'''
triangles_07 = '''Tous les triangles tels que la moyenne des cotes vaille 42'''
        
# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('triangles')

# ***************************************************************************
# Communes, departements et regions de France
# ***************************************************************************

communes_01 = '''Liste des communes avec departement, region et population'''
communes_02 = '''Pareil avec ordre decroissant de population'''
communes_03 = '''Rang de Strasbourg dans le classement des villes de France par population'''
communes_04 = '''Rang du Bas-Rhin dans le classement des departement de France par population'''
communes_05 = '''Rang de l'Alsace dans le classement des regions de France par population'''
communes_06 = '''Liste des communes dont le nom commence par "Pa" et finit par "is"'''
communes_07 = '''Liste des communes qui ont moins d'habitant que de lettres'''


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('communes')

# ***************************************************************************
# Prenoms parisiens
# ***************************************************************************

prenom_choisi = 'JJ'  # Mettre ici votre prenom (sans accent)
prenoms_01 = '''Nombre de fois ou le prenom 'prenom_choisi' a ete donne dans les annees concernees'''
prenoms_02 = '''Nombre de prenoms differents par annee'''
prenoms_03 = '''Prenoms donnes exactement 100 fois sur la periode complete'''
prenoms_04 = '''Prenoms donnes exactement 100 fois sur au moins une annee'''
prenoms_05 = '''Prenom le plus donne sur la periode (avec nombre total)'''
prenoms_06 = '''Prenom le plus donne pour chaque annee (avec annee et nombre)'''


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('prenoms')


# ***************************************************************************
# Notes de colles
# ***************************************************************************

colles_01 = '''Liste des noms des professeurs'''
colles_02 = '''Liste des noms des eleves'''
colles_03 = '''Nombre total de "20" attribues'''
colles_04 = '''Nombre de notes superieures ou egales a 6'''
colles_05 = '''Notes de Jacques-Louis Lions (triees selon les semaines croissantes)'''
colles_06 = '''Pareil mais en rajoutant le nom du colleur'''
colles_07 = '''Quadruplets (nom eleve,nom prof,note,semaine) pour toutes les colles de note >= 19'''
colles_08 = '''Moyenne des notes de Jacques-Louis Lions'''
colles_09 = '''Nom des eleves qui ont eu au moins 10 notes strictement sous la moyenne'''
colles_10 = '''Nom des eleves ayant eu au moins 6 notes stritemement superieures a 18'''
colles_11 = '''Liste des couples (nom eleve,moyenne)'''
colles_12 = '''Nom du colleur avec qui il vaut mieux passer (donne les meilleurs notes en moyenne)'''
colles_13 = '''Triplets (colleur, moyenne, variance) pour tous les colleurs'''
colles_14 = '''Nom du colleur qui donne les notes les plus semblables'''
colles_15 = '''Moyenne des moyennes des eleves'''


# Ligne suivante a decommenter pour tester 
#if __name__ == '__main__': testeur.fais_tests('colles')



# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
