# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 13:51:53 2015
@author: willie
"""

#==============================================================================
# Questions 1 et 2 : on ouvre le fichier et on l'affecte a une variable
#==============================================================================
fichier = open('/home/eleve/PTSI/TP6/TP6.txt','r')
#==============================================================================



#==============================================================================
# Question 3
#==============================================================================
for ligne in fichier: # on lit ligne par ligne
    for caractere in ligne: # et caractere par caractere
        print caractere
 
fichier.close()     # on referme le fichier sinon au prochain acces on est deja 
                    # en bout de fichier

#fichier.seek(0)    # alternative pour se repositionner en debut de fichier
#==============================================================================



#==============================================================================
# Question 4
#==============================================================================
fichier = open('/home/eleve/PTSI/TP6/TP6.txt','r')
 
liste_mots=[] # on initialise une liste de mots appelee mots
mot='' # on initialise une liste de caracteres appelee mot
 
for ligne in fichier:
    mots=[] #on initialise la liste des mots de la ligne
    for caractere in ligne:
        if caractere == ',' or caractere == '\n':# le mot est fini
            mots=mots+[mot] # on ajoute le mot a la liste des mots de la ligne
            mot='' # on reinitialise pour le prochain mot
        else: # le mot n est pas fini 
            mot=mot+caractere # on ajoute le caractere au mot
    liste_mots=liste_mots+[mots] # la ligne est finie on ajoute les mots 
                                 # de la ligne a la liste demandee

fichier.close()

# print liste_mots
#==============================================================================
         


#==============================================================================
# Question 5
#==============================================================================
## sur certains systemes d exploitation la fin du fichier ne peut parfois pas 
## etre detectee correctement dans les boucles
## en consequence, le dernier mot de la dernière ligne n'est pas traite 
## correctement on l ajoute manuellement a la liste des mots et on ecrase 
## la derniere ligne
#
#mots=mots+[mot]
#liste_mots[-1]=mots
#
#print liste_mots
#==============================================================================

         

#==============================================================================
#Question 6
#==============================================================================
fichier = open('/home/eleve/PTSI/TP6/TP6.txt','r')
fichiertab = open('/home/eleve/PTSI/TP6/TP6tab.txt','w')

for ligne in fichier: # on lit ligne par ligne
    for caractere in ligne: # et caractere par caractere
        if caractere == ',': # si le caractere est une virgule
            caractere = '\t' # on le remplace par une tabulation
        fichiertab.write(caractere) # on ecrit le caractere dans le fichier
        
fichier.close()
fichiertab.close()        
#==============================================================================



#==============================================================================
#Question 7
#==============================================================================
#Question 4 avec des methodes python

fichier = open('/home/eleve/PTSI/TP6/TP6.txt','r')
liste=[]
for ligne in fichier.readlines():
    liste.append(ligne.strip().split(','))
print liste
fichier.close()    

#Question 6 avec des methodes python
fichier = open('/home/eleve/PTSI/TP6/TP6.txt','r')
fichiertab = open('/home/eleve/PTSI/TP6/TP6tab.txt','w')

texte=fichier.read()    # lit la totalite du fichier et la renvoie comme 
                        # une unique chaine de caracteres
textetab=texte.replace(',','\t')    # produit une copie du texte dans laquelle 
                                    # les virgules sont replaxcees par des 
                                    # tabulations
fichiertab.write(textetab) # ecrit le texte tabule dans fichiertab

fichier.close()
fichiertab.close()     
#==============================================================================



#==============================================================================
#Question 8
#==============================================================================
fichier1 = open('/home/eleve/PTSI/TP6/TP6tab.txt','r')
fichier2 = open('/home/eleve/PTSI/TP6/TP6.tsv','w')

fichier2.write(fichier1.read())# ecrit le texte tabule dans fichiertab
fichier1.close()
fichier2.close()     
#==============================================================================



#==============================================================================
#Question 9
#==============================================================================

import math as math

fichier  = open('/home/eleve/PTSI/TP6/notes.csv','r')
fichier2 = open('/home/eleve/PTSI/TP6/notes_et_moyennes.csv','w')

donnees=[] # on initialise la liste des donnees
donneesseparees=[] # on initialise la liste des donnees separees

for ligne in fichier: # on parcourt le fichier ligne a ligne
# on elimine les caracteres d echappement
    ligne_sans_echappement=ligne.strip() 
# on cree la liste des donnees separees par une virgule
    liste_donnees_separees_d_une_ligne=ligne_sans_echappement.split(',') 
# on ajoute a la liste des listes de donnees separees
    donneesseparees=donneesseparees+[liste_donnees_separees_d_une_ligne] 
# on cree la liste des lignes de donnees non separees et sans echappement
    donnees=donnees+[ligne_sans_echappement] 
    
def moyenne_eleve(note1,note2,note3):
    return (1*note1+2*note2+3*note3)/6

moyennes=[] # on initialise une liste des moyennes des eleves

for i in range(len(donneesseparees)):  # on parcourt ligne a ligne
    note1=float(donneesseparees[i][2]) # on recupere la note 1
    note2=float(donneesseparees[i][3]) # on recupere la note 2
    note3=float(donneesseparees[i][4]) # on recupere la note 3
# on calcule la moyenne et on l ajoute a la liste des moyennes
    moyennes=moyennes+[moyenne_eleve(note1,note2,note3)] 

for i in range(len(donnees)):
# on ajoute la moyenne de l eleve i a sa ligne et on termine la ligne
    donnees[i]=donnees[i]+','+str(moyennes[i])+'\n' 

# on ajoute l en tete
donnees_avec_entete=['nom,prenom,note1,note2,note3,moyenne\n']+donnees 

# on parcourt chaque ligne de la liste des listes des donnees avec en tete
for ligne in donnees_avec_entete: 
    fichier2.write(ligne) # on ecrit chaque ligne dans le fichier

def moyenne(liste_valeurs):
    """renvoie la moyenne des valeurs
    contenue dans la liste passée en paramètres"""
    somme=0
    for valeur in liste_valeurs: # somme des valeurs
        somme=somme+valeur
    return somme/len(liste_valeurs)

def variance(liste_valeurs):
    """renvoie la variance des valeurs
    contenue dans la liste passée en paramètres"""
    somme_carres_ecarts=0
    for valeur in liste_valeurs: # somme des carres des ecarts à la moyenne
        somme_carres_ecarts=somme_carres_ecarts+(valeur-moyenne(liste_valeurs))**2
    return somme_carres_ecarts/len(liste_valeurs)
    
def ecart_type(liste_valeurs):
    """renvoie l'écart-type des valeurs
    contenue dans la liste passée en paramètres"""
    return math.sqrt(variance(liste_valeurs))

print "moyenne de la classe = ", moyenne(moyennes)
print "écart-type des moyennes = ", ecart_type(moyennes)

fichier.close()
fichier2.close()
#==============================================================================
