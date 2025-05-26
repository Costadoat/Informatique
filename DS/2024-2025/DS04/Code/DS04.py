# Question 1
def inverse_liste(liste):
    return [liste[i] for i in range(len(liste)-1,-1,-1)]

print('Question 1')
print(inverse_liste(['A','B','C']))

# Question 2
def convert_bin(decimal):
    binaire=[]
    r=decimal
    while r>1:
        q=r//2
        r=r%2
        binaire.append(r)
        r=q
    binaire.append(r)
    return inverse_liste(binaire)

def convert_bin_default(decimal):
    a=str(bin(decimal))[2:]
    s=[*a]
    s=[int(i) for i in s]
    return s

print('\nQuestion 2')
print(convert_bin(17))    
print(convert_bin_default(17))    


# Question 3
def convert_decimal(binaire):
    decimal=0
    for i in range(len(binaire)):
        decimal+=binaire[len(binaire)-1-i]*2**i
    return decimal

print('\nQuestion 3')
print(convert_decimal(convert_bin(17)))

#Question 4
produit={'code barre':31002,'designation':"café noir",'prix':1.50,'horaire_scan':50525}

#Question 5
panier=[]
def enfiler(file,produit):
    # Méthode qui enfile le produit au panier
    file.append(produit)

enfiler(panier,produit)
print('\nQuestion 5')
print(panier)

#Question 6
panier2=[{'code barre':20333,'designation':"madeleines",'prix':4.30,'horaire_scan':40520},
                   {'code barre':1204,'designation':"sucre",'prix':3.40,'horaire_scan':40550},
                   {'code barre':2046,'designation':"chocolat",'prix':2.50,'horaire_scan':40612}]

#Question 7
def remplir(panier,panier2):
    # Méthode qui enfile un panier 2 dans un panier
    for element in panier2:
        panier.append(element)

remplir(panier,panier2)
print('\nQuestion 6')
print(panier)

#Question 8
def prix_total(panier):
    prix=0
    for element in panier:
        prix+=element['prix']
    return prix

print('\nQuestion 7')
print(prix_total(panier))

#Question 9
def duree_achats(panier):
    min=panier[0]['horaire_scan']
    max=panier[0]['horaire_scan']
    for element in panier[1:]:
        if element['horaire_scan']<min:
            min=element['horaire_scan']
        if element['horaire_scan']>max:
            max=element['horaire_scan']
    return max-min

print('\nQuestion 8')
print(duree_achats(panier))

#Question 10
def convertion_duree(duree):
    heures=duree//3600
    secondes=duree%3600
    minutes=secondes//60
    secondes=secondes%60
    return "{} heures, {} minutes et {} secondes".format(heures, minutes, secondes)

print('\nQuestion 10')
print(convertion_duree(duree_achats(panier)))

#Question 11
produits_commandes=[]
def commander(produit):
    produits_commandes.append(produit)

def defiler(panier):
    commander(panier[0])
    panier.pop(0)

def commander_panier(panier):
    while len(panier)>0:
        defiler(panier)

print('\nQuestion 11')
print('Panier avant commande')
print(panier)
commander_panier(panier)
print('Panier après commande')
print(panier)
print('Produits commandés')
print(produits_commandes) 


