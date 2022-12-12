### Donnée ###    
def distance(lieu1, lieu2):
    return ((lieu1[0]-lieu2[0])**2+(lieu1[1]-lieu2[1])**2)**(1/2)

# Question 6:
dorian=['0','74 Av. Philippe Auguste',[48.854576520866964, 2.3926308459105954],0]
print(distance(dorian[2],compteurs[0][2]))
