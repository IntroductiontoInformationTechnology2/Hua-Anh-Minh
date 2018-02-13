import turtle


def bet():
    choose = False
    while not choose:
        choose = turtle.numinput("Bet", "Guess who will win (1-4)", 1, 1, 4)
    return choose


def choose_set(): #this function will be used in the near future...
    pass


def get_name():
    turtle_1 = turtle.textinput("Name", "Name of the first turtle")
    turtle_2 = turtle.textinput("Name", "Name of the second turtle")
    turtle_3 = turtle.textinput("Name", "Name of the third turtle")
    turtle_4 = turtle.textinput("Name", "Name of the fourth turtle")
    if turtle_1 == "":
        turtle_1 = "Python"
    if turtle_2 == "":
        turtle_2 = "Ruby"
    if turtle_3 == "":
        turtle_3 = "JavaScript"
    if turtle_4 == "":
        turtle_4 = "Null"
    return turtle_1, turtle_2, turtle_3, turtle_4