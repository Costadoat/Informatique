import matplotlib.pyplot as plt
import numpy as np
import random

##########################################Préparation du fichier#######################################
t1=np.arange(0,2.4,0.01)
t2=np.arange(2.41,2.9,0.01)
t3=np.arange(2.91,3.4,0.01)
t4=np.arange(3.41,23.9,0.01)
t5=np.arange(23.91,24.4,0.01)
t6=np.arange(24.41,24.9,0.01)
t7=np.arange(24.91,30,0.01)
t=np.concatenate((t1,t2,t3,t4,t5,t6,t7))

accmax=2.5
accmin=2.5

acc1=np.zeros(len(t1))
acc2=(t2-t2[0])*accmax/(t2[-1]-t2[0])
acc3=-(t3-t3[-1])*accmax/(t3[-1]-t3[0])
acc4=t4*0.
acc5=-(t5-t5[0])*accmin/(t5[-1]-t5[0])
acc6=(t6-t6[-1])*accmin/(t6[-1]-t6[0])
acc7=t7*0.
acc=np.concatenate((acc1,acc2,acc3,acc4,acc5,acc6,acc7))
for i in range(len(acc)):
	acc[i]=acc[i]+(random.random()-0.5)*0.1	

fichier1=open('data.csv','w')
for i in range(len(t)):
        ligne=str(t[i])+";"+str(acc[i])+"\n"
        if i<2:
                print(ligne)
        fichier1.write(ligne)

fichier1.close()
##########################################Fin préparation du fichier#######################################

fichier=open('data.csv','r')
contenu=fichier.read()
lignes=contenu.split('\n')
temps=[]
acceleration=[]

for ligne in lignes[1:-1]:
	temps.append(float(ligne.split(";")[0]))
	acceleration.append(float(ligne.split(";")[1]))

plt.figure(1)
plt.plot(temps,acceleration)
plt.savefig('figure1.png')
#plt.show()

def integration_num(t,f,init):
        fi=[init]
        for i in range(1,len(f)):
                fi.append(fi[i-1]+f[i]*(t[i]-t[i-1]))
        return fi

vitesse=integration_num(temps,acceleration,0)
position=integration_num(temps,vitesse,0)
plt.figure(2)
plt.plot(temps,position)
plt.savefig('figure2.png')
#plt.show()
print(position[-1]/3.)

def index_temps(t,data_temps):
        i=0
        while data_temps[i]<t:
                i=i+1
        return i

def a(t):
        return acceleration[index_temps(t,temps)]

def methode_euler(F,y0,t):
        y = [0]*len(t)
        y[0] = y0
        for i in range(len(t)-1):
                y[i+1] = y[i]+(t[i+1]-t[i])*F(t[i])
        return y

v_list=methode_euler(a,0,temps)

def v(t):
        return v_list[index_temps(t,temps)]

p_list=methode_euler(v,0,temps)
plt.figure(3)
plt.plot(temps,position)
plt.plot(temps,p_list)
plt.savefig('figure3.png')
#plt.show()

def p(t):
        return p_list[index_temps(t,temps)]

def p2(t):
        return p(t)-12.

def methode_Newton(f,df,a,p) :
        x0=a
        while abs(f(x0))>p : # ou abs(e)>p
                x1=x0-f(x0)/df(x0)
                e=x1-x0
                x0=x1
        return x1

print(methode_Newton(p2,v,5,10**(-2)))
