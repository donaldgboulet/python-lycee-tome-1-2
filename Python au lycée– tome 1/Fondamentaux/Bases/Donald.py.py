from turtle import*
setup(900, 400)
speed(5)
color('red')
width(5)

def Lettre_D():
    left(90)
    forward(100)
    left(92)
    circle(50, -180)

def Lettre_O():
    circle(50)

def Lettre_N():
    forward(100)
    right(135)
    forward(141)
    left(135)
    forward(100)

def Lettre_A():
    left(60)
    forward(100)
    right(120)
    forward(100)
    backward(30)
    right(120)
    forward(70)

def Lettre_L():
    forward(100)
    left(90)
    forward(70)

# ══════════════════════
#   DONALD
# ══════════════════════
penup()
goto(-400, -50)
pendown()
setheading(0)
Lettre_D()

penup()
goto(-220, 0)
pendown()
setheading(90)
Lettre_O()

penup()
goto(-180, -40)
pendown()
setheading(90)
Lettre_N()

penup()
goto(-60, -40)
pendown()
setheading(0)
Lettre_A()

penup()
goto(60, 60)
pendown()
setheading(-90)
Lettre_L()

penup()
goto(150, -50)
pendown()
setheading(0)
Lettre_D()

ht()
exitonclick()