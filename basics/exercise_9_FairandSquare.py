import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(0) 
t.width(5)

LenthSideOfShape = 120
colors = ['purple', 'green', 'blue', 'yellow', 'orange', 'red', 'pink', 'brown', 'gray', 'gold']

def shape(sides, shapeNumber,LenthSideOfShape ):
    t.color(colors[shapeNumber])
    for _ in range(sides):
        t.right(360/sides)  
        t.forward(LenthSideOfShape)

for numberSquer in range(4):
    t.penup()
    t.goto(LenthSideOfShape/2, LenthSideOfShape/2)
    t.pendown()
    shape(4, numberSquer,LenthSideOfShape)
    LenthSideOfShape=LenthSideOfShape-20

turtle.done()

