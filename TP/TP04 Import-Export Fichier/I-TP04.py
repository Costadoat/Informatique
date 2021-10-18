# coding: utf-8
import matplotlib.pyplot as plt
import math as m

file=open('temperature-quotidienne-departementale.csv','r')
contenu=file.read()
file.close()

dep='75'
year='2018'

lignes=contenu.split('\n')
temperatures=[]
print(lignes[0])
for ligne in lignes[1:]:
    data=ligne.split(';')
    if data[0][1:5]==year and data[1]==dep:
        temperatures.append([data[0][1:-1],float(data[5][1:-1])])

print(temperatures[0])
file2=open('fichier_export.csv','w')
for date,temp in temperatures:
    file2.write(date+';'+str(temp)+'\n')
file2.close()

# Recherche du min
min=temperatures[0][1]
max=temperatures[0][1]
for date,temp in temperatures:
    if temp<min:
        min=temp
    if temp>max:
        max=temp
print(min,max)

# Calcul de la moyenne
t_total=0
for date,temp in temperatures:
    t_total+=temp
t_moy=t_total/len(temperatures)

print(t_moy)

# Calculer la médiane
temperatures_classe=sorted(temperatures)
print(temperatures_classe[len(temperatures)//2])

# Calcul de l'écart type
sigma=0
for date,temp in temperatures:
    sigma+=(temp-t_moy)**2
sigma=m.sqrt(sigma/len(temperatures))
print(sigma)

# Tracer un histogramme
plt.hist([temp for date,temp in temperatures],range=(-4,30),bins=34)
plt.show()

# Faire pour 2018, 2019, 2020

fig = plt.figure()
for num,year in enumerate(['2018','2019','2020']):
    temperatures=[]
    for ligne in lignes[1:]:
        data=ligne.split(';')
        if data[0][1:5]==year and data[1]==dep:
            temperatures.append([data[0][1:-1],float(data[5][1:-1])])

    # Calcul de la moyenne
    t_total=0
    for date,temp in temperatures:
        t_total+=temp
    t_moy=t_total/len(temperatures)

    
    # Calculer la médiane
    temperatures_classe=sorted([temp for date,temp in temperatures])
    t_med=temperatures_classe[len(temperatures)//2]

    # Calcul de l'écart type
    sigma=0
    for date,temp in temperatures:
        sigma+=(temp-t_moy)**2
    sigma=m.sqrt(sigma/len(temperatures))

    print("Pour l'année {} dans le {} :\n - La moyenne est {:.2f}\n - La médiane est {:.2f}\n - L'écart type est {:.2f}".format(year,dep,t_moy,t_med,sigma))

    # Tracer un histogramme
    ax = fig.add_subplot(3,1,num+1)
    ax.hist([temp for date,temp in temperatures],range=(-4,30),bins=34)

plt.show()


