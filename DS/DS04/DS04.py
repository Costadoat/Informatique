import os
os.chdir('photos')

#Q1

def placeDuPoint(chaine):
    for i in range(len(chaine)):
        if chaine[i] == ".":
            return i

print(placeDuPoint('devoir.ipynb'))

#Q2

def coupeExtension(nom_fichier):
    id_point = placeDuPoint(nom_fichier)
    return nom_fichier[:id_point]
print(coupeExtension('devoir.ipynb'))

#Q3

def jpgTohtml(nom_fichier):
    nom_sans_extension = coupeExtension(nom_fichier)
    return nom_sans_extension + ".html"
print(jpgTohtml('photo.jpg'))

from exif import Image

def openImage(nom): #nom est une chaîne de caractère qui représente ici une photo
    with open (nom, 'rb') as imageFile:
        return Image(imageFile)
myimage = openImage('photo.jpg')

#Q4

def convertTodecimale(angle_tuple):
    degre, minutes, secondes = angle_tuple
    return degre + 1 / 60 * minutes +  1 / 3600 * secondes 
print(convertTodecimale((36,10,11.78)))

#Q5

def imageToGpsPoint(im):
    latitude = convertTodecimale(im.gps_latitude)
    if im.gps_latitude_ref == 'S':
        # la latitude est négative, on prend l'opposé
        latitude *= -1
    longitude = convertTodecimale(im.gps_longitude)
    if im.gps_longitude_ref == 'W':
        # la longitude est négative, on prend l'opposé
        longitude *= -1
    return (latitude, longitude)
print(imageToGpsPoint(myimage))

#Q6
listePhotos = ['photo{}.jpg'.format(k) for k in range(8)]

for photo in listePhotos:
    myimage = openImage(photo)
    print(imageToGpsPoint(myimage))

#Q7

lycee_dorian=[48.854411, 2.392279]

def calculDistance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**(1/2)
myimage = openImage('photo0.jpg')
print(calculDistance(imageToGpsPoint(myimage),lycee_dorian))

#Q8

distances=[]

for photo in listePhotos:
    my_image = openImage(photo)
    distances.append([photo,calculDistance(imageToGpsPoint(myimage),lycee_dorian)])

print(distances[0])   

#Q9

def tri_bulle(liste):
    # Parcours de 1 à la taille de la liste
    for i in range(1, len(liste)):
        # Parcours des éléments précédents
        for j in range(0, len(liste)-i):
            # On permutte les deux éléments successifs
            if liste[j][1] > liste[j+1][1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]

tri_bulle(distances)

print(distances)

#Q10

print('La photo prise la plus près est la {}.'.format(coupeExtension(distances[0][0])))
print('La photo prise la plus loin est la {}.'.format(coupeExtension(distances[-1][0])))

#Q11

def listeApresGouter(photos):
    avant_midi = []
    for photo in photos:
        my_image = openImage(photo)
        var_date = my_image.datetime
        heure = var_date[11:13]
        if heure > "17":
            avant_midi.append(photo)
    return avant_midi

print(listeApresGouter(listePhotos))

#Q12


def listAbsolutePath(directory):
    for dirpath,dirs,filenames in os.walk(directory):
        return sorted([os.path.abspath(os.path.join(dirpath, d)) for d in dirs])

os.chdir('Arboresence')

s=listAbsolutePath('Arboresence')[0]
print(s)


gr={'A':['B','D','E'],'B':['A','C','E'],'C':['B','D'],'D':['A','C','G'],'E':['A','B','F'],'F':['E','G'],'G':['D','F','H','I'],'H':['G','J'],'I':['G'],'J':['H']}

def parcoursLargeur(gr,s):
    files=[s]
    noeuds_decouverts=[s]
    while len(files)!=0:
        noeud_courant=files[0]
        files=files[1:]
        for voisin in gr[noeud_courant]:
            if voisin not in noeuds_decouverts:
                noeuds_decouverts.append(voisin)
                files.append(voisin)
    return(noeuds_decouverts)

print(parcoursLargeur(gr,'A'))


files=[s]
noeuds_decouverts=[s]
while len(files)!=0:
    noeud_courant=files[0]
    files=files[1:] 
    for voisin in listAbsolutePath(noeud_courant):
        if voisin not in noeuds_decouverts:
            noeuds_decouverts.append(voisin)
            files.append(voisin)

print(noeuds_decouverts)


chaine=''
for dir in noeuds_decouverts:
    chaine+=dir.split('/')[-1]

print(chaine)
