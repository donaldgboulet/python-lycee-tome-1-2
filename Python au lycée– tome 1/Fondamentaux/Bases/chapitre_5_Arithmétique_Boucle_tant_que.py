
"""Activité 1 (Quotient, reste, divisibilité).
Objectifs : utiliser le reste pour savoir si un entier divise un autre.

#__1__
def quotient_reste(a,b):
    q = a//b
    r =  a%b
    print("Le quotient q de la division euclidienne de a par b est : ", q)
    print("Le Reste de la division euclidienne de a par b est : ", r)
    print("Si le reste r est bien positif et strictement inférieur à b : " , r>=0 and r<b)
    print(" Si on a bien l’égalité a = bq+ r :", a == b*q + r )
    
#quotient_reste(100,2)

#__2__


 Programme une fonction est_pair(n) qui teste si l’entier n est pair ou pas. La fonction renvoie
True ou False.
Indications
"""
"""
def est_pair(n):
    if n%2 == 0:
       return True
    else:
        return False
        
print(est_pair(6))

def est_pair_1_(n):
    q = n%10
    if q%2==0:
        return True
    else:
        return False
    
print(est_pair_1_(22))

def est_pair_2_(n):
        return n%2 == 0
print(est_pair_2_(5))

"""
#__3__
"""
3.Programme une fonction est_divisible(a,b) qui teste si b divise a. La fonction renvoie True
ou False."""

def est_divisible(a,b):
    return a%b==0   
print(est_divisible(5,1))
print(est_divisible(75,5))
print(est_divisible(39,7))

