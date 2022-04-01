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

liste_mots = charger_liste_mots('/.../listemotsfrancais.txt')

## conversions

def string_to_list(s : str) -> list:
    '''convertit une chaîne de caractères en liste de caractères'''
    pass

def list_to_string(l : list) -> str:
    '''convertit une liste de caractères en chaîne'''
    pass

## une bien mauvaise méthode...

def permutations_aux(l : list, i : int) -> list:
    '''renvoie la liste des permutations de l laissant fixes les éléments d'indices strictement inférieurs à i'''
    pass

def permutations(l : list) -> list:
    '''renvoie la liste des permutations de s'''
    pass

def sont_anagrammes1(mot1 : str, mot2 : str) -> bool:
    '''teste si deux mots sont anagrammes'''
    pass

## une seconde méthode

def mot_to_dico(m : str) -> dict:
    '''renvoie le dictionnaire des nombres d'occurrences correspondant au mot m'''
    pass

def sont_anagrammes2(mot1 : str, mot2 : str) -> bool:
    '''teste si deux mots sont anagrammes'''
    pass    

## une troisième méthode

def tri_liste(l : list) -> None:
    '''trie une liste'''
    pass

def tri_mot(s : str) -> str:
    '''renvoie la version triée d'un mot'''
    pass

def sont_anagrammes3(mot1 : str, mot2 : str) -> bool:
    '''teste si deux mots sont anagrammes'''
    pass

def chrono(f, mot1 : str, mot2 : str, n : int = 1000) -> None:
    '''affiche le temps moyen d'exécution de n répétitions de f, avec les paramètres mot1 et mot2'''
    pass

## recherche de tous les anagrammes d'un mot donné

def liste_anagrammes1(liste_mots : list, mot1 : str) -> list:
    '''renvoie la liste des anagrammes de mot1 dans la liste de mot'''
    pass

def liste_mots_to_dict(l : list) -> dict:
    '''transforme une liste de mot en dictionnaire des anagrammes'''
    pass

dictionnaire = liste_mots_to_dict(liste_mots)    


def liste_anagrammes2(dictionnaire : dict, mot1 : str) -> list:
    '''renvoie la liste des anagrammes de mot1 en utilisant le dictionnaire prétraité'''
    pass

def max_anagrammes(dictionnaire : dict) -> list:
    '''renvoie la plus grande liste de mots anagrammes les uns des autres 
    présente dans le dictionnaire'''
    pass

## anagrammes avec plusieurs mots

def sous_mot1(mot1 : str, mot2 : str) -> bool:
    '''teste si mot1 est un sous-mot de mot2'''
    pass

    
def premiere_occurrence(c : str, mot : str, j : int) -> int:
    '''renvoie l'indice de première occurrence de c dans mot à partir de la position j, 
    None s'il n'apparaît pas'''
    pass

    
def sous_mot2_aux(mot1 : str, mot2 : str, i1 : int, i2 : int) -> bool:
    '''teste si mot1[i1:] est un sous-mot de mot2[i2:], où les deux mots sont triés'''
    pass

    
def sous_mot2(mot1 : str, mot2 : str) -> bool:
    '''teste si mot1 est un sous-mot de mot2, où ces mots sont triés'''
    pass


def soustrait(mot1 : str, mot2 : str) -> str:
    '''si mot1 est un sous-mot de mot2 et que ces mots sont triés, enlève de 
    mot2 les lettres de mot1 (avec leur nombre d'occurrences)'''
    pass


##

def tous_anagrammes_liste(dictionnaire : dict, liste : list) -> list:
    '''si liste = [m1, ... mn] est une liste de mots triés, renvoie la
    liste de toutes les listes de la forme [m1', ... mn'] où mi' est un 
    anagramme de m_i apparaissant comme valeur du dictionnaire'''
    pass


## Anagrammes de listes de mots

def anagramme_liste(dictionnaire : dict, accumulateur : list, reste : str, n : int) -> None:
    '''dernière question'''
    pass
