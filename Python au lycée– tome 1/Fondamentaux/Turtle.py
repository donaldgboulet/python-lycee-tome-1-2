"""
from turtle import*
speed(1)


#============================#
# Tracer les premiers dessins#
#============================#

# Exercice 1

def Lettre_P():
    right(90)
    forward(100)
    forward(100)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    
def Lettre_Y():
    forward(100)
    left(45)
    forward(100)
    backward(100)
    right(90)
    forward(100)
 
penup()
goto(0,0)
pendown()
color('red')
width(5)
#setheading(180)
setheading(90)
#Lettre_P()
#Lettre_Y()
ht()
exitonclick()
"""

#### Exercice 2 (Activite 2) ########
  # Objectif:  Tracer les figures geometriques 
# 1- Tracer le premier pentagone en Bleu

from turtle import*
from math import*
setup(500,500)
bgcolor('black')   
#color('blue')
#color('red')
#color('darkviolet')
color('pink')
width(3)
speed(0)

def Pentagone():
    for i in range(5):
        forward(100)
        left(72)
    
def Pentagone_1():
    for i in range(5):
        forward(200)
        left(72)


def Dodecagone():
    for i in range(12):
        forward(100)
        left(30)
        
def spirale():
    longueur = 1
    for i in range(100):
        left(90)
        forward(longueur)
        longueur +=5


def graphe_fonction():
    penup()
    for x in range(-200, 201):
        y = (1/100) * x**2 -200
        goto(x, y)
        pendown()
    
def graphe_fonction_trigo():
    penup()
    color('red')
    for x in range(-200, 201):
        y = 20*(cos((1/20) * x -200 )) +5
        goto(x, y)
        pendown()
def graphe_fonction_trigos():
    penup()
    color('green')
    for x in range(-200, 201):
        y = 60*(cos((1/20) * x -200)) +5
        goto(x, y)
        pendown()
        
        

penup()
goto(-150,10)
pendown()
#Pentagone()
#Pentagone_1()
#Dodecagone()
#spirale()
#graphe_fonction()
graphe_fonction_trigo()
graphe_fonction_trigos()
ht()
exitonclick()




    
    



