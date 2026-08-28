
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


# --- Tests ---
#affiche_table_de_7()
#affiche_bonjour()
#affiche_une_table(5)
#affiche_salutation("Coucou !")
print(demande_prenom_nom())