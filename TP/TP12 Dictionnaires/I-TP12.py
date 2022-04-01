##############
# Exercice 1
##############

def comptage(mot):
    '''renvoie un dictionnaire contenant le nombre
    d'occurences de chaque caractère du mot'''
    occurrences = {}
    for caractere in mot:
        if caractere in occurrences:
            occurrences[caractere] = occurrences[caractere] + 1
        else:
            occurrences[caractere]=1
    return occurrences

##############
# Exercice 2
##############

print(comptage('tatayoyo'))
print(comptage('yoayttoa'))
print(comptage('tatayoyo') == comptage('yyaottoa'))

##############
# Exercice 3
##############

def statistiques(texte):
    '''renvoie un dictionnaire contenant le nombre
    d'occurences de chaque caractère du texte
    à l'exclusion des ponctuations, espaces et saut de ligne'''
    occurrences = {}
    for caractere in texte:
        if caractere not in " ,;.:!?\n":
            if caractere in occurrences:
                occurrences[caractere] = occurrences[caractere] + 1
            else:
                occurrences[caractere]=1
    return occurrences

##############
# Exercice 4
##############

file=open('hugo.txt','r')
hugo=file.read()
file.close()
print(statistiques(hugo))

##############
# Exercice 5
##############

print(statistiques(hugo).items())

#Tri par insertion 
def tri_occurrences(dictionnaire):
    '''Tri par insertion des données du dictionnaire
    après obtention de la liste des couples clé/élément'''
    # création de la liste des couples clé/élément
    liste=list(dictionnaire.items())
    # Parcour de 1 à la taille de la liste
    for i in range(1, len(liste)):
        # On mémorise la position initiale de l'élément
        k = liste[i]
        # On décale cet élément vers la gauche tant que
        # l'élément précédent est plus grand que lui
        j = i-1
        while j >= 0 and k[1] > liste[j][1] : 
                liste[j + 1] = liste[j] 
                j -= 1
        liste[j + 1] = k
    return liste

def tri_occurrences2(dictionnaire):
    '''Tri à bulles des données du dictionnaire
    après obtention de la liste des couples clé/élément'''
    # création de la liste des couples clé/élément
    liste=list(dictionnaire.items())
    # Parcours de 1 à la taille de la liste
    for i in range(1, len(liste)):
        # Parcours des éléments précédents
        for j in range(0, len(liste)-i):
            # On permutte les deux éléments successifs
            if liste[j][1] < liste[j+1][1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return(liste)

print(tri_occurrences(statistiques(hugo)))
file=open('perec.txt','r')
perec=file.read()
file.close()
print(tri_occurrences(statistiques(perec)))

##print(tri_occurrences2(statistiques(hugo)))
##file=open('perec.txt','r')
##perec=file.read()
##file.close()
##print(tri_occurrences2(statistiques(perec)))

##############
# Exercice 6
##############

import unidecode
def enleve_diacritiques_majuscules_tirets(s):
    '''renvoie le mot s en minuscule, et sans les accents et cedilles'''
    return unidecode.unidecode(s).lower().replace('-','')

def sont_anagrammes(mot1, mot2):
    '''teste si deux mots sont anagrammes l'un de l'autre après
    avoir éliminé les diacritiques, accents, etc.'''
    return comptage(enleve_diacritiques_majuscules_tirets(mot1)) == comptage(enleve_diacritiques_majuscules_tirets(mot2))

print(sont_anagrammes('tatayoyo', 'yôyötâtà'))
print(sont_anagrammes('tatayoyo', 'chaudchocolat'))

##############
# Exercice 7
##############

fichier=open('listemotsfrancais.txt','r')
contenu=fichier.read()
fichier.close()
listemotsfrancais = contenu.split('\n')
print(listemotsfrancais[0:10])

##############
# Exercice 8
##############

def anagrammes(mot):
    '''renvoie un dictionnaire contenant un unique couple
    dont la clé est mot et l'élément est la listes des anagrammes
    de mot'''
    anagrammes = {}
    liste_anagrammes = []
    motbis=enleve_diacritiques_majuscules_tirets(mot)
    for motcandidat in listemotsfrancais:        
        motcandidatbis = enleve_diacritiques_majuscules_tirets(motcandidat)
        if mot != motcandidat:
            if sont_anagrammes(motbis,motcandidatbis):
                liste_anagrammes.append(motcandidat)
    anagrammes[mot] = liste_anagrammes
    return anagrammes

print(anagrammes('chien'))
