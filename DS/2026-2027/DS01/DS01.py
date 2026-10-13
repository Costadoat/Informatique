import random

# ============================================================
# Exercice 3 - Question 4 : fonctions
# ============================================================

def affichage_menu(fosse, gradin, carre_or):
    print("\n=== Catégories disponibles ===")
    print("1 - Fosse (133.50 euros) [stock :", fosse, "]")
    print("2 - Gradin (232.5 euros) [stock :", gradin, "]")
    print("3 - Carré Or (298.5 euros) [stock :", carre_or, "]")
    print("0 - Quitter")


def vendre_billet(nom, stock, prix, achats):
    # Exercice 4 (Bonus) : une fois sur 20, surclassement offert en Carré Or
    if stock == 0:
        print("Plus de places en " + nom + ".")
    elif random.randrange(20) == 0:
        print("Coup de chance ! Vous êtes surclassé(e) en Carré Or, offert !")
        stock -= 1
        achats += 1
    else:
        argent = int(input("Montant inséré : "))
        if argent < prix:
            print("Montant insuffisant.")
        else:
            print("Vous avez acheté une place en " + nom + ".")
            monnaie = argent - prix
            if monnaie > 0:
                print("Monnaie rendue :", monnaie, "euros")
            stock -= 1
            achats += 1
    return stock, achats


# ============================================================
# Programme principal
# ============================================================

# Exercice 1 : stocks de départ (correction des 3 erreurs)
fosse = 5
gradin = 5
carre_or = 5

achats = 0

print("Bienvenue à la billetterie en ligne !")

# Exercice 1 : boucle tant qu'il reste des places
while fosse > 0 or gradin > 0 or carre_or > 0:
    affichage_menu(fosse, gradin, carre_or)

    choix = int(input("Sélection ? "))

    if choix == 0:
        print("Merci, à bientôt !")
        break
    else:
        # Exercice 2 : cas Fosse
        if choix == 1:
            fosse, achats = vendre_billet('fosse', fosse, 133.50, achats)
        # Exercice 3 : cas Gradin
        elif choix == 2:
            gradin, achats = vendre_billet('gradin', gradin, 232.5, achats)
        # Exercice 3 : cas Carré Or
        elif choix == 3:
            carre_or, achats = vendre_billet('carre or', carre_or, 298.5, achats)
        else:
            print("Choix invalide.")

print("\n=== Fin du programme ===")
print("Nombre total de billets vendus :", achats)
