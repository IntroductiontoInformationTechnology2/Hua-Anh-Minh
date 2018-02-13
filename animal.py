from random import randint
from turtle import *


class Animal:
    def __init__(self, name, color, startX, startY, speedMin, speedMax, shape):
        self.name = name
        self.color = color
        self.startX = startX
        self.startY = startY
        self.speedMin = speedMin
        self.speedMax = speedMax
        self.shape = shape
        self.animal = Turtle()
        self.animal.color(self.color)
        self.animal.shape(self.shape)
        self.animal.penup()
        self.animal.goto(self.startX, self.startY)
        self.animal.pendown()
        self.animal.speed(randint(self.speedMin, self.speedMax))
        self.step = 0

    def move(self, rotate, step):
        if rotate != 0:
            self.animal.left(rotate)
        self.animal.forward(step)
        if rotate == 0:
            self.step += step
        else:
            self.step -= step
