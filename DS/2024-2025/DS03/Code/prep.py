import random
from PIL import Image

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

liste_lettres=[]
for lettrea in alphabet:
    for lettreb in alphabet:
        liste_lettres.append(lettrea+lettreb)

random.shuffle(liste_lettres)

image = Image.open("harry1.jpg")


lx,ly=image.size
dx,dy=12,12
sx,sy=lx//dx,ly//dy
i=random.randint(1, 10)
j=0
for x in range(dx):
    for y in range(dy):
        im_crop=image.crop((x*sx,y*sy,(x+1)*sx,(y+1)*sy))
        im_crop.save('boite/{}{:04d}.jpg'.format(liste_lettres[j],i), quality=95)
        i+=random.randint(1, 10)
        j+=1
        
image = Image.open("ninja.jpg")


lx,ly=image.size
dx,dy=12,12
sx,sy=lx//dx,ly//dy
i=1
for x in range(dx):
    for y in range(dy):
        im_crop=image.crop((x*sx,y*sy,(x+1)*sx,(y+1)*sy))
        im_crop.save('boite2/{:04d}.jpg'.format(i), quality=95)
        i+=1
        


