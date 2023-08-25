#!/usr/bin/python
#    Test_personalite.py



questions1 = [("Votre talent tient dans vos", "super-pouvoirs", "ressources"),
    ("Un animal est pour vous un", "symbole", "truc pas pratique lorsqu'on part en vacances")]

result=''

for question in questions1:
    question_string = "%s:\n\ta. %s\n\tb. %s\n[a/b]:  " % (question[0], question[1], question[2])
    answer = input(question_string).lower()
    while answer not in ("a", "b"):
        print("Please choose A or B")
        answer = input(question_string).lower()
    result = result + answer

if result == 'aa':
    print('Vous etes Spiderman !')
elif  result == 'ab':
    print('Vous etes Superman !')
elif  result == 'ba':
    print('Vous etes Batman !')
else:
    print('Vous etes Iron man !')
