import turtle

screen = turtle.Screen()
screen.bgcolor("black") 

color = turtle.textinput("Pick a color", "Enter a color (e.g., red, green, blue): ")


t = turtle.Turtle()
t.speed(1) 
t.pencolor(color) 

t.right(90)
t.forward(100) 

turtle.done()