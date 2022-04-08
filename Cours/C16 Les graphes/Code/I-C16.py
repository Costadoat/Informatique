G={'A':['B','D','E'],'B':['A','C','E'],'C':['B','D'],'D':['A','C','G'],'E':['A','B','F'],'F':['E','G'],'G':['D','F','H','I'],'H':['G','J'],'I':['G'],'J':['H']}


def parcours_largeur(G):
    noeud_depart='A'
    file=[noeud_depart]
    noeuds_decouverts=[noeud_depart]
    while len(file)!=0:
        print('File:'+str(file))
        noeud_courant=file[0]
        file.remove(noeud_courant)
        for voisin in G[noeud_courant]:
            if voisin not in noeuds_decouverts:
                noeuds_decouverts.append(voisin)
                file.append(voisin)
    return noeuds_decouverts

print('Noeuds découverts:'+str(parcours_largeur(G)))

def parcours_profondeur(G):
    noeud_depart='A'
    pile=[noeud_depart]
    noeuds_decouverts=[noeud_depart]
    while len(pile)!=0:
        print('Pile:'+str(pile))
        noeud_courant=pile[-1]
        pile.remove(noeud_courant)
        for voisin in G[noeud_courant]:
            if voisin not in noeuds_decouverts:
                pile.append(voisin)
                noeuds_decouverts.append(voisin)
    return noeuds_decouverts

print('Noeuds découverts:'+str(parcours_profondeur(G)))
