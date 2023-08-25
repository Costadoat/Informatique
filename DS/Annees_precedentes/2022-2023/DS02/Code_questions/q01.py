# Question 1:
file_in=open('comptage-velo-donnees-compteurs_light.csv','r')
contenu=file_in.read()
file_in.close()
lignes=contenu.split('\n')
print(lignes[0])
print(lignes[1])
