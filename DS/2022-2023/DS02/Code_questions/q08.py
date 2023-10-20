# Question 8:
def get_max(compteurs):
    max=0
    for compteur in compteurs:
        if compteur[3]>max:
            max=compteur[3]
            plus_gros_hub=compteur
    return plus_gros_hub

print(get_max(compteurs))
