import winsound
from turtle import *
import turtle
from tkinter import *
import tkinter.messagebox


winsound.PlaySound('Spectre NCS Release.wav', winsound.SND_ASYNC + winsound.SND_LOOP)

def draw_map(level, map):
    map.destroy()
    turtle.screensize()
    turtle.setup(width=1.0, height=1.0)
    turtle.speed(0)
    screen = turtle.Screen()
    screen.title("TURTLE RACE")

    #length = int(screen.numinput("Setup the map", "Enter the length", 20, 20, 1500))
    #width = int(screen.numinput("Setup the map", "Enter the width", 11, 11, 25))
    length = 0
    width = 0

    turtle.penup()
    if (level == 1):
        turtle.setpos(-200, 100)
        length = 20
        width = 11

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
    #winsound.PlaySound('Mini - Game Victory 6.wav', winsound.SND_ASYNC)
    #winner()
    done()

def winner():
    var = messagebox.showinfo("", "Player 1 win.")

def choose_level(destroy_menu):
    destroy_menu.destroy()
    choose_map = Tk()
    choose_map.title("Select Level")
    var = StringVar()
    ask_to_choose_map = Label(choose_map, textvariable=var, height = 3, width = 40, padx = 0, pady = 0)
    var.set("Please choose the level of the map")
    ask_to_choose_map.pack()
    level_1 = Button(choose_map, text = "Level 1", command = lambda: draw_map(1, choose_map), height=1, width=20)
    level_2 = Button(choose_map, text = "Level 2", command = lambda: draw_map(2, choose_map), height=1, width=20)
    level_3 = Button(choose_map, text = "Level 3", command = lambda: draw_map(3, choose_map), height=1, width=20)
    level_1.pack()
    level_2.pack()
    level_3.pack()
    choose_map.mainloop()

def info():
    var = messagebox.showinfo("About", """
    This game is a part of mid-term project at subject Introduction to Information and Technology.
    This is an open source software. You are free to copy, share and edit it.
    Team leader: Hua Anh Minh
    Phung Thanh Sang
    Le Minh Quan
    Nguyen Ly Nhat Phuong""")

def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()

def menu():
    draw_menu = tkinter.Tk()
    draw_menu.title("Start Menu")

    draw_menu.config(background='white')
    w = 300
    h = 250
    ws = draw_menu.winfo_screenwidth()
    hs = draw_menu.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    draw_menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    var = StringVar()
    menu_choose = Label(draw_menu, textvariable = var, height = 3, width = 40, padx = 0, pady = 0, background='white')
    var.set("WELLCOME TO THE TURTLE RACE")
    menu_choose.pack()
    Start = Button(draw_menu, text = "Start", command = lambda: choose_level(draw_menu), height = 2, width = 10)
    About = Button(draw_menu, text = "About", command = info, height = 2, width = 10)
    Start.pack()
    About.pack()
    line_space = Label(draw_menu, height = 1, background='white')
    line_space.pack()
    frame = Frame(draw_menu, width=230, height=80, background='white')
    frame.pack_propagate(0)
    frame.pack()
    img = PhotoImage(file='python-powered-w-200x80.png')
    make_label(frame, img)
    draw_menu.mainloop()

menu()
