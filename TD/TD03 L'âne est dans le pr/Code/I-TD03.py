import numpy as np
import matplotlib.pyplot as plt

n_larg=200
n_long=200
c=20

pre=np.zeros([n_larg,n_long])
def manger(x,y):
    for i in range(n_larg):
        for j in range(n_long):
            if ((x-i)**2+(y-j)**2)**(1/2.)<=c:
                if pre[i,j]<2:
                    pre[i,j]+=1

def parcours(e):
    x,y=c,c
    while x<n_larg-c:
        while y<n_long-c:
            manger(x,y)
            y+=e
        x+=e
        y=c

def parcours_q(e):
    x,y=c,c
    while x<n_larg-c:
        while y<n_long-c:
            manger(x,y)
            y+=e
        x+=e/2
        if ((x-c)//(e/2))%2==0:
            y=c
        else:
            y=c+e/2

def trace(x1,y1,x2,y2):
    plt.plot([0,n_larg,n_larg,0,0],[0,0,n_long,n_long,0],color='pink')
    plt.scatter(x1,y1,s=1,color='green')
    plt.scatter(x2,y2,s=1,color='red')
    plt.axis('equal')
    plt.xlim(0, n_long)
    plt.ylim(0, n_larg)
    plt.show()

def pourcent(k,x1,x2):
    if k==1:
        return len(x1)/(n_long*n_larg)
    if k==2:
        return len(x2)/(n_long*n_larg)

def analyse(yes_plot):
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    for i,ligne in enumerate(pre):
        for j,valeur in enumerate(ligne):
            if valeur==1.0:
                x1.append(i)
                y1.append(j)
            elif valeur==2.0:
                x2.append(i)
                y2.append(j)
    if yes_plot:
        trace(x1,y1,x2,y2)
    return 1-pourcent(1,x1,x2)-pourcent(2,x1,x2)


for e in np.arange(45,45,0.1):
    pre=np.zeros([n_larg,n_long])
    parcours_q(e)
    print(e,int((n_larg-2*c)/e)+1,analyse(0))

e=45.5
pre=np.zeros([n_larg,n_long])
parcours_q(e)
print(e,int((n_larg-2*c)/e)+1,analyse(1))
