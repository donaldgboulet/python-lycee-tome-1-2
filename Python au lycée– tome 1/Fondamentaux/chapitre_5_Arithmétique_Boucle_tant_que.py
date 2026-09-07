

"""
Chapitre 5 — Arithmétique, boucle "tant que"
Python au lycée, tome 1
"""
 
# ============================================================
# Activité 1 — Quotient, reste, divisibilité
# Objectif : utiliser le reste pour savoir si un entier divise un autre.
# ============================================================
 
# 1. Quotient et reste de la division euclidienne
def quotient_reste(a, b):
    q = a // b
    r = a % b
    print("Le quotient q de la division euclidienne de a par b est : ", q)
    print("Le reste r de la division euclidienne de a par b est : ", r)
    print("Le reste r est bien positif et strictement inférieur à b :", r >= 0 and r < b)
    print("On a bien l'égalité a = bq + r :", a == b * q + r)
 
 
# 2. est_pair(n) — teste si n est pair
def est_pair(n):
    return n % 2 == 0
 
 
# 3. est_divisible(a, b) — teste si b divise a
def est_divisible(a, b):
    return a % b == 0
 
 
# ============================================================
# Activité 2 — Nombres premiers
# Objectif : tester si un entier est premier ou non.
# ============================================================
 
# 1. Plus petit diviseur de n (à partir de 2)
def plus_petit_diviseur(n):
    d = 2
    while n % d != 0:
        d += 1
    return d
 
 
# 2. Nombres premiers (1) — version naïve
# n est premier si son plus petit diviseur est n lui-même.
def est_premier_1(n):
    return plus_petit_diviseur(n) == n
 
 
# 3. Nombre de Fermat : plus petit n tel que 2**2**n + 1 ne soit pas premier
def nombre_fermat(n):
    f_n = 2**2**n + 1
    while est_premier_1(f_n):
        n += 1
        f_n = 2**2**n + 1   # à recalculer avec le nouveau n
    return f_n, n
 
 
# 4. Nombres premiers (2) — on s'arrête dès que d*d > n
# (si n a un diviseur, il y en a forcément un <= racine(n))
def est_premier_2(n):
    d = 2
    while d*d <= n and n % d != 0:
        d += 1
    return d*d >= n
 
 
# 5. Nombres premiers (3) — ne teste que les diviseurs impairs
# (2 est traité à part ; ensuite, un diviseur pair est inutile à tester)
def est_premier_3(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n and n % d != 0:
        d += 2
    return d*d >= n
 
 
# 6. Temps de calcul — comparer est_premier_1 / 2 / 3 sur un million d'appels
# A faire
 
# ============================================================
# Tests
# ============================================================
 
quotient_reste(100, 2)
 
print("est_pair(6) :", est_pair(6))
print("est_divisible(5, 1) :", est_divisible(5, 1))
 
print("plus_petit_diviseur(17) :", plus_petit_diviseur(17))
print("est_premier_1(13) :", est_premier_1(13))
print("nombre_fermat(0) :", nombre_fermat(0))
 
print("est_premier_2(13) :", est_premier_2(13))   # True
print("est_premier_2(14) :", est_premier_2(14))   # False
print("est_premier_2(97) :", est_premier_2(97))   # True
 
print("est_premier_3(13) :", est_premier_3(13))   # True
print("est_premier_3(14) :", est_premier_3(14))   # False
print("est_premier_3(15) :", est_premier_3(15))   # False
 
