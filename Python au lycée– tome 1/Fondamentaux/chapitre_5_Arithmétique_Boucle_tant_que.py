
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
#print(est_divisible(5,1))



"""
Activité2(Nombrespremiers).
__Objectifs:tester_si_un_entier_est(ou_pas)un_nombre_premier__

"""
#1 :-)Pluspetitdiviseur.

def plus_petit_diviseur(n):
    d = 2
    while n%d!=0:
        d +=1
    return d
    
#print(plus_petit_diviseur(14))


#2 :-)Nombrespremiers(1).
"""
Activité2(Nombrespremiers).
__Objectifs:tester_si_un_entier_est(ou_pas)un_nombre_premier__

"""
def plus_petit_diviseur(n):
    d = 2
    while n%d!=0:
        d +=1
    return d
    
print(plus_petit_diviseur(17))

#2 :-)Nombrespremiers(1).

def est_premier_1(n):
    
    if plus_petit_diviseur(n)==n:
        return True
    else:
        return False
        
print(est_premier_1(13))


#3 :-) Nombre_fermat(n)

def nombre_fermat(n):
    f_n = 2**2**n + 1
    while est_premier_1(f_n):
        n += 1
        f_n = 2**2**n + 1   # à recalculer ici, avec le nouveau n
    return f_n,n

print(nombre_fermat(0))



