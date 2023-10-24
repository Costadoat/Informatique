for mois in ['07','08']:
    fichier_in=open('synop.2022'+mois+'.csv','r')
    fichier_out=open('synop.2022'+mois+'01.csv','w')
    contenu=fichier_in.read()
    fichier_in.close()
    lignes=contenu.split('\n')
    entetes=lignes[0]
    fichier_out.write(entetes+'\n')
    data=lignes[1:-1]
    for idx,donnees_jour in enumerate(data):
        data_jour=donnees_jour.split(';')
        if data_jour[1][8:]=='000000':
            fichier_out.write(donnees_jour+'\n')
    fichier_out.close()
