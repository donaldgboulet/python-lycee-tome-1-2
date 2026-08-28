def affiche_mois(nummero):
    if nummero == 1 :
        print("Nous sommes en Janvier! ")
    elif nummero == 2:
        print("Nous sommes en Fevrier! ")
    elif nummero == 3:
        print("Nous sommes en Mars! ")
    elif nummero == 4:
        print("Nous sommes en Avril! ")
    elif nummero == 5:
        print("Nous sommes en Mai! ")
    elif nummero == 6:
        print("Nous sommes en Juin! ")
    elif nummero == 7:
        print("Nous sommes en Juillet! ")
    elif nummero == 8:
        print("Nous sommes en Aout! ")
    elif nummero == 9:
        print("Nous sommes en Septembre! ")
    elif nummero == 10:
        print("Nous sommes en Octobre! ")
    elif nummero == 11:
        print("Nous sommes en Novembre! ")
    elif nummero == 12:
        print("Nous sommes en Decembre! ")
    else :
        print("Vous n'avez pas entrer le bon nombre !!!")
        print("Veillez entrez un nombre compris entre 1 et 12 Merci ")
        

#nummero = 1       
#affiche_mois(7)



def calcule_cube(a):
    cube = a*a*a # ou bien a**3
    return cube

x = 3
y = 4
z = calcule_cube(x)+calcule_cube(y)
#calcule_cube(9)
#print(calcule_cube(9))
print(z)
