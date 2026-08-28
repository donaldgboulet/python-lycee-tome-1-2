#Activité 3 (Tortue)
"""
Objectifs : définir quelques fonctions qui dessinentdes figures géométriques.
Créer une fonction est similaire à créer un bloc avec Scratch"""
from turtle import*
speed(5)
#color('red')
#color('green')
#color('blue')
color('darkviolet')
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
    #n = 360/6
    for i in range(6):
        forward(longueur)
        left(60)
        
        
def polygone(n,longueur):
    #n = 360/12
    for i in range(n):
        forward(longueur)
        left(360/n)
        
    
      

        
penup()
goto(-30,-310)
pendown()
#triangle()
#carre()
#hexagone(200)
polygone(10,200)
ht()
exitonclick()

    