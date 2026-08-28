""" #####################################
    #									#
    #									#
    #	LES FONCTIONS EN PYTHON 		#
    #									#
    #####################################
1- La fonction print()
2- importer le module math avec "import math*" pour utuliser tous les fonctions mathematiques 
3- 
4- 

# 1. __ la fonction print()__
print("Coucou Claire cava ?")
chaine  = "Je voulais just te saluer et demander comment tu allais mais ca saute aux yeux 😄 "
print(chaine)


# 3- __ Importer le module math qui va ous prmetrre d'utuliser tous les fonctions mathematiques 
from math import* # la ligne ci importe le module math pour pouvoir utulsier la fonction 

x = sqrt(6) #la ligne ci calcule la racine care ed 6 
print(x) # et on affiche la racine carre de 6
print(x**2) # ici on calcule la racine de 6 au carre


# 4. __Les fonctions Trigonometriques__
angle = pi/2
print(angle)
print(sin(angle)) #  afficher le sinus de l'angle pi sur 2
print(cos(angle)) # afficher le cosinus de l'angle pi sur 2
print(pi) # afficher la valeur approche de la constance pi 
print(round(pi)) # permet d'arrandir a l'entier le plus proche 
print(round(cos(angle))) # affichere et arrandir le cosinus de l'angle pi sur 2
print(ceil(1.2)) # renvoir l'entieur quiest supprerieur et le plus proche 
print(floor(1.9))# renvoir l'entire inferieur le plus proche
"""


"""
    ####################################
    #									#
    #									#
    #	Exercice sur les  FONCTIONS 	#
    #			EN PYTHON 				#
    #####################################

"""
# Activite 3 a pour objectif d'utuliser les fonctions de p<thon et le module math

## Exercice_1 ##
from math import*  # on importe la fontion maths
"""
a = 10403
b = 10506
pgcd = gcd(a,b)
c = a*b
ppcm  = (c)/(pgcd)
print(pgcd) # greatest common division(gcd)
print(ppcm) # afficher la plus petit commun multiple ntre a et b


## Exercice_1 ## cette fois ci en utulisant une fonction definis par l'utulisateur "def"

def pgcd():
    a = 10403
    b = 10506
pgcd = gcd(a,b)
print(pgcd)
def ppcm():
    a = 10403
    b = 10506
    c = a*b
ppcm = (c / pgcd)
print(ppcm)

"""

### __EXERCICE__2 ###
"""le but de l'exercice est de trouver pat tatonnement le nombre
reel x qui verifie tout eles operations suivantes """
x =3.9
print(abs(x**2 - 15))
print(round(2*x))
print(floor(3*x))
print(ceil(4*x))

### __EXERCICE3__###
""" En utulisant la formule trigonometrique cos(x)**2 + sin(x)**2 = 1
on dois verifie que pour pi sur 7 cette formules est numeriqument vrai """

x = pi/7
y = cos(x)**2 + sin(x)**2
resultat = y
print(floor(resultat))






    







