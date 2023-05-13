import json
 
# Opening JSON file
with open('liste-et-localisation-des-musees-de-france.json') as json_file:
    musees = json.load(json_file)

c=0
for musee in musees:
    if musee['departement']=='Paris':
        c+=1
    if 'chasse' in musee['nom_officiel_du_musee'].lower() and musee['departement']=='Paris':
            print(musee['nom_officiel_du_musee'],musee['adresse'])
    if musee['identifiant_museofile']=='M0077':
        print(musee['nom_officiel_du_musee'], musee['commune'])

print('Il y a {} musées à Paris.'.format(c))
