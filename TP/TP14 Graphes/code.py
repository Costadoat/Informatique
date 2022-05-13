#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:44:01 2022

@author: jg
"""

#==============================================================================
# Parcours de graphe en longueur, profondeur
#==============================================================================

gr={'A':['B','D','E'],'B':['A','C','E'],'C':['B','D'],'D':['A','C','G'],'E':['A','B','F'],'F':['E','G'],'G':['D','F','H','I'],'H':['G','J'],'I':['G'],'J':['H']}



def PL(gr,s):
    files=[s]
    noeuds_decouverts=[s]
    while len(files)!=0:
        noeud_courant=files[0]
        files=files[1:]
        for voisin in gr[noeud_courant]:
            if voisin not in noeuds_decouverts:
                noeuds_decouverts.append(voisin)
                files.append(voisin)
    return(noeuds_decouverts)                

def PL2(gr,s):
    files=[s]
    noeuds_decouverts=[s]
    while len(files)!=0:
        print(files)
        noeud_courant=files[0]
        files=files[1:]
        for voisin in gr[noeud_courant]:
            if voisin not in noeuds_decouverts:
                noeuds_decouverts.append(voisin)
                files.append(voisin)
    return(noeuds_decouverts)                

PL2(gr,'A')
print("Les noeuds entrent par la fin et sortent par l'avant, il s'agit donc d'une file.")

def PP(gr,s):
    piles=[s]
    noeuds_decouverts=[]
    while len(piles)!=0:
        noeud_courant=piles[-1]
        piles=piles[:-1]
        for voisin in gr[noeud_courant]:
            if (voisin not in noeuds_decouverts) and (voisin not in piles):
                piles.append(voisin)   
        noeuds_decouverts.append(noeud_courant)
                
    return(noeuds_decouverts)

def PP2(gr,s):
    piles=[s]
    noeuds_decouverts=[]
    while len(piles)!=0:
        print(piles)
        noeud_courant=piles[-1]
        piles=piles[:-1]
        for voisin in gr[noeud_courant]:
            if (voisin not in noeuds_decouverts) and (voisin not in piles):
                piles.append(voisin)   
        noeuds_decouverts.append(noeud_courant)
                
    return(noeuds_decouverts)    

PP2(gr,'A')
print("Les noeuds entrent par la fin et sortent par la fin, il s'agit donc d'une pile.")

#==============================================================================
# Connexite
#==============================================================================

def EstConnexe(gr):
    sommet=gr.keys()[0]
    liste=PL(gr,sommet)
    return(len(liste)==len(gr.keys()))


def NbCompConnexe(gr):
    liste_sommets=gr.keys()
    Nb=0
    while len(liste_sommets)!=0:
        Nb=Nb+1
        sommet=liste_sommets[0]
        for voisin in PL(gr,sommet):
            liste_sommets.remove(voisin)
    return(Nb)       
            
#print(EstConnexe({1:[2],2:[1],3:[4],4:[3]})) 


#==============================================================================
# Dijkstra  
#==============================================================================

gr={'A':{'B':1,'C':2},'B':{'A':1,'D':4},'C':{'A':2},'D':{'B':4}}

def MinDistance(sousgr):
    sommet_mini=sousgr.keys()[0]
    mini=sousgr[sommet_mini]
    for sommet in sousgr.keys():
        if sousgr[sommet]<mini:
            mini=sousgr[sommet]
            sommet_mini=sommet
    return(sommet_mini)        
 
gr2={'A':{'B':5,'C':10,'D':9},'B':{'A':5,'E':10},'C':{'A':10,'F':21},'D':{'A':9,'G':32},'E':{'B':10,'F':2},'F':{'C':21,'E':2,'G':8},'G':{'D':32,'F':8}}           
            
def DicoDesDistances(gr,s):
    distance={}
    explores=[s]
    for sommet in gr.keys() :
        distance[sommet]=float('inf')
    distance[s]=0
    while len(explores)!=len(gr.keys()):
        noeud_courant=MinDistance(distance)
        for voisin in gr[noeud_courant]:
            if distance[voisin]>distance[noeud_courant]+gr[noeud_courant][voisin]:
                distance[voisin]=distance[noeud_courant]+gr[noeud_courant][voisin]
        explores.append(noeud_courant) 
    return(distance)  


def etapes(Graphe,depart,final,s_traites,dist,prec):
    """
    Etapes de l'algorithme de Dijkstra (version récursive)
        
    s_traites:  Liste des sommets déjà traités
    dist:       Distances minimales trouvées pour chaque sommet
    prec:       Indique pour chaque sommet, celui qui le précède dans le trajet le plus court trouvé    
    """    
    #on choisit le sommet à traiter:
    if not dist:
        #si aucune distance n'a été calculée, on choisit depart(et on note 0 comme distance pour le depart)
        s_courant=depart
        dist[s_courant]=0 
    else:
        #sinon on choisit un sommet non encore traité dont la distance calculée est minimale 
        non_traites={ s:dist.get(s,float('inf'))  for s in Graphe if s not in s_traites }
        s_courant=min(non_traites, key=non_traites.get)

    #si le sommet courant est celui à atteindre
    if s_courant==final:
        #construction de la liste des sommets, à rebours
        Chaine=[final]
        while Chaine[-1]!=depart:
            Chaine.append(prec[Chaine[-1]])
        #on renvoie la distance minimale trouvée et la liste des sommets
        Chaine.reverse()
        return dist[final],Chaine

    #on traite tous les voisins du sommet courant
    for voisin in Graphe[s_courant]:
        #on récupère la distance précédemment calculée pour ce voisin (+inf si non atteint)
        dist_voisin_prec=dist.get(voisin,float('+inf'))
        #on calcule la nouvelle distance obtenue

        dist_voisin_new=dist[s_courant]+Graphe[s_courant][voisin]
        #on compare les deux distances et on modifie si nécessaire
        if dist_voisin_new<dist_voisin_prec:
            dist[voisin]=dist_voisin_new
            prec[voisin]=s_courant

    #on ajoute le sommet courant à la liste des sommets traites
    s_traites.append(s_courant)

    #on réitère la méthode pour traiter le sommet suivant
    return etapes(Graphe,depart,final,s_traites,dist,prec)

def Dijkstra(Graphe,depart,final):
    """
    Application de l'algorithme de Dijkstra
    
    Graphe:     Graphe fourni sous forme d'un dictionnaire
    depart:     Sommet initial du trajet cherché 
    final:      Sommet final du trajet cherché
    """  
    return etapes(Graphe,depart,final,[],{},{})
      

    

#==============================================================================
# Metro
#==============================================================================



fichier = open("data/data_nom.csv", "r")
fichier2 = open("data/data_arete.csv", "r")

tableau=fichier.read()
tableau2=fichier2.read()

fichier.close()
fichier2.close()

lignes=tableau.split('\n')
nom=[]
for i in lignes[:-1]:
    ligne=i.split(',')
    ligne[0]=int(ligne[0])
    nom.append(ligne)
    
lignes2=tableau2.split('\n')    
arete=[]
for i in lignes2[:-1]:
    ligne=i.split(',' )
    arete.append([int(ligne[0]),int(ligne[1]),float(ligne[2])])
    
dico={}
for i in arete:
    if i[0] not in dico:
        dico[i[0]]={i[1]:i[2]}
    else:
        dico[i[0]][i[1]]=i[2]

Trajet=Dijkstra(dico,88,302)

print(Trajet[0]/60.)
for i in Trajet[1]:
    print(nom[i])
