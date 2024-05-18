import turtle
john = turtle.Turtle()

john.width(5)
john.penup()
john.back(140)
john.pendown()

for color in ["red", "blue", "green"]:
  john.penup()
  john.forward(50)
  john.pendown()
  john.color(color)
  john.forward(50)


turtle.done()
