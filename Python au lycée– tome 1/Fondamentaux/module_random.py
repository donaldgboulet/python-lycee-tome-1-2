from random import*

n = randint(1,6)
print(n)

x = random()
print(x)

##ACTIVITE_1
a = randint(1,12)
b = randint(1,12)
d = a*b
c = int(input(f"Combien vaut ,d ? : "))
if c == d:
    print(f"Vous avez gagne Bravo ",d ,"est effectivement", c)
else:
    print("Vous avez  perdu : ", d, "ne vaut pas ", c ,"malheureusement")




