print "Question 14:"

# il faut initialiser toutes les grandeurs utilisees ensuite dans le code
periode=180 # en secondes
temps=[] 
vitesse=[]
y0=0 
a=0.02 # en m/s²
v0=2.5 # en m/s

for i in range(5):
    for k in range(periode/2):
        temps.append(i*periode+k)
        vitesse.append(v0*3.6) # 3.6 pour conversion m/s --> km/h
    for k in range(periode/2):
        temps.append(i*periode+k+periode/2)
        vitesse.append((v0+a*k)*3.6) # idem

# Question 15
def F(t):
    return vitesse[temps.index(t)]  # on recupere la vitesse qui correspond au temps
                                    # temps.index(t) est utile si t0 est different de 0

# Question 16    
def methode_euler(F,y0,t):
    y = [0]*len(t)
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i]+(t[i+1]-t[i])*F(t[i])/3.6 # conversion de la vitesse 
                                                # km/h --> m/s puisque le temps
                                                # est en secondes
    return y

# Question 17
position=methode_euler(F,y0,temps)  # il faut appeler une fonction si on veut utliser
                                    # ce qu'elle renvoie
print position[-1] #la distance totale parcourue est la dernière distance calculee

# Question 18
plt.plot(temps,vitesse)

# Question 19

plt.plot(temps,position)
plt.show()
