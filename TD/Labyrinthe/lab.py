#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from random import choice, randrange as rand
import matplotlib.pyplot as plt
import copy
    
##
# Dimensions du labyrinthe
width = 20
height = 20
 
##
# Constantes servant à décrire les directions des passages
N, S, E, W  = 1, 2, 4, 8
IN          = 0x10
FRONTIER    = 0x20
OPPOSITE    = {E: W, W: E, S: N, N: S}

##
# Structures de données
grid = [([0] * width) for _ in range(height)]
frontier = set()

##
# Méthodes utilitaires
def add_frontier(x, y):
    if (x >= 0 and y >= 0 and y < len(grid)
            and x < len(grid[y]) and grid[y][x] == 0):
        grid[y][x] |= FRONTIER
        frontier.add((x, y))
 
 
def mark(x, y):
    grid[y][x] |= IN
    add_frontier(x-1, y)
    add_frontier(x+1, y)
    add_frontier(x, y-1)
    add_frontier(x, y+1)
 
 
def neighbors(x, y):
    if x > 0 and (grid[y][x-1] & IN):
        yield (x-1, y)
    if x + 1 < len(grid[y]) and (grid[y][x+1] & IN):
        yield (x+1, y)
    if y > 0 and (grid[y-1][x] & IN):
        yield (x, y-1)
    if y + 1 < len(grid) and (grid[y+1][x] & IN):
        yield (x, y+1)
 
 
def direction(fx, fy, tx, ty):
    return {(fx < tx): E,
            (fx > tx): W,
            (fy < ty): S,
            (fy > ty): N}[True]
 
 
def is_empty(cell):
    return cell == 0 or cell == FRONTIER

def display_plt():
    plt.text(2,5*height-2,'D')
    plt.text(5*width-3,2,'A')
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell&N==0:
                plt.plot([5*x,5*x+5],[5*height-(5*y),5*height-(5*y)],'b')
            if cell&S==0:
                plt.plot([5*x,5*x+5],[5*height-(5*y+5),5*height-(5*y+5)],'b')
            if cell&E==0:
                plt.plot([5*x+5,5*x+5],[5*height-(5*y+5),5*height-(5*y)],'b')
            if cell&W==0:
                plt.plot([5*x,5*x],[5*height-(5*y+5),5*height-(5*y)],'b')
    plt.axis('equal')
    
def choice_dir(x,y):
    list_dir=[N,S,E,W]
    for test in parcours:
        if test[0]==(x,y):
            if test[1] in list_dir:
                list_dir.remove(test[1])
    return(list_dir)
                    

def generation_grille():
    mark(rand(width), rand(height))
    while frontier:
        ##
        # Choix d'un voisin à la frontière
        x, y = choice(list(frontier))
        frontier.remove((x, y))
        nx, ny = choice(list(neighbors(x, y)))
 
        ##
        # Création d'un passage
        dir = direction(x, y, nx, ny)
        grid[y][x] |= dir
        grid[ny][nx] |= OPPOSITE[dir]
 
        mark(x, y)
         
        ## DEBUG :
        # print("frontier =", frontier)
        # print("(%d, %d) -> (%d, %d)" % (x, y, nx, ny))
        # display_maze()
        # input("Appuyez sur Entree pour continuer")


def test_grille():
    i=0
    x,y=0,0
    parcours=[]
    grid_parcours = [([0] * width) for _ in range(height)]
    grid_parcours[0][0]=1
    while (x,y)!=(width-1,height-1):
        test_case=(grid[y][x]&N)+(grid[y][x]&S)+(grid[y][x]&E)+(grid[y][x]&W)
        if test_case in [N,S,E,W]:
            banni.append([x,y,test_case])
        i+=1
        parcours.append([x,y])
        idee=choice([N,S,E,W])
        if idee==E and grid[y][x]&E!=0 and (x+1,y) not in banni:
            x+=1
        elif idee==S and grid[y][x]&S!=0 and (x,y+1) not in banni:
            y+=1
        elif idee==W and grid[y][x]&W!=0 and (x-1,y) not in banni:
            x+=-1
        elif idee==N and grid[y][x]&N!=0 and (x,y-1) not in banni:
            y+=-1
        grid_parcours[y][x]=1
    parcours.append([x,y])
    #plt.scatter([5*ban[0]+2.5 for ban in banni],[5*height-(5*ban[1]+2.5) for ban in banni])
    return(parcours)

def mise_a_jour_grille():
    for ban in banni[1:]:
        if [ban[0],ban[1]] not in traite and (ban[0],ban[1])!=(0,0):
            if ban[2]==N and ban[1]>0:
                traite.append([ban[0],ban[1]])
                grid[ban[1]][ban[0]] +=- ban[2]
                grid[ban[1]-1][ban[0]] +=- OPPOSITE[ban[2]]
            elif ban[2]==S and ban[1]<height-1:
                traite.append([ban[0],ban[1]])
                grid[ban[1]][ban[0]] +=- ban[2]
                grid[ban[1]+1][ban[0]] +=- OPPOSITE[ban[2]]
            if ban[2]==E and ban[0]<width-1:
                traite.append([ban[0],ban[1]])
                grid[ban[1]][ban[0]] +=- ban[2]
                grid[ban[1]][ban[0]+1] +=- OPPOSITE[ban[2]]
            if ban[2]==W and ban[0]>0:
                traite.append([ban[0],ban[1]])
                grid[ban[1]][ban[0]] +=- ban[2]
                grid[ban[1]][ban[0]-1] +=- OPPOSITE[ban[2]]

plt.figure('Initial')

generation_grille()
grid_init=copy.deepcopy(grid)
display_plt()

for i in range(50):
    print('Essai '+str(i))
    banni=[]
    parcours=test_grille()
    if i in [0]:
        plt.figure('Essai '+str(i))
        plt.plot([5*par[0]+2.5 for par in parcours],[5*height-(5*par[1]+2.5) for par in parcours],'r')
        display_plt()
    traite=[]
    mise_a_jour_grille()


plt.figure('Final')
grid=copy.deepcopy(grid_init)
display_plt()
plt.plot([5*par[0]+2.5 for par in parcours],[5*height-(5*par[1]+2.5) for par in parcours],'r')

plt.show()

