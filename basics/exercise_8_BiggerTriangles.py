import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(0) 
t.width(5)

GlobalLenthSideOfShape = 100
numberOfTriangles = 6
colors = ['purple', 'green', 'blue', 'yellow', 'orange', 'red', 'pink', 'brown', 'gray', 'gold']

def shape(sides, shapeNumber):
    t.color(colors[shapeNumber])
    t.left(120)
    for _ in range(sides):
        t.right(360/sides)  
        t.forward(GlobalLenthSideOfShape)

def hexagon():
    for triangleNumber in range(numberOfTriangles):
        shape(3, triangleNumber)
        t.right(120)
        t.forward(GlobalLenthSideOfShape)
        t.right(60)

t.right(180)

for _ in range(6):
    hexagon()
    t.left(120)
    t.forward(GlobalLenthSideOfShape)
    t.right(180)

turtle.done()

