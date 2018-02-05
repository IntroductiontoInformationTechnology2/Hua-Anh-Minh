from turtle import *
import turtle
from get_user_info import *


def initialize_resolution():
    turtle.screensize()
    turtle.setup(width = 1.0, height = 1.0)
    turtle.speed(0)
    screen = turtle.Screen()
    screen.title("TURTLE RACE")


def draw_finish_line(posX, posY):
    turtle.penup()
    turtle.setpos(posX, posY)


def draw_map(level, destroy_menu):
    destroy_menu.destroy() #destroy the start Menu
    initialize_resolution()

    length_of_map = 0
    width_of_map = 0
    setX_map_line = 0
    setY_map_line = 100

    turtle.penup()
    if (level == 1):
        turtle.setpos(-200, setY_map_line)
        length_of_map = 20
        width_of_map = 11
        setX_map_line = 180
    elif (level == 2):
        turtle.setpos(-300, setY_map_line)
        length_of_map = 40
        width_of_map = 22
        setX_map_line = 480
    else:
        turtle.setpos(-400, setY_map_line)
        length_of_map = 50
        width_of_map = 44
        setX_map_line = 580

    for draw_number in range(int(length_of_map / 2)):
        turtle.write(draw_number, align = 'center')
        turtle.forward(40)

    turtle.pensize(5)
    turtle.right(180)
    setY_map_line -= 20
    
    for i in range(5):
        turtle.penup()
        turtle.setpos(setX_map_line, setY_map_line)
        turtle.pendown()
        turtle.forward(length_of_map * 20)
        setY_map_line -= 60

    draw_finish_line(setX_map_line, 100)
    get_name()
    bet()
    done()