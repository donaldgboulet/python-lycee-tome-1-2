from turtle import*
bgcolor('black')
speed(0)
width(3)
color('pink')

def sierpinski():
    for t in range(3):      # grand triangle bleu
        color("blue")
        forward(256)
        left(120)
        for t in range(3):      # grand triangle bleu
            color("red")
            forward(128)
            left(120)
            for t in range(3):      # grand triangle bleu
                color("green")
                forward(64)
                left(120)
                for t in range(3):      # grand triangle bleu
                     color("yellow")
                     forward(32)
                     left(120)
                     for t in range(3):      # grand triangle bleu
                         color("white")
                         forward(16)
                         left(120)
                         for t in range(3):      # grand triangle bleu
                             color("pink")
                             forward(8)
                             left(120)
    
    
penup()
goto(-150,-50)
pendown()
sierpinski()
ht()
exitonclick()