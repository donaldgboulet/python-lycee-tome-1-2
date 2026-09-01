from math import *

"""
Activité 4 (Triangles).
Objectifs : déterminer les propriétés d'un triangle à partir des trois longueurs des côtés.
"""

def triangle():
    print("Entrez trois entiers a, b et c avec a ≤ b ≤ c")
    a = int(input("Valeur de a : "))
    b = int(input("Valeur de b : "))
    c = int(input("Valeur de c : "))

    # 1. Ordre
    if a <= b <= c:
        print("✓ Les valeurs respectent l'ordre a ≤ b ≤ c")
    else:
        print("✗ Les valeurs ne respectent pas l'ordre a ≤ b ≤ c")

    # 2. Existence
    if a + b >= c:
        print("✓ Il existe un triangle correspondant à ces longueurs")
    else:
        print("✗ Aucun triangle possible avec ces longueurs")
        return  # inutile de continuer

    # 3. Triangle rectangle (Pythagore)
    if a**2 + b**2 == c**2:
        print("✓ Le triangle est rectangle (en C)")

    # 4. Triangle équilatéral
    if a == b == c:
        print("✓ Le triangle est équilatéral")

    # 5. Triangle isocèle
    if (a == b or b == c or a == c) and not (a == b == c):
        print("✓ Le triangle est isocèle")

    # 6. Angles aigus (loi des cosinus)
    cos_A = (-a**2 + b**2 + c**2) / (2 * b * c)
    cos_B = (a**2 - b**2 + c**2) / (2 * a * c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

    if cos_A >= 0 and cos_B >= 0 and cos_C >= 0:
        print("✓ Tous les angles sont aigus (≤ 90°)")
    else:
        print("✗ Le triangle a un angle obtus (> 90°)")

triangle()
