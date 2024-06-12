import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.goto(-600, 0)

startSideLength = 100

def makeTriangle(sides, length, color):
    t.color(color)
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

def makeSquare(sides, length, color):
    t.color(color)
    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)

def moveToAnotherHouse(sideLength):
    t.penup()
    t.forward(sideLength * 2)
    t.pendown()

def makebuilding(sideLength):
    makeTriangle(3, sideLength, "green")

    t.penup()
    t.forward(sideLength / 4)
    t.right(90)
    t.forward(sideLength / 2)
    t.left(90)
    t.pendown()

    makeSquare(4, sideLength / 2, "red")

    t.penup()
    t.left(90)
    t.forward(sideLength / 2)
    t.left(90)
    t.forward(sideLength / 4)
    t.right(180)
    t.pendown()

    makeSquare(4, sideLength, "white")



for i in range(6):
    sideLength = startSideLength + i * 20
    makebuilding(sideLength)
    moveToAnotherHouse(sideLength)

turtle.done()