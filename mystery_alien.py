from turtle import Turtle
import random

STARTING_POINT = (-450, 340)


class MysteryAlien(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.goto(STARTING_POINT)

    def move(self, move_speed):
        self.forward(move_speed)
        if self.xcor() > 400:
            self.goto(STARTING_POINT)
            pass
