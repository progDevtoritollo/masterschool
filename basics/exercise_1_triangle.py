import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(1) 
t.pencolor("green") 

t.left(180) 

for _ in range(3):
    t.forward(100)  
    t.left(120) 

turtle.done()