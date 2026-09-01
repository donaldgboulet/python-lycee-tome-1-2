"""
# ici on va apprendre  a utuliser la boucle pour et traiter des exercices avec
1- Premierement la boucle est la maniere la plus simple de repeter les informations
et en python on l'ecris en Anglais for

"""
# Exemple pour la boucle for afficher les valeur de 1 a 5 en utulisant cette boucle 
a = 0
for i in range(5):
    a +=1
    #print(a)
"""   
for i in range(10):
    if i >=1:
        print(i**2)
# parcourir une liste
for p in [2,3,5,7,11,13]:
    print(p**3)

# un programme qui calcule la somme des 20 prmier entiers naturels 0+1+1+2+.......+19+20

somme = 0 # initialisation de la variable somme a zero
for i in range(20): # la boucle for qui va parcourir toutes les 20 premiers nombres entiers naturels 
    somme += i # incrementer la somme pour une valaur de i bien precis 
    print(somme) # afficher

a= list(range(10))# afficher la liste de 0 a 9 dans un tableau 
print(a)
b= list(range(10,20))# parcourir les element  de 10 a 20 dans un tableau 
print(b)
c = list(range(0,20,5)) # Parcourir les element de 0 a 20 mais en faisant de pas 5 a 5
print(c)


# Laboucle imbrique
for i in[10,20,30,40,50]:
    for j in[3,7]:
        a = i+j
        print(a)
"""

"""
    #####################################
    #									#
    #									#
    #	Activite 4(La Boucle pour(for))	#
    #									#
    #####################################
1- L'objectifs est de construir des boucles simples en traitant des exercices
2- 

# Exercice 1)a de l'activite 4
# afficher les cubes entieres de 1 a 100
for i in range(0,101):
    print(i**3)

    
# Exercice 1)b de l'activite 4
# afficher les puissances quatriemes des entier entre 10 a 20
for i in range(10,21):
    print(i**4)

    
# Exercice 1)c de l'activite 4
# Afficher les racines carres entiers 0,5,10,15...100
from math import*
for i in range(0,101,5):
    print(sqrt(i))
    
# Exercice 2
for i in range(1,11):
    print(2**i)
"""
"""
# Exercice 3

for i in range(0,100):
    x = i /100
    y = x**3 - x**2  - (1/4)*x + 1
    print("pour x = ",x, " On a y = ",y)
"""

"""
from math import*
y_min = 999999   # on commence avec une valeur énorme
x_min = 0

for i in range(0,100):
    x = i / 100
    y = x**3 - x**2 - (1/4)*x + 1
    if y < y_min:        # si y est plus petit que ce qu'on a déjà...
        y_min = y              # que faut-il écrire ici ?
        x_min = x

print("Minimum :", y_min, "en x =", x_min)
    """


### __EXERCICE__4 ###
"""
Cherchons une valeur approche que dois avoir la rayon d'une boule sachant que son volume ets egale a 100
"""

from math import *

for i in range (1,300):
    R = i/100
    V = (4/3)*pi*R**3
    print("R = ", R, "V = ", V)
        
































