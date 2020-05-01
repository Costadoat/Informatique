import pygame
import matplotlib.pyplot as plt
from pygame.locals import *
import random, math, sys
pygame.init()

Surface = pygame.display.set_mode((1600,600))

Circles = []
nb_malades=[]
nb_malades_index=0
class Circle:
    def __init__(self,couleur):
##        self.radius = int(random.random()*50) + 1
        self.radius = 20
        self.x = random.randint(self.radius, 800-self.radius)
        self.y = random.randint(self.radius, 600-self.radius)
        self.speedx = 0.2*(random.random()+1.0)
        self.speedy = 0.2*(random.random()+1.0)
##        self.mass = math.sqrt(self.radius)
        self.color=couleur
        self.temps_malade=0

nb_personnes=30
Circles.append(Circle((150,0,0)))
for x in range(nb_personnes-1):
    Circles.append(Circle((0,150,0)))

def CountSeek(C):
    i=0
    for cone in C:
        if cone.color==(150,0,0):
            i+=1
    return i

def CircleCollide(C1,C2):
    if C1.color== (150,0,0) and C2.color!=(0,0,150):
        C2.color= (150,0,0)
    if C2.color== (150,0,0) and C1.color!=(0,0,150):
        C1.color= (150,0,0)
    C1Speed = math.sqrt((C1.speedx**2)+(C1.speedy**2))
    XDiff = -(C1.x-C2.x)
    YDiff = -(C1.y-C2.y)
    if XDiff > 0:
        if YDiff > 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
        elif YDiff < 0:
            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
            XSpeed = -C1Speed*math.cos(math.radians(Angle))
            YSpeed = -C1Speed*math.sin(math.radians(Angle))
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180
        XSpeed = C1Speed*math.cos(math.radians(Angle))
        YSpeed = C1Speed*math.sin(math.radians(Angle))
    C1.speedx = XSpeed
    C1.speedy = YSpeed
def Move(nb):
    for Circle in Circles[:nb]:
        Circle.x += Circle.speedx
        Circle.y += Circle.speedy

def CollisionDetect():
    for Circle in Circles:
        if Circle.x < Circle.radius or Circle.x > 800-Circle.radius:    Circle.speedx *= -1
        if Circle.y < Circle.radius or Circle.y > 600-Circle.radius:    Circle.speedy *= -1
    for Circle in Circles:
        for Circle2 in Circles:
            if Circle != Circle2:
                if math.sqrt(  ((Circle.x-Circle2.x)**2)  +  ((Circle.y-Circle2.y)**2)  ) <= (Circle.radius+Circle2.radius):
                    CircleCollide(Circle,Circle2)

def Draw():
    Surface.fill((255,255,255))
    for Circle in Circles:
        pygame.draw.circle(Surface,Circle.color,(int(Circle.x),int(600-Circle.y)),Circle.radius)
        if Circle.color==(150,0,0):
            Circle.temps_malade+=1
            if Circle.temps_malade==2000:
                Circle.temps_malade=0
                Circle.color=(0,0,150)
    if nb_malades_index  % 10 == 0:
        nb_malades.append(CountSeek(Circles))
    for i,malade in enumerate(nb_malades):
        pygame.draw.line(Surface, (150,0,0), (int(i/10)+900,595-malade*10), (int(i/10)+900,600-malade*10), 3)
    pygame.display.flip()
    return CountSeek(Circles)

def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()
def main():
    t=0
    while t<8000:
        t+=1
        GetInput()
        Move(10)
        CollisionDetect()
        Draw()

if __name__ == '__main__': main()
