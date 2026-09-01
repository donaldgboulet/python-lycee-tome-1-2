# Activité 3 (Chiffres d’un nombre)
"""
Objectifs : trouver des nombres dont les chiffres vérifient certaines propriétés
"""
# 1. Le programme suivant affiche tous les entiers de 0 à 99. Comprends ce programme.
# Que représentent les variables u et d ?
for d in range(10):
    for u in range(10):
        n = 10*d+u
        print(n)
        
        
# 2.  Trouve tous les entiers compris entre 0 et 999 qui vérifient toutes les propriétés suivantes
#• l’entier se termine par 3,
#• la somme des chiffres est supérieure ou égale à 15,
#• le chiffre des dizaines est pair


compteur = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            l = 100*i+10*j+k
            
            # somme des chiffres
            somme_des_chiffres = i+j+k
            if k == 3 and j%2 ==0 and somme_des_chiffres>=15:
                print(l)
                compteur = compteur + 1
print("Le nombre total des compteurs sont : ", compteur)





