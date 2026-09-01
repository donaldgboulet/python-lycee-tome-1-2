"""
Pour compliquer le jeu, l’ordinateur a le droit de mentir de temps en temps. Par exemple environ une
fois sur quatre l’ordinateur donne la mauvaise indication « plus grand » ou « plus petit ».
Indications. Pour décider quand l’ordinateur ment, à chaque tour tire un nombre au hasard entre 1 et
4, si c’est 4 l’ordinateur ment!
"""
from random import *

mystere = randint(0, 99)

for i in range(7):
    reponse = int(input("Veuillez entrer un nombre entre 0 et 99 : "))
    
    tirage = randint(1, 4)  # 1 chance sur 4 de mentir
    
    if reponse == mystere:
        print("Bravo champion, c'est le bon nombre !")
        break
    elif reponse < mystere:  # vérité = plus grand
        if tirage == 4:      # ment → dit plus petit
            print("Plus petit !")
        else:                # dit la vérité
            print("Plus grand !")
    else:                    # vérité = plus petit
        if tirage == 4:      # ment → dit plus grand
            print("Plus grand !")
        else:                # dit la vérité
            print("Plus petit !")
else:
    print(f"Perdu ! Le nombre mystère était {mystere}")