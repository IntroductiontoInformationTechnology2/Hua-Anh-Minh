import winsound
from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from map import *
from match import *


def set_pos_start_gui(gui, width_of_menu, height_of_menu):
    ws = gui.winfo_screenwidth()
    hs = gui.winfo_screenheight()
    startPosX = (ws / 2) - (width_of_menu / 2)
    startPosY = (hs / 2) - (height_of_menu / 2)
    gui.geometry('%dx%d+%d+%d' % (width_of_menu, height_of_menu, startPosX, startPosY))


def choose_level(destroy_menu): 
    destroy_menu.destroy()
    choose_map = Tk()
    choose_map.title("Select Level")

    set_pos_start_gui(choose_map, 300, 200)

    text_ask = StringVar()
    text_ask.set("Please choose the level of the map")
    Label(choose_map, textvariable = text_ask, height = 3, width = 40, padx = 0, pady = 0).pack()
    Button(choose_map, text = "Level 1", command = lambda: begin_match(1, choose_map), height = 1, width = 20).pack()
    Button(choose_map, text = "Level 2", command = lambda: begin_match(2, choose_map), height = 1, width = 20).pack()
    Button(choose_map, text = "Level 3", command = lambda: begin_match(3, choose_map), height = 1, width = 20).pack()

    choose_map.mainloop()


def info():
    messagebox.showinfo("About", """
    Information about Game\n
    Mid-term project for subject Introduction to Information Technology 2 - class 17CLC2 - Group 3\n
    Version info: pre-release alpha build 1.1\n
    Every information about game, bugs, features, please contact to huaanhminh0412@gmail.com\n
    -------------------------------------------------------------------------------\n
    Team members:\n
    Team leader: Hứa Anh Minh - Student ID: 1753070\n
    Phùng Thanh Sang - Student ID: 1753096\n
    Nguyễn Lý Nhật Phương - Student ID: 1753089\n
    Lê Minh Quân - Student ID: 1753137\n
    """)


def Introduction():
    messagebox.showinfo("Introduction", """
    Welcome to the instruction of turtle race. First, name four turtles on the race.\n
    If not, their default name will be Ruby, Python, JavaScript and Null.\n
    Choose the turtle that you think it will win (1-4)
    """)


def draw_menu():
    #winsound.PlaySound('Spectre NCS Release.wav', winsound.SND_ASYNC + winsound.SND_LOOP)
    menu_gui = tkinter.Tk()
    menu_gui.title("MAIN MENU")
    menu_gui.config(background = 'white')
    set_pos_start_gui(menu_gui, 350, 280)
    text_welcome = StringVar()
    text_welcome.set("WELCOME TO THE TURTLE RACE")

    Label(menu_gui, textvariable = text_welcome, height = 3, width = 40, background = 'white').pack()
    Button(menu_gui, text = 'Start', command = lambda: choose_level(menu_gui), height = 2, width = 10).pack()
    Button(menu_gui, text = 'Introduction', command = lambda: Introduction(), height = 2, width = 10).pack()
    Button(menu_gui, text = 'About', command = lambda: info(),height = 2, width = 10).pack()

    Label(menu_gui, height = 1, background = 'white').pack()

    frame_python_logo = Frame(menu_gui, width = 230, height = 80, background = 'white')
    frame_python_logo.pack_propagate(0)
    frame_python_logo.pack()
    python_logo = PhotoImage(file='python-powered-w-200x80.png')
    Label(frame_python_logo, image = python_logo).pack()
    menu_gui.mainloop()

