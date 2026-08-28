import math

# calculer l'aire du cercle fonction de son rayon
def aire_cercle():
    for r in range(1,11):
        aire = math.pi*r**2
        print(f" pour rayon = {r}:  L'aire du cercle est de {aire:.2f} m**2")
# calculer l'aire du carre  en fontion de son cote
def aire_carre():
    for c in range(1,11):
        aire = c*c
        print(f" pour cote du carre = {c}:  L'aire du carre est egale a {aire:.2f} m**2")
# calculer l'aire du rectangle  en fontion de sa longueur e sa largeur 
def aire_rectangles():
    for l in range(1, 11):
        for w in range(1, 11):
            aire = l*w
            print(f"Pour longuer = {l} et largeur = {w} on a {aire:.2f} m**2")

# calculer l'aire du traingle  en fontion de sa base et son hauteur 
def aire_triangle():
    for b in range(1,11):
        for h in range(1,11):
            aire = (b*h)/2
            print(f"Pour base = {b} et   hauteur = {h} on a {aire:.2f} m**2")
aire_cercle()
aire_carre()
aire_rectangles()
aire_triangle()
    