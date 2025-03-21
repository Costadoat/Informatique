import json
import numpy as np

file=open('centres_efs.csv','r')
contenu=file.read()
file.close()
lignes=contenu.split('\n')

centres=[]
for idx,ligne in enumerate(lignes[1:-2]):
    lieu={}
    data=ligne.split(';')
    lieu['adresse']=data[1]
    adresse=data[2].split(' ')
    if len(adresse)>1:
        lieu['code_postal']=data[2].split(' ')[0]
        lieu['ville']=' '.join(data[2].split(' ')[1:])
    else:
        lieu['code_postal']=''
        lieu['ville']=''
    lieu['nom']=data[3]
    lieu['sang']=data[5]
    lieu['plasma']=data[6]
    lieu['plaquettes']=data[7]
    lieu['latitude']=float(data[10])
    lieu['longitude']=float(data[11])
    lieu['location_regionName']=data[16]
    lieu['date']=data[26]
    lieu['debut_am']=data[33]
    lieu['fin_am']=data[32]
    lieu['debut_pm']=data[35]
    lieu['fin_pm']=data[34]
    centres.append(lieu)

json_object = json.dumps(centres, indent=4)
 
# Writing to sample.json
with open("centres_efs.json", "w") as outfile:
    outfile.write(json_object)
    
with open('centres_efs.json', 'r') as openfile:
 
    # Reading from json file
    liste_des_centres = json.load(openfile)


def distance(coords1,coords2):
    return np.sqrt((coords1[0]-coords2[0])**2+(coords1[1]-coords2[1])**2)

coordonnees_dorian=[48.854787,2.393162]

plus_proches=10*[[0,1000]]
for idx,centre in enumerate(liste_des_centres):
    coordonnees_centre=[centre['latitude'],centre['longitude']]
    dist=distance(coordonnees_centre,coordonnees_dorian)
    rang=0
    while dist>plus_proches[rang][1] and rang < len(plus_proches)-1:
        rang+=1
    if rang < len(plus_proches):
        for i in range(len(plus_proches)-1,rang,-1):
            plus_proches[i]=plus_proches[i-1]
        plus_proches[rang]=[idx,dist]

for plus_proche in plus_proches:
    print(liste_des_centres[plus_proche[0]])
