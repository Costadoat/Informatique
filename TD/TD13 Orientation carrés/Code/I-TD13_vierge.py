# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:24:55 2018

@author: Renaud
"""

from math import asin, pi, cos, sin
from PIL import Image, ImageDraw, ImageFont

    
for image in range(4):
    im = Image.open(str(image)+'.jpg')
    pix = im.load()
    size=im.size
    print pix[size[0]/2.,size[1]/2.]
    largeur0=int(size[0]/2.)
    longueur0=int(size[1]/2.)
    e=20
    for i in range(largeur0-e,largeur0+e):
        for j in range(longueur0-e,longueur0+e):
            pix[i,j]=(255,0,0)   
    im.save('Copie '+str(image)+'.jpg')