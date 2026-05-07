import turtle
pen=turtle.Turtle()
pen.color("blue", "pink")
pen.speed(5)

for i in range(100):
    pen.forward(i*2)
    pen.right(45)
turtle.done()