from map import *
from get_user_info import *
from animal import *
from random import randint


def set_up_start_position(level):
    start_position = [0 for i in range(5)]
    start_position[0] = 215
    start_position[1] = 85
    start_position[2] = -45
    start_position[3] = -175
    if level == 1: start_position[4] = -200
    elif level == 2: start_position[4] = -300
    else: start_position[4] = -400
    return start_position


def set_up_turtle(level):
    name = [0 for i in range(4)]
    animals = [0 for i in range(4)]
    start_position = set_up_start_position(level)
    name[0], name[1], name[2], name[3] = get_name()
    choose = bet()
    animals[0] = Animal(name[0], 'yellow', start_position[4], start_position[0], 0, 2, 'turtle')
    animals[1] = Animal(name[1], 'red', start_position[4], start_position[1], 0, 2, 'turtle')
    animals[2] = Animal(name[2], 'blue', start_position[4], start_position[2], 0, 2, 'turtle')
    animals[3] = Animal(name[3], 'green', start_position[4], start_position[3], 0, 2, 'turtle')
    return name, choose, animals


def begin_match(level, destroy_menu): #no KISS in here
    destroy_menu.destroy()
    draw_map(level)
    name, choose, animals = set_up_turtle(level)
    if level == 1: length_to_race = 400
    elif level == 2: length_to_race = 800
    else: length_to_race = 1000

    check_available_to_move = [0 for i in range(4)]
    for i in range(0, 4, 1):
        check_available_to_move[i] = False
    while (animals[0].step < length_to_race or animals[1].step < length_to_race
           or animals[2].step < length_to_race or animals[3].step < length_to_race):
        while True:
            turn_move = randint(0, 3)
            if not check_available_to_move[turn_move]:
                check_available_to_move[turn_move] = True
                break
        if animals[turn_move].step < length_to_race:
            animals[turn_move].move(0, randint(0, length_to_race / 2))
        if (check_available_to_move[0] and check_available_to_move[1]
            and check_available_to_move[2] and check_available_to_move[3]):
            for i in range(0, 4, 1):
                check_available_to_move[i] = False