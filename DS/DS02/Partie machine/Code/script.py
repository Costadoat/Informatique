import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Question 1:
    
fichier=open('source1.csv','r')
contenu=fichier.read()
fichier.close()

lignes=contenu.split('\n')

print(lignes[0:2])

# Question 2:

data=lignes[1].split(",")
jour_test = datetime.strptime(data[0], '"%Y-%m-%d"')
taux_incidence=float(data[1])
taux_positivite=float(data[4])
print(jour_test,taux_incidence,taux_positivite)

# Question 3:

population=67000000
nb_tests=int((100*taux_incidence*population/100000)/taux_positivite)
print(nb_tests)

# Question 4:

dates_tests1=[]
nb_tests1=[]
for ligne in lignes[1:-1]:
    data=ligne.split(",")
    jour_test = datetime.strptime(data[0], '"%Y-%m-%d"')
    dates_tests1.append(jour_test)
    taux_incidence=float(data[1])
    taux_positivite=float(data[4])
    nb_test_positifs=float(data[1])*population/100000
    nb_tests=(100*taux_incidence*population/100000)/taux_positivite
    nb_tests1.append(int(nb_tests))

# Question 5:

plt.plot(dates_tests1,nb_tests1)

# Question 6:

fichier_test=open('source2.csv','r')
contenu=fichier_test.read()
fichier_test.close()

lignes=contenu.split('\n')

print(lignes[0:2])

# Question 7:

dates_tests2=[]
nb_tests2=[]
for ligne in lignes[1:-1]:
    data=ligne.split(";")
    if data[8]=='0':
        sem=data[1][-2:]
        jour_test = datetime(2020, 1, 1)+timedelta(weeks=int(sem))
        dates_tests2.append(jour_test)
        nb_tests=int(data[7])
        nb_tests2.append(nb_tests)

# Question 8:

#plt.figure(1)
#plt.plot(dates_tests2,nb_tests2)
#plt.show()

# Question 9:

dates_tests2=[]
nb_tests2=[]
for ligne in lignes[1:-1]:
    data=ligne.split(";")
    if data[8]=='0':
        sem=data[1][-2:]
        jour_test = datetime(2019, 12, 29)+timedelta(weeks=int(sem))
        dates_tests2.append(jour_test)
        nb_tests=int(data[7])
        nb_tests2.append(nb_tests)

plt.figure(1)
plt.plot(dates_tests2,nb_tests2)
plt.show()

# Question 10:

dates_ecarts=[]
ecarts=[]
for i,date in enumerate(dates_tests2):
     if date in dates_tests1:
         dates_ecarts.append(date)
         ecarts.append(nb_tests2[i]-nb_tests1[dates_tests1.index(date)])

# Question 11:

plt.figure(2)
plt.plot(dates_ecarts,ecarts)
plt.show()

# Question 12:

def get_max(liste):
    maximum=abs(liste[0])
    for valeur in liste:
        if abs(valeur)>maximum:
            maximum=abs(valeur)
    return maximum

# Question 13:

print('Nb écarts',get_max(ecarts))
print('Nb tests',get_max(nb_tests1))

print('Erreur relative pourcent',100*get_max(ecarts)/get_max(nb_tests1))
