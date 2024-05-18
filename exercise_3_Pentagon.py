import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(2) 
t.pencolor("purple") 
t.width(5)

t.left(180)

def shape(sides, leanthSide):
    for _ in range(sides):
        t.forward(leanthSide) 
        t.left(360/sides)  

shape(5, 100)
turtle.done()