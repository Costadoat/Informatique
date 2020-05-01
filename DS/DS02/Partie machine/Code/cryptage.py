##################### PREPARATION ENONCE #####################
alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
message_decode='C EST UN BON DEBUT'
n=5

message_code=''
for lettre in message_decode:
    if lettre!=' ':
        i=alphabet.index(lettre)
        message_code+=alphabet[(i+n)%26]
    else:
        message_code+=' '
    
print(message_code)

clef_a='ABCDEFGHIJKLMNOPQRSTUVWXYZ \n'
clef_b='FQBMXITEPALWHSDOZKVGRCNYJU \n'

fichier=open('message_analyse.txt','r')
message=fichier.read().lower().replace(',','').replace(';','').replace('.','')\
         .replace('!','').replace('?','').replace('ù','u').replace("'"," ")\
         .replace('-',' ').replace('î','i').replace('ï','i')\
         .replace('ê','e').replace('è','e').replace('é','e')\
         .replace('à','a').replace('â','a').replace('ô','o')\
         .replace(':',' ').replace('û','u').upper()
fichier.close()
message_code=''
for lettre in message:
    #print(lettre)
    i=clef_a.index(lettre)
    message_code+=clef_b[i]

fichier2=open('message_analyse2.txt','w')
fichier2.write(message)
fichier2.close()


compteur=[0 for i in range(len(clef_a))]
for lettre in message:
    i=clef_a.index(lettre)
    compteur[i]+=1
total=0

liste_max=[]
liste_stat=[]
for i in range(len(clef_a)-2):
    m=0
    for i,total in enumerate(compteur):
        if total>m and clef_a[i] not in liste_max:
            m=total
            max=i        
    liste_max.append(clef_a[max])
    liste_stat.append('%.02f'% (100*m/len(message)))

truc=[' ', 'E', 'S', 'A', 'I', 'L', 'R', 'T', 'N', 'U', 'O', '\n', 'M', 'D', 'C', 'V', 'P', 'H', 'B', 'Q', 'F', 'J', 'G', 'Y', 'X', 'Z']
stat=['16.36', '13.93', '6.99', '6.89', '5.93', '5.83', '5.22', '5.12', '5.07', '4.91', '4.26', '3.19', '2.79', '2.53', '2.48', '1.62', '1.22', '1.11', '1.01', '0.91', '0.66', '0.61', '0.61', '0.46', '0.15', '0.10']
print(truc[:15])
print(liste_max[:15])
print(liste_stat[:15])

lim=15
liste_stat = ''.join(truc[:lim])
print(liste_stat)
##################### PREPARATION ENONCE #####################

