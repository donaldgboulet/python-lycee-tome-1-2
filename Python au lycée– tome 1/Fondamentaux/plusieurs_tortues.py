# Diriger plusieurs tortues
import turtle as Tortue
Tortue.width(5)

tortue1 = Tortue.Turtle()
tortue1.speed(5)
tortue1.penup()
tortue1.goto(-200, -200)
tortue1.pendown()
tortue1.color('red')


tortue2 = Tortue.Turtle()
tortue2.speed(5)
tortue2.penup()
tortue2.goto(200, -200)
tortue2.pendown()
tortue2.color('blue')


tortue3 = Tortue.Turtle()
tortue3.speed(5)
tortue3.penup()
tortue3.goto(200, 200)
tortue3.pendown()
tortue3.color('yellow')

tortue4 = Tortue.Turtle()
tortue4.speed(5)
tortue4.color('green')
tortue4.penup()
tortue4.goto(-200, 200)
tortue4.pendown()

for i in range(38):
    # tortue1 chasse tortue2
    position2 = tortue2.position()
    angle1 = tortue1.towards(position2)
    tortue1.setheading(angle1)
    tortue1.forward(10)
    
    # tortue2 chasse tortue3
    position3 = tortue3.position()
    angle2 = tortue2.towards(position3)
    tortue2.setheading(angle2)
    tortue2.forward(10)
    
    # tortue3 chasse tortue4
    # tortue2 chasse tortue3 ← tu l'as déjà!
    position3 = tortue4.position()
    angle3 = tortue3.towards(position3)
    tortue3.setheading(angle3)
    tortue3.forward(10)
    
    # tortue4 chasse tortue1
    position4 = tortue1.position()
    angle4 = tortue4.towards(position4)
    tortue4.setheading(angle4)
    tortue4.forward(10)


Tortue.exitonclick()