print('# Question 1')

import random

# Stocks de départ
soda = 5
cafe = 5
jus = 5

achats = 0

print("Bienvenue dans le distributeur automatique !")

# Boucle tant qu’il reste des boissons
while soda > 0 or cafe > 0 or jus > 0:
    print("\n=== Menu ===")
    print("1 - Soda (2 €) [stock :", soda, "]")
    print("2 - Café (1 €) [stock :", cafe, "]")
    print("3 - Jus  (3 €) [stock :", jus, "]")
    print("0 - Quitter")

    choix = int(input("Sélection ? "))

    if choix == 0:
        print("Merci, à bientôt !")
        break
    else:
        # Cas Soda
        if choix == 1:
            print("Soda demandé")

print("\n=== Fin du programme ===")
print("Nombre total d’achats :", achats)

print('# Question 2')

import random

# Stocks de départ
soda = 5
cafe = 5
jus = 5

achats = 0

print("Bienvenue dans le distributeur automatique !")

# Boucle tant qu’il reste des boissons
while soda > 0 or cafe > 0 or jus > 0:
    print("\n=== Menu ===")
    print("1 - Soda (2 €) [stock :", soda, "]")
    print("2 - Café (1 €) [stock :", cafe, "]")
    print("3 - Jus  (3 €) [stock :", jus, "]")
    print("0 - Quitter")

    choix = int(input("Sélection ? "))

    if choix == 0:
        print("Merci, à bientôt !")
        break
    else:
        # Cas Soda
        if choix == 1:
            if soda == 0:
                print("Plus de soda en stock.")
            else:
                argent = int(input("Insérez votre argent : "))
                if argent < 2:
                    print("Pas assez d’argent.")
                else:
                    print("Vous avez acheté un soda.")
                    monnaie = argent - 2
                    if monnaie > 0:
                        print("Monnaie rendue :", monnaie, "€")
                    soda -= 1
                    achats += 1

print("\n=== Fin du programme ===")
print("Nombre total d’achats :", achats)

print('# Question 3')

import random

# Stocks de départ
soda = 5
cafe = 5
jus = 5

achats = 0

print("Bienvenue dans le distributeur automatique !")

# Boucle tant qu’il reste des boissons
while soda > 0 or cafe > 0 or jus > 0:
    print("\n=== Menu ===")
    print("1 - Soda (2 €) [stock :", soda, "]")
    print("2 - Café (1 €) [stock :", cafe, "]")
    print("3 - Jus  (3 €) [stock :", jus, "]")
    print("0 - Quitter")

    choix = int(input("Sélection ? "))

    if choix == 0:
        print("Merci, à bientôt !")
        break
    else:
        # Cas Soda
        if choix == 1:
            if soda == 0:
                print("Plus de soda en stock.")
            else:
                argent = int(input("Insérez votre argent : "))
                if argent < 2:
                    print("Pas assez d’argent.")
                else:
                    print("Vous avez acheté un soda.")
                    monnaie = argent - 2
                    if monnaie > 0:
                        print("Monnaie rendue :", monnaie, "€")
                    soda -= 1
                    achats += 1

        # Cas Café
        elif choix == 2:
            if cafe == 0:
                print("Plus de café en stock.")
            else:
                argent = int(input("Insérez votre argent : "))
                if argent < 1:
                    print("Pas assez d’argent.")
                else:
                    print("Vous avez acheté un café.")
                    monnaie = argent - 1
                    if monnaie > 0:
                        print("Monnaie rendue :", monnaie, "€")
                    cafe -= 1
                    achats += 1

        # Cas Jus
        elif choix == 3:
            if jus == 0:
                print("Plus de jus en stock.")
            else:
                argent = int(input("Insérez votre argent : "))
                if argent < 3:
                    print("Pas assez d’argent.")
                else:
                    print("Vous avez acheté un jus.")
                    monnaie = argent - 3
                    if monnaie > 0:
                        print("Monnaie rendue :", monnaie, "€")
                    jus -= 1
                    achats += 1
        else:
            print("Choix invalide.")

print("\n=== Fin du programme ===")
print("Nombre total d’achats :", achats)

print('# Question 4')

import random

def affichage_menu(soda, cafe, jus):
    print("\n=== Menu ===")
    print("1 - Soda (2 €) [stock :", soda, "]")
    print("2 - Café (1 €) [stock :", cafe, "]")
    print("3 - Jus  (3 €) [stock :", jus, "]")
    print("0 - Quitter")

def servir_boisson(nom,stock,prix,achats):

    if stock == 0:
        print("Plus de "+nom+" en stock.")
    else:
        argent = int(input("Insérez votre argent : "))
        if argent < prix:
            print("Pas assez d’argent.")
        else:
            print("Vous avez acheté un "+nom+".")
            monnaie = argent - prix
            if monnaie > 0:
                print("Monnaie rendue :", monnaie, "€")
            stock -= 1
            achats += 1
    return stock,achats

# Stocks de départ
soda = 5
cafe = 5
jus = 5

achats = 0

print("Bienvenue dans le distributeur automatique !")

# Boucle tant qu’il reste des boissons
while soda > 0 or cafe > 0 or jus > 0:
    affichage_menu(soda, cafe, jus)
    
    choix = int(input("Sélection ? "))

    if choix == 0:
        print("Merci, à bientôt !")
        break
    else:
        # Cas Soda
        if choix == 1:
            soda,achats=servir_boisson('soda',soda,2,achats)
        # Cas Café
        elif choix == 2:
            cafe,achats=servir_boisson('cafe',cafe,1,achats)
        # Cas Jus
        elif choix == 3:
            jus,achats=servir_boisson('jus',jus,3,achats)
        else:
            print("Choix invalide.")

print("\n=== Fin du programme ===")
print("Nombre total d’achats :", achats)

print('# Question 5')

import random

def servir_boisson(nom,stock,prix,achats):

    if stock == 0:
        print("Plus de "+nom+" en stock.")
    elif random.randrange(10) == 0:
        print("On vous offre un "+nom+" !")
        stock -= 1
        achats += 1
    else:
        argent = int(input("Insérez votre argent : "))
        if argent < prix:
            print("Pas assez d’argent.")
        else:
            print("Vous avez acheté un "+nom+".")
            monnaie = argent - prix
            if monnaie > 0:
                print("Monnaie rendue :", monnaie, "€")
            stock -= 1
            achats += 1
    return stock,achats

# Stocks de départ
soda = 5
cafe = 5
jus = 5

achats = 0

print("Bienvenue dans le distributeur automatique !")

# Boucle tant qu’il reste des boissons
while soda > 0 or cafe > 0 or jus > 0:
    affichage_menu(soda, cafe, jus)
    
    choix = int(input("Sélection ? "))

    if choix == 0:
        print("Merci, à bientôt !")
        break
    else:
        # Cas Soda
        if choix == 1:
            soda,achats=servir_boisson('soda',soda,2,achats)
        # Cas Café
        elif choix == 2:
            cafe,achats=servir_boisson('cafe',cafe,1,achats)
        # Cas Jus
        elif choix == 3:
            jus,achats=servir_boisson('jus',jus,3,achats)
        else:
            print("Choix invalide.")

print("\n=== Fin du programme ===")
print("Nombre total d’achats :", achats)

