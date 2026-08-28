""" #####################################
    #									#
    #	Notion de variable et de comment#
    #	comment afficher une variable   #
    #									#
    #####################################
1- Variable
2- les commentaires qui commence par ' et ne sont pas execute par python et permet
   d'expliquer le programme 
3- et donner des noms tres clairs aux variables
4- Python distingue des majuscules des miniscules

"""


a = 3 # la variable a
b = 5 # la variable b

#print("La somme vaut: ", a+b) # calculer et afficher la somme de a et b
#print(" Le profuit vaut: ", a*b) # calculer le produit de a et b et afficher le resultat

c = a**b # une nouvelle variable qui carcule a puissance ou exposant b
#print(" a exposant b vaut: ",c) # Et on affiche le resultat


#################################
#								#
#	calculer l'aire du	triangle#
#								#
#################################

base = 8
hauteur = 3
aire = (base*hauteur)/2
#print("Aire du Triangle est egale a : ",aire)
# NameError: print(Aire) # name 'Aire' is not defined Aire est different de aire



#################################
#								#
#	Reaffectation 				#
#								#
#################################

s = 1000
s = s+100
s = s+200
s = s - 50
#print("La valeur actuelle de s ets :",s)

#################################
#								#
#	Activite 2(Variables)		#
#objectif:utuliser les variables#
#								#
#################################

"""1: A- calculer l'aire de trapez
"""
H = 3 # hauteur
b = 4 # Petite_Base
B = 7 # Grande_Base
aire = ((B+b)*H)/2
print("Aire de la Trapeze vaut : ", aire)

"""1: B- calculer le Volume de la Boite a la fomre de parralepipede 
"""
L = 10
l = 8
H = 3

volume = L*l*H
print("le Volume du parraleppede vaut :", volume)

"""1: C- calculer l'aire du disque 
"""
PI = 3.14
R  = 10
Aire = PI*R**2
print("L'aire du disque vaut :",Aire)


"""2:  remet les ligne dans l'ordre pour que a la sortie x vaut 6
"""
x = 7
y = 2*x
y = y-1
x = x+3*y
print(x)

"""3:  calculer le capital des trois premiere annees 
"""
A	= 1000 # Le capital place sur le compte de l'epargne
A	= A*1.10
A	= A*1.10
A	= A*1.10
print("Le capital de la troissieme annee vaut :", A)


"""4:  echanger la valeur de la variable a et la variable b pour que a la fin
chaque variable prends la variable de l'autres


"""
a = 9
b = 11

c = a
a = b
b = c
print(a)
print(b)





