# Question 1

def f(x):
    return x**4-79*x**2-66*x+432

# Question 2

print(f(0))

# Question 3

for i in range(-10,11,1):
    if f(i)==0:
        print(i)
    elif  f(i)<0:
        print('-')
    else:
        print('+')

# Question 4:

semaine=3

if semaine%8==0:
    print("Colles de SI, d'Anglais et de Français")
elif semaine%2==0:
    print("Colles de SI et d'Anglais")
else:
    print("Colles de Math et de Physique")

# Question 5:

def colloscope(semaine):
    if semaine%8==0:
        return "Colles de SI, d'Anglais et de Français"
    elif semaine%2==0:
        return "Colles de SI et d'Anglais"
    else:
        return "Colles de Math et de Physique"

print(colloscope(4))
print(colloscope(8))
print(colloscope(9))

# Question 6:

def permuter(a,b):
    return(b,a)

def permuter(a,b): # Deuxième solution
    x=a
    a=b
    b=x
    return(a,b)


print(permuter(1,2))

# Question 7:

texte="Je fais souvent ce rêve étrange et pénétrant."

count=0
for lettre in texte:
    if lettre == 'e' or lettre == 'é' or lettre == 'ê':
        count=count+1
print(count)







