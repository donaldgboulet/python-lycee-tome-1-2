from random import *

mystere = randint(0, 99)

for i in range(7):
    reponse = int(input("Veuillez entrer un nombre entre 0 et 99 : "))
    
    if reponse == mystere:
        print("Bravo champion, c'est le bon nombre !")
        break
    elif reponse < mystere:
        print("Plus grand !")
    else:
        print("Plus petit !")
    
    # L'ordinateur triche — change le nombre mystère !
    mystere = mystere + randint(-3, 3)
    mystere = max(0, min(99, mystere))

else:
    print(f"Perdu ! Le nombre mystère était {mystere}")