from turtle import *
import turtle

turtle.setup(width = 800, height = 600)
screen = turtle.Screen()
screen.title("TURTLE RACE")
length = int(screen.numinput("Setup the map", "Enter the length", 20, 20, 1500))
width = int(screen.numinput("Setup the map", "Enter the width", 11, 11, 25))
penup()
turtle.setpos(-200, 100)
for step in range(length):
    write(step, align = 'center')
    turtle.speed(0)
    right(90)
    for space in range(width):
        turtle.speed(0)
        forward(10)
        pendown()
        forward(10)
        penup()
    backward(220)
    left(90)
    forward(20)
done()