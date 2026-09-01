# activite_5 (Le coeur de la table de multiplication)
from turtle import*
from math import*
speed(5)
width(2)

def mutiplication_table():
    n = 300
    r = 200
    penup()
    goto(0,-r)
    pendown()
    circle(r)
     
    # 2. Connecter les points
    for k in range(n):
        x1 = r * cos(10*k*pi/n)
        y1 = r * sin(10*k*pi/n)
        k2 = (10*k) % n          # ← 2k modulo n
        x2 = r * cos(10*k2*pi/n)
        y2 = r * sin(10*k2*pi/n)
        penup()
        goto(x1, y1)
        pendown()
        goto(x2, y2)
        
        
"""
# activite_5 (Le coeur de la table de multiplication)
from turtle import*
from math import*
speed(5)
width(2)

def table_multiplication():
    n = 100
    r = 200
    penup()
    goto(0,-r)
    pendown()
    circle(r)
    for k in range(n):
        x1 = r*cos((2*k*pi)/n)
        y1 = r*sin((2*k*pi)/n)
        k2 = (2*k)%n
        x2 = r*cos((2*k2*pi)/n)
        y2 = r*sin((2*k2*pi)/n)
        penup()
        goto(x1,y1)
        pendown()
        goto(x2,y2)
        
    




table_multiplication()  
ht()
exitonclick()


"""

    
mutiplication_table()   
ht()
exitonclick()