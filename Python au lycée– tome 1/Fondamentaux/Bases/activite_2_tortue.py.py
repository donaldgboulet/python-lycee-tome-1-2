from turtle import*

# Activite 2 (Les mots de la tortue).
"""
Objectifs : piloter la tortue par un mot, chaque caractère correspondant à une instruction.
• A:avance de 100 en traçant,
• a:avance de 100 sans tracer,
• g:tourne à gauche de 90 degrés,
• d:tourne à droite de 90 degrés.
"""

mot =   "AagAgAdAgAAgaAA"
#mot = "AAgAdAAgAAdAAdgAgAddd" # Essayer de changer de mot 

penup()
goto(-150,-150)
pendown()
color('blue')
width(5)

for c in mot:
    if c == 'A':
        forward(100)
    elif c == 'a':
        up()
        forward(100)
        down()
    elif c == 'g':
        left(90)
    elif c == 'd':
        right(90)


ht()        
exitonclick()
        