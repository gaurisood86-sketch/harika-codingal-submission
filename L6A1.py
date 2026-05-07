import turtle
pen=turtle.Turtle()
pen.speed(2)
pen.color("red")
pen.fillcolor("blue")
pen.begin_fill()

for i in range(4):
   pen.forward(100)
   pen.right(90)

pen.end_fill()
turtle.done()


import turtle
pen=turtle.Turtle()
number_of_sides=8
side_length=60

for i in range(number_of_sides):
   pen.forward(side_length)
   pen.right(360/number_of_sides)
turtle.done()

import turtle
pen=turtle.Turtle()

for i in range(5):
   pen.forward(150)
   pen.right(144)
turtle.done()

import turtle
pen=turtle.Turtle()

pen.circle(100)
turtle.done()