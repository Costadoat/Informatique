# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 14:08:20 2017

@author: costa
"""
import random
import unicodedata
liste_pays=['Afghanistan','Albanie','Antarctique','Algérie','Samoa Américaines','Andorre','Angola','Antigua-et-Barbuda','Azerbaïdjan','Argentine','Australie','Autriche','Bahamas','Bahreïn','Bangladesh','Arménie','Barbade','Belgique','Bermudes','Bhoutan','Bolivie','Bosnie-Herzégovine','Botswana','Île Bouvet','Brésil','Belize','Territoire Britannique de l\'Océan Indien','Îles Salomon','Îles Vierges Britanniques','Brunéi Darussalam','Bulgarie','Myanmar','Burundi','Bélarus','Cambodge','Cameroun','Canada','Cap-vert','Îles Caïmanes','République Centrafricaine','Sri Lanka','Tchad','Chili','Chine','Taïwan','Île Christmas','Îles Cocos (Keeling)','Colombie','Comores','Mayotte','République du Congo','République Démocratique du Congo','Îles Cook','Costa Rica','Croatie','Cuba','Chypre','République Tchèque','Bénin','Danemark','Dominique','République Dominicaine','Équateur','El Salvador','Guinée Équatoriale','Éthiopie','Érythrée','Estonie','Îles Féroé','Îles (malvinas) Falkland','Géorgie du Sud et les Îles Sandwich du Sud','Fidji','Finlande','Îles Åland','France','Guyane Française','Polynésie Française','Terres Australes Françaises','Djibouti','Gabon','Géorgie','Gambie','Territoire Palestinien Occupé','Allemagne','Ghana','Gibraltar','Kiribati','Grèce','Groenland','Grenade','Guadeloupe','Guam','Guatemala','Guinée','Guyana','Haïti','Îles Heard et Mcdonald','Saint-Siège (état de la Cité du Vatican)','Honduras','Hong-Kong','Hongrie','Islande','Inde','Indonésie','République Islamique d\'Iran','Iraq','Irlande','Israël','Italie','Côte d\'Ivoire','Jamaïque','Japon','Kazakhstan','Jordanie','Kenya','République Populaire Démocratique de Corée','République de Corée','Koweït','Kirghizistan','République Démocratique Populaire Lao','Liban','Lesotho','Lettonie','Libéria','Jamahiriya Arabe Libyenne','Liechtenstein','Lituanie','Luxembourg','Macao','Madagascar','Malawi','Malaisie','Maldives','Mali','Malte','Martinique','Mauritanie','Maurice','Mexique','Monaco','Mongolie','République de Moldova','Montserrat','Maroc','Mozambique','Oman','Namibie','Nauru','Népal','Pays-Bas','Antilles Néerlandaises','Aruba','Nouvelle-Calédonie','Vanuatu','Nouvelle-Zélande','Nicaragua','Niger','Nigéria','Niué','Île Norfolk','Norvège','Îles Mariannes du Nord','Îles Mineures Éloignées des États-Unis','États Fédérés de Micronésie','Îles Marshall','Palaos','Pakistan','Panama','Papouasie-Nouvelle-Guinée','Paraguay','Pérou','Philippines','Pitcairn','Pologne','Portugal','Guinée-Bissau','Timor-Leste','Porto Rico','Qatar','Réunion','Roumanie','Fédération de Russie','Rwanda','Sainte-Hélène','Saint-Kitts-et-Nevis','Anguilla','Sainte-Lucie','Saint-Pierre-et-Miquelon','Saint-Vincent-et-les Grenadines','Saint-Marin','Sao Tomé-et-Principe','Arabie Saoudite','Sénégal','Seychelles','Sierra Leone','Singapour','Slovaquie','Viet Nam','Slovénie','Somalie','Afrique du Sud','Zimbabwe','Espagne','Sahara Occidental','Soudan','Suriname','Svalbard etÎle Jan Mayen','Swaziland','Suède','Suisse','République Arabe Syrienne','Tadjikistan','Thaïlande','Togo','Tokelau','Tonga','Trinité-et-Tobago','Émirats Arabes Unis','Tunisie','Turquie','Turkménistan','Îles Turks et Caïques','Tuvalu','Ouganda','Ukraine','L\'ex-République Yougoslave de Macédoine','Égypte','Royaume-Uni','Île de Man','République-Unie de Tanzanie','États-Unis','Îles Vierges des États-Unis','Burkina Faso','Uruguay','Ouzbékistan','Venezuela','Wallis et Futuna','Samoa','Yémen','Serbie-et-Monténégro','Zambie']
nombrealeatoire = random.randint(0,len(liste_pays))

mot_init=liste_pays[nombrealeatoire]
mot = mot_init.lower()
mot1 = unicode(mot,'utf-8')
mot2 = unicodedata.normalize('NFD', mot1).encode('ascii', 'ignore') 
mot = mot2.lower()

test=[0]*len(mot)
jocker=3
no=[]
util=''

for i in range(len(mot)):
    if mot[i]==' ' or mot[i]=="'" or mot[i]=='-' :
        test[i]=1


def gen_mot_affiche(mot,test):
    mot_affiche=''
    for i in range(len(mot)):
        if test[i]==1:
            mot_affiche+=mot[i]
        else:
            mot_affiche+='*'
    return mot_affiche
            
while test!=[1]*len(mot) and jocker>0:
    if len(no)!=0:
        util='Lettres absentes: '
        for let in no:
            util+=let+' '
    print gen_mot_affiche(mot,test), 'Jocker={}'.format(jocker),util
    lettre=raw_input('Nouvelle lettre:')
    a=0
    i=0
    while a<len(mot):
        if (lettre in mot[a:]) and lettre!="":
            a=mot[a:].index(lettre)+a
            test[a]=1
            a+=1
            i=1
        elif i==0:
            jocker-=1
            if lettre!="":
                no.append(lettre)
            a=len(mot)+1
        else:
            a=len(mot)+1
    gen_mot_affiche(mot,test)

if test==[1]*len(mot):
    print 'Gagné !, c\'était {}'.format(mot_init) 
            
if jocker==0:
    print 'Perdu !, c\'était {}'.format(mot_init)