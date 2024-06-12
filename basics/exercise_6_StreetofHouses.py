import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(0) 

sideLeanth = 100

def maketriangle(sides, leanth, color):
  t.color(color)
  for _ in range(sides):
      t.forward(leanth)  
      t.left(360/sides) 

def makeSquer(sides, leanth, color):
  t.color(color)
  for _ in range(sides):
      t.forward(leanth)  
      t.right(360/sides) 

def moveToAnotherHouse():
  t.penup()
  t.forward(sideLeanth*2)
  t.pendown()

def makebuilding():
  maketriangle(3,100,"green")
  
  t.penup()
  t.forward(27)
  t.right(90)
  t.forward(50)
  t.left(90)
  t.pendown()

  makeSquer(4,50,"red")

  t.penup()
  t.left(90)
  t.forward(50)
  t.left(90)
  t.forward(27)
  t.right(180)
  t.pendown()

  makeSquer(4,100,"white")


t.goto(-500, 0)

for build in range(6):
  makebuilding()
  moveToAnotherHouse()

turtle.done()