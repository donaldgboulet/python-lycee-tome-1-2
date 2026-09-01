# Le nombre mystere

"""
Objectifs : coder le jeu incontournable lorsque l’on apprend à programmer. L’ordinateur choisit un
nombre au hasard. L’utilisateur doit deviner ce nombre en suivant des indications « plus grand »
ou «plus petit » données par l’ordinateur. Comme ce jeu est vite lassant, on introduit des variantes
où l’ordinateur a le droit de mentir ou de tricher!
"""
from random import *

mystere = randint(0, 99)

for i in range(7):
    reponse = int(input("Ton nombre : "))
    
    if reponse < mystere:
        print("Oh zut, le nombre à trouver est plus grand !")
    elif reponse > mystere:
        print("Oh non, le nombre à trouver est plus petit !")
    else:
        print("Bravo champion, c'est le bon nombre !")
        break
else:
    print(f"Perdu ! Le nombre mystère était {mystere}")
        
    
    
    