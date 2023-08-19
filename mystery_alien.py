from turtle import Turtle
import random

STARTING_POINT = (-400, 340)
MOVE_SPEED = 15


class MysteryAlien(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2, 2)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.move_speed = MOVE_SPEED
        self.goto(STARTING_POINT)

    def trigger(self):
        random_chance = random.randint(1, 40)
        if random_chance == 1 and not self.isvisible():
            self.goto(STARTING_POINT)
            self.showturtle()
            self.move_speed += random.randint(-10, 5)

    def move(self):
        self.forward(self.move_speed)
        if self.xcor() > 400:
            self.hideturtle()
            self.goto(STARTING_POINT)
            self.move_speed = MOVE_SPEED




