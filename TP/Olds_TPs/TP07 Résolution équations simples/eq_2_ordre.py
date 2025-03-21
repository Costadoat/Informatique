
#==============================================================================
# Resolution d une equation d ordre 2
#==============================================================================

from math import sqrt

a=0.1
b=0.6
c=0.9

if a==0: 
    #equation de degre 0
    if b==0: 
        if c==0: 
            print('Tout R est solution')
        else :
            print('Pas de solution')
    #equation de degre 1        
    else : 
        print('La solution est :'+str(-float(c)/b))  
#equation de degre 2        
else :
    D=float(b**2-4*a*c)
    if D==0:   
        print('L unique solution est :'+str(-float(b)/(2*a)))
    elif D>0:
        print('Les deux solutions reelles sont :'+str((-b+sqrt(D))/(2*a))+' et '+str((-b-sqrt(D))/(2*a)))
    else :
        z1=complex(-b,sqrt(-D))/(2*a)
        z2=complex(-b,-sqrt(-D))/(2*a)
        print('Les deux solutions complexes sont :'+str(z1)+' et '+ str(z2))
