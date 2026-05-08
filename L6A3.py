import turtle
pen=turtle.Turtle()
pen.speed(1)
pen.color("pink")
pen.fillcolor("cyan")
for i in range(3):
    pen.forward(100)
    pen.left(120)
turtle.done()


import turtle
pen=turtle.Turtle()
x=turtle.Screen()
pen.speed(1)
pen.color("pink")
pen.fillcolor("cyan")
x.bgcolor("purple")
for i in range(6):
    pen.forward(100)
    pen.right(60)
turtle.done()

import turtle
pen=turtle.Turtle()
x=turtle.Screen()
pen.speed(1)
pen.color("pink")
pen.fillcolor("light blue")
x.bgcolor("lavender")
pen.begin_fill()
for i in range(2):
    pen.forward(200)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()
turtle.done()