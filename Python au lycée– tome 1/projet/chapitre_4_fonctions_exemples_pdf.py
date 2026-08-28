

"""
- Activite 1 # Le but est d'ecrire des focntions tres simples 
"""
#fonction 1
# Fonction sans parametre ni sortie

def affiche_table_de_7():
    for i in range(1, 13):
        print(i, "* 7 =", i * 7)
          
def affiche_bonjour():
    prenom = input("Veuillez entrezvotre prenom SVP !!!:")
    print(f"Bonjour",prenom)


#fonction 2
# Fonction avec avec un parametre et sans sortie

def affiche_une_table(n):
        for i in range(0,13):
            for j in [n] :
                k = i*j
            print(i,"*",j,"=",k)
    


def affiche_salutation(formule):
    prenom = input("Veuillez entrezvotre prenom SVP !!!:")
    print(formule,prenom)
    
# Fonction sans parametre et avec sortie
def demande_prenom_nom():
    prenom = input("Veuillez entrez votre prenom SVP !!!:")
    nom = input("Veuillez entrez votre Nom SVP !!!:")
    return nom.upper() + " " + prenom.lower()
    
#affiche_table_de_7()    
#affiche_bonjour() 
#affiche_une_table(5)
#affiche_salutation("Coucou!")
#print(demande_prenom_nom())



"""
- Activite 2 # Le but est  construire des fonctions
    avec différents types d’entrée et de sortie
"""
# 1 Trinômes
#a
def trinomes_1(x):
    r = 3*x**2 -7*x +4
    return r
#b
def trinome_2(a,b,c,x):
    s = a*x**2 +b*x +c
    return s
  
#print(trinomes_1(5))
#print(trinome_2(2,-1,0,6))


# 2 Devise
#a
def conversion_euros_vers_dollars(montant):
    dollars = montant * 1.15
    return dollars
     
#print(conversion_euros_vers_dollars(500))
    
# b
def conversion_euros(montant,devise):
    if devise == "Dollars" :
        D = montant*1.15
        return D
    elif devise == "Livre" :
        L = montant*0.81
        return L
    elif devise == "Fcfa":
        F = montant*655
        return F
    elif devise == "Yens" :
        Y = montant*130
        return Y
  
#print(conversion_euros(100,"Fcfa"))
#print(conversion_euros(100,"Yens"))
#print(conversion_euros(100,"Dollars"))
#print(conversion_euros(100,"Livre"))


# 3 Volume
from math import*
def  volume_cube(a):
    V = a*a*a
    return V
def volume_boule(r):
    # avec r le rayon de la sphere 
    V = (4/3)*pi*r**3
    return V 
def volume_cylindre(h,r):
    V = pi*r**2*h
    return V 
def volume_boite_parallepipede_rectangle(L,l,h):
    V = L*l*h
    return V

#print(volume_cube(3))
#print(volume_boule(3))
#print(volume_cylindre(13,3))
#print(volume_boite_parallepipede_rectangle(13,3,3))


#4. Périmètres et aires
#a
def perimetre_aire_rectangle(a,b):
    P = 2*(a+b)
    A = a*b
    return P,A
#b
from math import pi
def perimetre_aire_disque(rayon):
    P = 2*pi*rayon
    A = pi*rayon**2
    return P,A
#c
for rayon in range(0,30):
    P,A = perimetre_aire_disque(rayon/10)
    if A > P:
        print("À partir du rayon", rayon / 10,
              "l'aire est plus grande que le périmètre.")
        break
    

#print(perimetre_aire_rectangle(5,10))
print(perimetre_aire_disque(50))




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
polygone(5,200)
ht()
done()
        


#        Activité 4 (Toujours des fonctions)
#        Objectifs : créer de nouvelles fonctions

# ____________1_______
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



#        Activité 4 (Toujours des fonctions)
#        Objectifs : créer de nouvelles fonctions

# ____________1_______
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
test_multiplication("anglais")



import random 

# =_=_=_=A_=_=_=
def generer_et_verifier():
    # On génère les nombres ici
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    # On renvoie a, b et le résultat correct pour que la partie B puisse les utiliser
    return a, b, a * b

# =_=_=_=B_=_=_=
def test_multiplication(lang):
    # 1. On récupère les nombres et la bonne réponse générés par la partie A
    a, b, bonne_reponse = generer_et_verifier()
    
    # 2. Pose de la question selon la langue
    if lang == "francais":
        reponse_utilisateur = input(f"Combien font {a} x {b} ? : ")
    elif lang == "anglais":
        reponse_utilisateur = input(f"How much is {a} x {b} ? : ")
    elif lang == "Deutsch": # Correction de 'lamg'
        reponse_utilisateur = input(f"Wie viel ist {a} x {b} ? : ")
    else:
        print("Langue non supportée / Language not supported / Nicht unterstützt")
        return False

    # 3. Conversion et vérification de la réponse
    reponse_num = int(reponse_utilisateur)
    est_correct = (reponse_num == bonne_reponse)

    # 4. Affichage du verdict selon la langue
    if lang == "francais":
        if est_correct:
            print("Bravo ! C'est exact.")
        else:
            print(f"Faux ! La bonne réponse était {bonne_reponse}.")
            
    elif lang == "anglais":
        if est_correct:
            print("Well done! That's correct.")
        else:
            print(f"Wrong! The correct answer was {bonne_reponse}.")
            
    elif lang == "Deutsch":
        if est_correct:
            print("Super! Das ist richtig.") # Allemand plus naturel que 'Geil' dans un quiz scolaire
        else:
            print(f"Oh nein! Die richtige Antwort war {bonne_reponse}.")
            
    return est_correct

# Exemple de test
test_multiplication("francais")







    
    




















    
