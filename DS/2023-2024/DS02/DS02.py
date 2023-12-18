# Question 1:
import matplotlib.pyplot as plt
file=open('production-solaire-eolienne.csv','r')
contenu=file.read()
file.close()
lignes=contenu.split('\n')
print(lignes[:2])

# Question 2:
print(lignes[1].split(';'))

# Question 3:
journee=[]
for ligne in lignes:
    data=ligne.split(';')
    if data[0]=='2022-12-01':
        journee.append(data)
#print(journee)

# Question 4:
def get_journee(date):
    journee=[]
    for ligne in lignes:
        data=ligne.split(';')
        if data[0]==date:
            journee.append(data)
    return journee
#print(get_journee('2022-12-01'))

# Question 5:
jour_eolien=[]
jour_solaire=[]
journee=get_journee('2022-12-01')
for i in range(24):
    for heure in journee:
        if i==int(heure[1][:2]):
            jour_eolien.append(int(heure[2]))
            jour_solaire.append(int(heure[3]))

#print(jour_eolien, jour_solaire)

# Question 6:            
plt.plot(jour_eolien, label='Eolien')
plt.plot(jour_solaire, label='Solaire')
plt.xticks(range(24))
plt.legend()
plt.show()

# Question 7: 
jours_eolien=[[],[]]
jours_solaire=[[],[]]
dates=['2022-08-15','2022-12-01']
for id_jour in range(2):
    journee=get_journee(dates[id_jour])
    for id_heure in range(24):
        for heure in journee:
            if id_heure==int(heure[1][:2]):
                jours_eolien[id_jour].append(int(heure[2]))
                jours_solaire[id_jour].append(int(heure[3]))

    plt.plot(jours_eolien[id_jour], label='Eolien '+dates[id_jour])
    plt.plot(jours_solaire[id_jour], label='Solaire '+dates[id_jour])

plt.xticks(range(24))
plt.legend()
plt.show()

# Question 8: 
mois_eolien=[0]*12
mois_solaire=[0]*12
for ligne in lignes:
    data=ligne.split(';')
    if data[0][:4]=='2022':
        if data[2]:
            mois_eolien[int(data[0][5:7])-1]+=int(data[2])
        if data[3]:
            mois_solaire[int(data[0][5:7])-1]+=int(data[3])

print(mois_e
# Question 9: 
plt.bar([i+1 for i in range(12)],mois_eolien, label='Eolien')
plt.bar([i+1 for i in range(12)],mois_solaire, label='Solaire')
plt.xticks(range(12),labels=[i+1 for i in range(12)])
plt.legend()
plt.show()
        
