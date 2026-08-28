# cours_1 — Conditions

# Vérifier si un conducteur respecte la vitesse limite
def condition(vitesse):
    if vitesse > 110:
        print("Attention, tu roules trop vite !")
    elif vitesse == 110:
        print("Tu roules exactement à la limite.")
    else:
        print("Vous êtes un bon citoyen.")

# condition(200)

# Vérifier si un nombre est positif ou négatif
def nega_posi():
    x = -5
    if x >= 0:
        print("Le nombre est positif.")
    else:
        print("Le nombre est négatif.")

# nega_posi()


# cours_2 — Saisie utilisateur + conditions

prenom = input("Comment t'appelles-tu ? : ")
age = int(input("Quel est votre âge ? : "))

if age >= 18:
    print(f"Ohlala, Sie sind schon Erwachsen!! {prenom}")
    print("Supiii, sehr geil, du hast es geschafft!")
else:
    print(f"Du bist doch noch jung, {prenom}!")