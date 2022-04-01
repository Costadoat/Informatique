from copy import copy
from time import process_time
import unidecode

def enleve_diacritiques_majuscules(s : str) -> str:
    '''renvoie le mot s en minuscule, et sans les accents et cedilles'''
    return unidecode.unidecode(s).lower().replace('-','')


def charger_liste_mots(filename : str) -> list:
    '''charge un fichier sous forme de liste de chaînes de caractères'''
    l = []
    with open(filename) as f:
        content = f.read().splitlines()
        for line in content:
            l.append(line)
    return l

liste_mots = charger_liste_mots('listemotsfrancais.txt')

## conversions

def string_to_list(s : str) -> list:
    '''convertit une chaîne de caractères en liste de caractères'''
    l = []
    for e in s:
        l.append(e)
    return l

def list_to_string(l : list) -> str:
    '''convertit une liste de caractères en chaîne'''
    s = ''
    for e in l:
        s = s + e
    return s

## une bien mauvaise méthode...

def permutations_aux(l : list, i : int) -> list:
    '''renvoie la liste des permutations de l laissant fixes les éléments d'indices strictement inférieurs à i'''
    if i == len(l):
        return [copy(l)]
    else:
        r = []
        for k in range(i, len(l)):
            (l[i], l[k]) = (l[k], l[i])
            r = r + permutations_aux(l, i+1)
            (l[i], l[k]) = (l[k], l[i])
        return r

def permutations(l : list) -> list:
    '''renvoie la liste des permutations de s'''
    return permutations_aux(l, 0)

print(permutations(['a','b','c','d']))

def sont_anagrammes1(mot1 : str, mot2 : str) -> bool:
    '''teste si deux mots sont anagrammes'''
    l2 = string_to_list(mot2)
    for e in permutations(string_to_list(mot1)):
        if e == l2:
            return True
    return False

print(sont_anagrammes1('elvis', 'viles'))    
print(sont_anagrammes1('nettoyer', 'noyauter'))    

## une seconde méthode

def mot_to_dico(m : str) -> dict:
    '''renvoie le dictionnaire des nombres d'occurrences correspondant au mot m'''
    d = {}
    for e in m:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    return d

print(mot_to_dico('pingouin'))

def sont_anagrammes2(mot1 : str, mot2 : str) -> bool:
    '''teste si deux mots sont anagrammes'''
    return mot_to_dico(mot1) == mot_to_dico(mot2)

print(sont_anagrammes2('elvis', 'viles'))    
print(sont_anagrammes2('nettoyer', 'noyauter'))    
    

## une troisième méthode

def tri_liste(l : list) -> None:
    '''trie une liste'''
    l.sort()

def tri_mot(s : str) -> str:
    '''renvoie la version triée d'un mot'''
    l = string_to_list(s)
    tri_liste(l)
    return list_to_string(l)

def sont_anagrammes3(mot1 : str, mot2 : str) -> bool:
    '''teste si deux mots sont anagrammes'''
    return tri_mot(mot1) == tri_mot(mot2)
    
print(sont_anagrammes3('elvis', 'viles'))    
print(sont_anagrammes3('elvis', 'liles'))    

def chrono(f, mot1 : str, mot2 : str, n : int = 1000) -> None:
    '''affiche le temps moyen d'exécution de n répétitions de f, avec les paramètres mot1 et mot2'''
    t = process_time()
    for _ in range(n):
        f(mot1, mot2)
    print ((process_time() - t)/n)

chrono(sont_anagrammes1, 'elvis','viles', 10)
chrono(sont_anagrammes2, 'elvis','viles', 1000)
chrono(sont_anagrammes3, 'elvis','viles', 1000)
#chrono(sont_anagrammes1, 'elviselvis','vilesviles', 1)
chrono(sont_anagrammes2, 'elviselvis','vilesviles', 1000)
chrono(sont_anagrammes3, 'elviselvis','vilesviles', 1000)
chrono(sont_anagrammes2, 'elviselviselvis','vilesvilesviles', 1000)
chrono(sont_anagrammes3, 'elviselviselvis','vilesvilesviles', 1000)

## recherche de tous les anagrammes d'un mot donné

def liste_anagrammes1(liste_mots : list, mot1 : str) -> list:
    '''renvoie la liste des anagrammes de mot1 dans la liste de mot'''
    r = []
    mot1bis = enleve_diacritiques_majuscules(mot1)
    for mot2 in liste_mots:
        if sont_anagrammes2(mot1bis, enleve_diacritiques_majuscules(mot2)):
            r.append(mot2)
    return r
    
print(liste_anagrammes1(liste_mots, 'préparation'))
t = process_time(); liste_anagrammes1(liste_mots, 'préparation'); print(process_time()-t)
t = process_time(); liste_anagrammes1(liste_mots, 'pré'); print(process_time()-t)

def liste_mots_to_dict(l : list) -> dict:
    '''transforme une liste de mot en dictionnaire des anagrammes'''
    r = {}
    for mot in l:
        cle = tri_mot(enleve_diacritiques_majuscules(mot))
        if cle not in r:
            r[cle] = [mot]
        else:
            r[cle].append(mot)
    return r
    
dictionnaire = liste_mots_to_dict(liste_mots)    


def liste_anagrammes2(dictionnaire : dict, mot1 : str) -> list:
    '''renvoie la liste des anagrammes de mot1 en utilisant le dictionnaire prétraité'''
    return dictionnaire[tri_mot(enleve_diacritiques_majuscules(mot1))]
    
    
print(liste_anagrammes2(dictionnaire, 'alpine'))
print(liste_anagrammes2(dictionnaire, 'préparation'))
print(liste_anagrammes2(dictionnaire, 'Poire'))


def max_anagrammes(dictionnaire : dict) -> list:
    '''renvoie la plus grande liste de mots anagrammes les uns des autres 
    présente dans le dictionnaire'''
    r = 'a'
    for cle in dictionnaire:
        if len(dictionnaire[cle]) > len(dictionnaire[r]):
            r = cle
    return dictionnaire[r]

print(max_anagrammes(dictionnaire))

## anagrammes avec plusieurs mots

def sous_mot1(mot1 : str, mot2 : str) -> bool:
    '''teste si mot1 est un sous-mot de mot2'''
    d1 = mot_to_dico(mot1)
    d2 = mot_to_dico(mot2)
    for k in d1:
        if not k in d2:
            return False
        if d2[k] < d1[k]:
            return False
    return True
    
def premiere_occurrence(c : str, mot : str, j : int) -> int:
    '''renvoie l'indice de première occurrence de c dans mot à partir de la position j, 
    None s'il n'apparaît pas'''
    for i in range(j, len(mot)):
        if mot[i] == c:
            return i
    return None
    
def sous_mot2_aux(mot1 : str, mot2 : str, i1 : int, i2 : int) -> bool:
    '''teste si mot1[i1:] est un sous-mot de mot2[i2:], où les deux mots sont triés'''
    if i1 >= len(mot1):
        return True
    i = premiere_occurrence(mot1[i1], mot2, i2)
    if i == None:
        return False    
    return sous_mot2_aux(mot1, mot2, i1 + 1, i + 1)
    
def sous_mot2(mot1 : str, mot2 : str) -> bool:
    '''teste si mot1 est un sous-mot de mot2, où ces mots sont triés'''
    return sous_mot2_aux(mot1, mot2, 0, 0)
    
print (sous_mot1('voir','aurevoir'))
print (sous_mot2(tri_mot('voir'),tri_mot('aurevoir')))

print (sous_mot1('voirie','aurevoir'))
print (sous_mot2(tri_mot('voirie'),tri_mot('aurevoir')))


def chrono2(f, mot1 : str, mot2 : str) -> None:
    t = process_time()
    n = 10000
    for _ in range(n):
        f(mot1, mot2)
    print ((process_time() - t)/n)

mot1 = tri_mot('voirvoir')
mot2 = tri_mot('aurevoiraurevoir')
chrono2(sous_mot1, mot1, mot2)
chrono2(sous_mot2, mot1, mot2)
mot1 = tri_mot('voirievoirie')
mot2 = tri_mot('aurevoiraurevoir')
chrono2(sous_mot1, mot1, mot2)
chrono2(sous_mot2, mot1, mot2)


def soustrait(mot1 : str, mot2 : str) -> str:
    '''si mot1 est un sous-mot de mot2 et que ces mots sont triés, enlève de 
    mot2 les lettres de mot1 (avec leur nombre d'occurrences)'''
    r = ''
    i1 = 0
    i2 = 0
    while i1 < len(mot1):
        while i2 < len(mot2) and mot1[i1] != mot2[i2]:
            r = r + mot2[i2] #cplx
            i2 = i2 + 1
        i1 = i1 + 1
        i2 = i2 + 1    
    return r + mot2[i2:]
    
print(soustrait(tri_mot('voir'), tri_mot('aurevoir')))


##

def tous_anagrammes_liste(dictionnaire : dict, liste : list) -> list:
    '''si liste = [m1, ... mn] est une liste de mots triés, renvoie la
    liste de toutes les listes de la forme [m1', ... mn'] où mi' est un 
    anagramme de m_i apparaissant comme valeur du dictionnaire'''
    if liste == []:
        return [[]]
    mot = liste.pop()
    r = []
    for e in tous_anagrammes_liste(dictionnaire, liste):
        for m in dictionnaire[mot]:
            r.append(e+[m])
    return r

    
print(tous_anagrammes_liste(dictionnaire, ['aeiimnqstuu', 'fou', 'er']))

## Anagrammes de listes de mots

def anagramme_liste(dictionnaire : dict, accumulateur : list, reste : str, n : int) -> None:
    '''dernière question'''
    if n == 1:
        if reste in dictionnaire: 
            t = tous_anagrammes_liste(dictionnaire, accumulateur+[reste])
            for e in t:
                print(e)
        return
    for e in dictionnaire.keys():
        if sous_mot2(e, reste):
            s = soustrait(e, reste)
            accumulateur.append(e)
            anagramme_liste(dictionnaire, accumulateur, soustrait(e, reste), n-1)
            accumulateur.pop()

anagramme_liste(dictionnaire, [], tri_mot('informatique'), 3)

anagramme_liste(dictionnaire, [], tri_mot('informatiquepourtous'), 2)

anagramme_liste(dictionnaire, [], tri_mot('informatiquepourtous'), 3)



## Pour aller plus loin

def anagramme_liste(dictionnaire : dict, accumulateur : list, reste : str, n : int) -> None:
    '''version n'affichant que les listes triées par ordre lexicographique croissant des mots triés'''
    if n == 1:
        if reste in dictionnaire and not (len(accumulateur) >= 1 and reste < accumulateur[-1]): 
            t = tous_anagrammes_liste(dictionnaire, accumulateur+[reste])
            for e in t:
                print(e)
        return
    for e in dictionnaire.keys():
        if sous_mot2(e, reste):
            if len(accumulateur) >= 1 and e < accumulateur[-1]:
                continue 
            s = soustrait(e, reste)
            accumulateur.append(e)
            anagramme_liste(dictionnaire, accumulateur, soustrait(e, reste), n-1)
            accumulateur.pop()
