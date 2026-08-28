""" #####################################
    #									#
    #									#
    #Construire des boucles compliques	#
    #									#
    #####################################
1- Utuliser des boucle plus complique 
2- 
3- 
4-
"""
## __ ACTIVITE 5___ ##

#1 Definir une variable n(par exemple n = 20) et calculer la somme

def calcul_somme():
    somme = 0 # initialisation du compteur d'accumulation de la somme pour le garder en memoire 
    n = 20 # definir la variable n et luis affeczer une valeur possible
    for i in range(n+1): # la boucle pour qui va permettre de calculer la somme des carres des 20 premieres termes 
        somme +=i**2 # iteration du compteur ici on calcule la sommes des carres 
    print(somme) # et on l'affiche
#calcul_somme() # appeler la fonction afin de l'executer 

# 2 caculer le produit des 19 premier nombre entier naturel
def calcul_produit(): 
    n = 19
    produit= 1
    for i in range(1,n+1,2):
        produit *=i
    print(produit)
#calcul_produit()
        
# Afficher les tables de multiplications entre 1 et 10       
def table_multiplication():
    n = 10
    m = 10
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i, "x",j, "=", i*j)
table_multiplication()
        
    
        

