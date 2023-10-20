alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
message_code='H JXY ZS GTS IJGZY'
n=-5

message_decode=''
for lettre in message_code:
    if lettre!=' ':
        i=alphabet.index(lettre)
        message_decode+=alphabet[(i+n)%26]
    else:
        message_decode+=' '
    
print(message_decode)

fichier=open('message_code.txt','r')
message_code=fichier.read()
fichier.close()

print(message_code[:90])


fichier=open('message_analyse.txt','r')
message_analyse=fichier.read()
fichier.close()

clef_a='ABCDEFGHIJKLMNOPQRSTUVWXYZ \n'
clef_b="-------------------------- \n"

def analyse_texte(texte):
    compteur=[0 for i in range(len(clef_a))]
    for lettre in texte:
        i=clef_a.index(lettre)
        compteur[i]+=1
    print(compteur)

    liste_triee_occurences=[]
    liste_stat=[]
    for i in range(len(clef_a)-2):
        m=0
        for i,total in enumerate(compteur):
            if total>m and clef_a[i] not in liste_triee_occurences:
                m=total
                max=i
        liste_triee_occurences.append(clef_a[max])
        liste_stat.append('%.01f'% (100*m/len(message_analyse)))
    return liste_triee_occurences, liste_stat

liste_triee_occurences, liste_stat=analyse_texte(message_analyse)
print(liste_triee_occurences[:15], liste_stat[:15])
liste_triee_occurences, liste_stat=analyse_texte(message_code)
print(liste_triee_occurences[:15], liste_stat[:15])

liste_stat=' ESAILRTNUO\nMDC'

clef_decode=''
for lettre in clef_a:
    if lettre in liste_stat:
        i=liste_stat.index(lettre)
        lettre=liste_triee_occurences[i]
    else:
        lettre='-'
    clef_decode+=lettre

print(clef_a)
print(clef_decode)

clef_b='F-BMX---P--WHSD--KVGR----- \n'
#clef_b='FQBMXITEPALWHSDOZKVGRCNYJU \n'

def decodage_texte(message,clef_a,clef_b):
    message_decode=''
    for lettre in message_code:
        if lettre in clef_b:
            i=clef_b.index(lettre)
            lettre=clef_a[i]
        message_decode+=lettre
    return message_decode

#print(decodage_texte(message_code,clef_a,clef_b))
