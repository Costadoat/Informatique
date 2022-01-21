file=open('resultats_1.txt','r')
contenu=file.read()
journees=contenu.split('\n\n')

liste_equipes=sorted(['Lyon','Reims','Dijon','Montpellier','Paris_FC','Guingamp','Saint_Étienne','Bordeaux','Soyaux',\
               'Issy','PSG','Fleury'])

resultats_equipes=[[equipe] for equipe in liste_equipes]

for journee in journees:
    matchs=journee.split('\n')
    for match in matchs:
        score=match.split(' : ')
        if len(score)>1:
            score=match.split(' : ')[1]
            equipes,score=score.split(' ')
            equipes=equipes.split('-')
            score=score.split('-')
            if score[0]>score[1]:
                points=[3,0]
            elif score[0]<score[1]:
                points=[0,3]
            else:
                points=[1,1]
            for i in range(2):
                resultats_equipes[liste_equipes.index(equipes[i])].append([str(points[i]),score[i],score[1-i]])

#print(resultats_equipes)

ligne=''
for equipe in resultats_equipes:
    ligne+=equipe[0]+';'
    for item in equipe[1:]:
        ligne+=':'.join(item)+';'
    ligne+='\n'

file=open('resultats.csv','w')
file.write(ligne)
file.close()
