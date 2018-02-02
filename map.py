import winsound
from turtle import *
import turtle

winsound.PlaySound('Spectre NCS Release.wav', winsound.SND_ASYNC)

def draw_map():
    turtle.setup(width = 800, height = 600)
    turtle.speed(0)
    screen = turtle.Screen()
    screen.title("TURTLE RACE")
    length = int(screen.numinput("Setup the map", "Enter the length", 20, 20, 1500))
    width = int(screen.numinput("Setup the map", "Enter the width", 11, 11, 25))
    turtle.penup()
    turtle.setpos(-200, 100)

    for step in range(int(length / 2)):
        turtle.write(step, align = 'center')
        turtle.forward(40)
    turtle.pensize(5)
    setY = 100
    turnback = 1
    turtle.right(180)
    setY = setY - 20
    for i in range(5):
        turtle.penup()
        turtle.setpos(180, setY)
        turtle.pendown()
        turtle.forward(length * 20)
        turnback += 1
        setY = setY - 60
    turtle.penup()
    turtle.forward(1000)
    done()

draw_map()