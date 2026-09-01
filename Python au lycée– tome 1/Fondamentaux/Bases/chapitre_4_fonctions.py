
"""
Chapitre 4 - Fonctions
Activite 1 : Ecrire des fonctions simples
"""

# --- Fonction sans parametre ni sortie ---

def affiche_table_de_7():
    """Affiche la table de multiplication par 7."""
    for i in range(1, 11):
        print(i, "* 7 =", i * 7)

def affiche_bonjour():
    """Demande le prenom et affiche un bonjour personnalise."""
    prenom = input("Veuillez entrer votre prenom : ")
    print("Bonjour", prenom)


# --- Fonction avec parametre et sans sortie ---

def affiche_une_table(n):
    """Affiche la table de multiplication par n."""
    for i in range(1, 11):
        print(i, "*", n, "=", i * n)

def affiche_salutation(formule):
    """Affiche une salutation personnalisee selon la formule donnee."""
    prenom = input("Veuillez entrer votre prenom : ")
    print(formule, prenom)


# --- Fonction sans parametre et avec sortie ---

def demande_prenom_nom():
    """Demande prenom et nom, renvoie l'identite complete (nom en majuscule)."""
    prenom = input("Veuillez entrer votre prenom : ")
    nom = input("Veuillez entrer votre nom : ")
    return nom.upper() + " " + prenom


# --- Tests1 ---
#affiche_table_de_7()
#affiche_bonjour()
#affiche_une_table(5)
#affiche_salutation("Coucou !")
#print(demande_prenom_nom())

"""
Activite 2 : Construire des fonctions avec différents types d'entrée et de sortie
"""
from math import pi


# 1. Trinômes

def trinome_1(x):
    """Renvoie la valeur du trinôme 3x² - 7x + 4."""
    return 3*x**2 - 7*x + 4

def trinome_2(a, b, c, x):
    """Renvoie la valeur du trinôme ax² + bx + c."""
    return a*x**2 + b*x + c


# 2. Devises

def conversion_euros_vers_dollars(montant):
    """Convertit un montant en euros vers les dollars (1€ = 1.15$)."""
    return montant * 1.15

def conversion_euros(montant, devise):
    """Convertit un montant en euros vers la devise choisie."""
    if devise == "dollars":
        return montant * 1.15
    elif devise == "livre":
        return montant * 0.81
    elif devise == "yens":
        return montant * 130
    elif devise == "fcfa":
        return montant * 655


# 3. Volumes

def volume_cube(a):
    """Renvoie le volume d'un cube de côté a."""
    return a**3

def volume_boule(r):
    """Renvoie le volume d'une boule de rayon r."""
    return (4/3) * pi * r**3

def volume_cylindre(r, h):
    """Renvoie le volume d'un cylindre de rayon r et hauteur h."""
    return pi * r**2 * h

def volume_boite(L, l, h):
    """Renvoie le volume d'une boîte de dimensions L, l, h."""
    return L * l * h


# 4. Périmètres et aires

def perimetre_aire_rectangle(a, b):
    """Renvoie le périmètre et l'aire d'un rectangle de dimensions a et b."""
    return 2 * (a + b), a * b

def perimetre_aire_disque(r):
    """Renvoie le périmètre et l'aire d'un disque de rayon r."""
    return 2 * pi * r, pi * r**2

# Trouver à partir de quel rayon l'aire dépasse le périmètre
for rayon in range(0, 30):
    P, A = perimetre_aire_disque(rayon / 10)
    if A > P:
        print("À partir du rayon", rayon / 10, "l'aire est plus grande que le périmètre.")
        break
"""    
# --- Tests2 ---
print(trinome_1(7))           # doit afficher 102
print(trinome_2(2, -1, 0, 6)) # doit afficher 66
print(conversion_euros_vers_dollars(100))  # doit afficher 115.0
print(conversion_euros(100, "livre"))      # doit afficher 81.0
print(volume_cube(3))         # doit afficher 27
print(volume_boule(3))        # doit afficher ~113.1
print(perimetre_aire_rectangle(5, 10))     # doit afficher (30, 50)
print(perimetre_aire_disque(5))            # doit afficher (~31.4, ~78.5)
"""



"""
                        Activité 3 (Tortue)
Objectifs : définir quelques fonctions qui dessinent des figures géométriques. Créer une fonction est
similaire à créer un bloc avec Scratch.

"""
from turtle import*
#color("red")
color("green")
#color("blue")
#color("darkviolet")
width(5)

def triangle():
    for i in range(3):
        forward(200)
        left(120)
        
def carre():
    for i in range(4):
        forward(200)
        left(90)

def  hexagone(longueur):
    for i in range(6):
        forward(longueur)
        left(60)
        
def polygone(n,longueur):
    for i in range(n):
        N = 360/n
        forward(longueur)
        left(N)
       
#triangle()
#carre()
#hexagone(200)
#polygone(5,200)
ht()
done()

 
 
 
#        Activité 4 (Toujours des fonctions)
#        Objectifs : créer de nouvelles fonctions

# __________1_______
# A
def reduction(age):
    # Attribution directe du pourcentage avec l'opérateur =
    if age < 10:
        valeur_reduction = 50
    elif age <= 18:  
        valeur_reduction = 30
    elif age >= 60:
        valeur_reduction = 20
    else:
        valeur_reduction = 0
    return valeur_reduction 
    #print(f"Votre réduction est de {valeur_reduction}%")

# B
def montant(tarif_normal, age):
    pourcentage_reduit = reduction(age)
    tarif_reduit = tarif_normal*(1-pourcentage_reduit/100)
    return tarif_reduit


# --- RÉSOLUTION DE L'EXERCICE ---

# 1. Calcul du billet pour l'enfant de 9 ans (Tarif: 30€)
billet_enfant = montant(30, 9)

# 2. Calcul pour les jumeaux de 16 ans (Tarif: 20€ chacun -> donc 2 billets)
billet_jumeau1 = montant(20, 16)
billet_jumeau2 = montant(20, 16)

# 3. Calcul pour les parents de 40 ans (Tarif: 35€ chacun -> donc 2 billets)
billet_parent1 = montant(35, 40)
billet_parent2 = montant(35, 40)

# 4. Calcul du montant total
total_famille = billet_enfant + billet_jumeau1 + billet_jumeau2 + billet_parent1 + billet_parent2

    
# --- AFFICHAGE DES RÉSULTATS ---
print(f"Prix billet enfant : {billet_enfant} €")
print(f"Prix billet un jumeau : {billet_jumeau1} €")
print(f"Prix billet un parent : {billet_parent1} €")
print("-" * 53)
print(f"Le montant total payé par la famille est de : {total_famille} €")




import random 

# =_=_=_=A_=_=_=
# Cette fonction ne fait QUE vérifier si un calcul est juste.
# Elle a besoin de recevoir a, b et la réponse pour travailler.
def calcul_est_exact(a, b, reponse):
    if reponse == a * b:
        return True
    else:
        return False

# =_=_=_=B_=_=_=
def test_multiplication(lang):
    # 1. On génère les nombres aléatoires directement dans le jeu
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    
    # 2. Pose de la question et récupération de la réponse selon la langue
    if lang == "francais":
        reponse_utilisateur = input(f"Combien font {a} x {b} ? : ")
    elif lang == "anglais":
        reponse_utilisateur = input(f"How much is {a} x {b} ? : ")
    elif lang == "Deutsch":
        reponse_utilisateur = input(f"Wie viel ist {a} x {b} ? : ")
    else:
        print("Langue non supportée / Language not supported")
        return False

    # 3. Conversion du texte de l'utilisateur en nombre entier
    reponse_num = int(reponse_utilisateur)

    # 4. On envoie les données à la fonction A pour avoir le verdict
    est_correct = calcul_est_exact(a, b, reponse_num)

    # 5. Affichage du verdict selon la langue
    if lang == "francais":
        if est_correct:
            print("Bravo ! C'est exact.")
        else:
            print(f"Faux ! La bonne réponse était {a * b}.")
            
    elif lang == "anglais":
        if est_correct:
            print("Well done! That's correct.")
        else:
            print(f"Wrong! The correct answer was {a * b}.")
            
    elif lang == "Deutsch":
        if est_correct:
            print("Super! Das ist richtig.")
        else:
            print(f"Oh nein! Die richtige Antwort war {a * b}.")
            
    # 6. Retourne le résultat (True ou False)
    return est_correct

# Exemple de test
test_multiplication("Deutsch")

# _________ACTIVITE5_______

"""
Activité 5 (Égalité expérimentale).
Objectifs : utiliser l’ordinateur pour expérimenter des égalités de fonctions."""

from math import*
#1.a)
def valeur_absolue(x):
    if x >=0:
        return x
    else :
        return -x
    
print(valeur_absolue(-5))

#1.b)
def  racine_du_carre(x):
    return sqrt(x**2)

print(racine_du_carre(-5))


#1.c)
def deux_fonctions_egales():

    for i in range(-100,101):
        a = abs(i)
        b = sqrt(i**2)
        if a != b:
            print("a different de b ")
            break
    else :
        print("Elles sont egales")
        
deux_fonctions_egales()



#2.a)
def  F1(a,b):
    return (a+b)**2

def  F2(a,b):
    return a**2+2*a*b+b**2
print(F1(5,5))
print(F2(5,5))

#2.b)
egales = True
for i in range(-100,101):
    for j in range(-100,101):
        if (i+j)**2 != i**2+2*i*j+j**2:
            egales = False
if egales:
    print("Les deux fonctions sont egales")
else:
    print("Les deux fonctions ne sont pas egales ")
    
#2.c)
egales = True
for i in range(-100,101):
    for j in range(-100,101):
        if (i-j)**3 != i**3 - 3*i**2*j - 3*i*j**2 + j**3:
            egales = False
if egales:
    print("Les deux fonctions sont egales ")
else:
    print("Les deux fonctions ne sont pas egales ")
        
    
egales = True
for i in range(-100,101):
    for j in range(-100,101):
        if (i-j)**3 != i**3 - 3*i**2*j + 3*i*j**2- j**3:
            egales = False
if egales:
    print("Les deux fonctions sont egales ")
else:
    print("Les deux fonctions ne sont pas egales ")
    
    
    
    
#3.a)
def sincos(x):
    return	(sin(x))**2 + (cos(x))**2

def un(x):
    return 1

def verifie():
    egales = True
    for x in range(-100,101):
        if sincos(x) != un(x):
            egales = False
    if egales:
        print("Les deux fonctions  sont egales ")
      
    else:
        print("Les deux fonctions ne sont pas egales")

#verifie()


# 3.b)
epsilon = 0.00001
egales = True
for i in range(-100,101):
    if abs(sincos(i) - un(i)) > epsilon:
        egales = False
if egales :
    print("f et g sont expérimentalement approximativement égales  ")
else :
    print("f et g ne sont pas expérimentalement approximativement égales  ")
    
# 3.c)
epsilon = 0.00001
egales = True
for i in range(-100,101):
    if abs( sin(2*i) - 2*sin(i)*cos(i)) > epsilon:
        egales = False
if egales:
    print("Les deux fonctions sont egales")
else :
    print("Les deux fontions ne sont pas egales ")
    
    
epsilon = 0.00001
egales = True
for i in range(-100,101):
    if abs(cos((pi/2)-i)- sin(i))>epsilon:
        egales = False
if egales:
    print("Les deux fonctions sont egales")
else :
    print("Les deux fontions ne sont pas egales ")


#3.d)
def g1(x):
    return sin(pi*x)
def g2(x):
    return 0
def verifie_1():
    epsilon = 0.00001
    egales = True
    for x in range(-100,101):
        if abs(g1(x) - g2(x))>epsilon:
            egales = False
    if egales:
        print("Les deux fonctions  sont egales ")
      
    else:
        print("Les deux fonctions ne sont pas egales")

verifie_1()
print("Test avec x = 0.5 :")
print("g1(0.5) =", g1(0.5))   # va afficher 1.0 (ou presque)
print("g2(0.5) =", g2(0.5))   # va afficher 0









        
        
    

    
    
    
    
    
    





