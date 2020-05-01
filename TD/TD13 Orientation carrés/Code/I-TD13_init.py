# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:10:07 2018

@author: Renaud
"""

from math import asin, pi, cos, sin
from PIL import Image, ImageDraw, ImageFont

def change(pt,pt0,angle):
    return pt0[0]+(pt[0]-pt0[0])*cos(angle)+(pt[1]-pt0[1])*sin(angle),pt0[1]-(pt[0]-pt0[0])*sin(angle)+(pt[1]-pt0[1])*cos(angle)


ratio=[1.,1.]
for image in range(8):
    angle=pi/2.-image*pi/12.
    im= Image.new('RGB',(1920,1080),color=(255,255,255,0))
    pix = im.load()
    size=im.size
    largeur0=int(size[0]/2.)
    longueur0=int(size[1]/2.)
    pt0=[largeur0,longueur0]
    e=300
    for i in range(largeur0-e,largeur0+e):
        for j in range(longueur0-e,longueur0+e):
            pix[change([i,j],pt0,angle)]=(0,144,255)   
    im.save(str(image)+'.jpg')