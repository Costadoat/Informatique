# coding: utf-8

# Question 1

monnaie_euro=[500,200,100,50,20,10,5,2,1]

# Question 2

def montant(monnaie,liste):
    somme=0
    for idx,piece in enumerate(liste):
        somme+=piece*monnaie[idx]
    return somme

liste_monnaie=[0,0,0,1,0,1,0,2,0]
print("En donnant les pièces suivantes: {}, on rembourse {}€.".format(liste_monnaie,montant(monnaie_euro,liste_monnaie)))

# Question 3

liste_monnaie=[0,0,0,0,2,2,0,1,2]
print("En donnant les pièces suivantes: {}, on rembourse {}€.".format(liste_monnaie,montant(monnaie_euro,liste_monnaie)))

# Question 4

def rendre_monnaie_euro(restant_du):
    monnaie_euro=[500,200,100,50,20,10,5,2,1]
    monnaie_a_rendre=[0]*len(monnaie_euro)
    i=0
    while restant_du>0:
        if restant_du>=monnaie_euro[i]:
            monnaie_a_rendre[i]+=1
            restant_du+=-monnaie_euro[i]
        else:
            i+=1
    return(monnaie_a_rendre)

print("Pour rembourser {}€, il faut les pièces suivantes: {}.".format(242,rendre_monnaie_euro(242)))

# Question 5

print("Le montant remboursé est alors de {}€.".format(montant(monnaie_euro,rendre_monnaie_euro(242))))

# Question 6

def nombre_de_piece(liste):
    somme=0
    for piece in liste:
        somme+=piece
    return somme

print("Dans la liste {}, il y a {} pièces.".format(rendre_monnaie_euro(242),nombre_de_piece(rendre_monnaie_euro(242))))

# Question 7

def rendre_monnaie_non_canonique(montant_du):
    monnaie_non_canonique=[9,7,3,1]
    monnaie_a_rendre=[0]*len(monnaie_non_canonique)
    i=0
    while montant_du>0:
        if montant_du>=monnaie_non_canonique[i]:
            monnaie_a_rendre[i]+=1
            montant_du+=-monnaie_non_canonique[i]
        else:
            i+=1
    return(monnaie_a_rendre)

print("Pour rembourser {}€, dans le système non canonique, il faut les pièces suivantes: {}.".format(14,rendre_monnaie_non_canonique(14)))

print("Dans la liste {}, il y a {} pièces.".format(rendre_monnaie_non_canonique(14),nombre_de_piece(rendre_monnaie_non_canonique(14))))

# Question 8
    
monnaie_non_canonique=  

print("Dans la liste {}, il y a {} pièces, c'est mieux que le résultat de l'algorithme Glouton".format([0,2,0,0],nombre_de_piece([0,2,0,0])))

print("En donnant les pièces suivantes: {}, on rembourse {}€.".format([0,2,0,0],montant(monnaie_non_canonique,[0,2,0,0])))


# Question Allocation de salles

Horaire=[[0,2],[1,3],[1,4],[2,5],[7,8],[6,9]]

def Salle(Horaire):
    Planning=[]
    Libre=0
    Cours=0
    while Cours<len(Horaire):
        (debut,fin)=Horaire[Cours]
        if debut>=Libre:
            Planning.append([debut,fin])
            Libre=fin   
        Cours=Cours+1
    return(Planning)    


# Question empaqueter

Objets=[7,6,3,4,8,5]
Objets=[8,7,6,5,4,3]
C=11

def empaqueter(Liste_objets,C):
    Boite=[[]]
    Capacite_Boites=[C]
    for objet in Liste_objets:
        numero_boite=0
        while numero_boite<len(Boite) and objet>Capacite_Boites[numero_boite]:
            numero_boite=numero_boite+1
        if numero_boite>=len(Boite):
            Boite.append([objet])
            Capacite_Boites.append(C-objet)
        else:
            Boite[numero_boite].append(objet)
            Capacite_Boites[numero_boite]-=objet
    return(Boite)            
        
print(empaqueter(Objets.sort(reverse=True),C))    

