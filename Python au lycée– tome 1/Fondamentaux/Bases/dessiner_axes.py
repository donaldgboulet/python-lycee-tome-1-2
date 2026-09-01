from turtle import *
from math import cos,sin


def dessiner_axes():
    speed(0) # Vitesse maximale pour les axes
    hideturtle()
    
    # --- Tracer l'axe X ---
    penup()                                                 
    goto(-250, 0)
    pendown()
    goto(250, 0)
    
    # --- Tracer l'axe Y ---
    penup()
    goto(0, -150)
    pendown()
    goto(0, 150)
    
    # --- Ajouter des graduations et nombres ---
    # Graduations sur l'axe X (tous les 50 unités)
    for x in range(-200, 201, 30):
        penup()
        goto(x, -1)
        pendown()
        goto(x, 1) # Petit trait vertical
        # Écrire le nombre
        penup()
        goto(x - 10, -20)
        write(str(x), font=("Arial", 8, "normal"))
        
    # Graduations sur l'axe Y (tous les 20 unités, par exemple)
    for y in range(-200, 200, 30):
        if y != 0: # Ne pas écrire 0 deux fois
            penup()
            goto(-1, y)
            pendown()
            goto(1, y) # Petit trait horizontal
            penup()
            goto(10, y - 1)
            write(str(y), font=("Arial", 8, "normal"))

# Appelez cette fonction avant de tracer vos courbes
dessiner_axes()

def graphe_fonction_trigo():
    penup()
    color('red')
    x_start = -200
    y_start = 100 * (cos((1/20) * x_start - 200)) + 5
    goto(x_start, y_start)
    pendown()
    for x in range(-199, 201):
        y = 100 * (cos((1/20) * x - 200)) + 5
        goto(x, y)

def graphe_fonction_trigos():
    penup()
    color('green')
    x_start = -200
    y_start = 100 * (sin((1/20) * x_start - 200)) + 5
    goto(x_start, y_start)
    pendown()
    for x in range(-199, 201):
        y = 100 * (sin((1/20) * x - 200)) + 5
        goto(x, y)

# Tracé
graphe_fonction_trigo()
graphe_fonction_trigos()

hideturtle()
exitonclick()
