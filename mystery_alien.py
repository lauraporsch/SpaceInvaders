from turtle import Turtle
import random

STARTING_POINT = (-400, 340)
MOVE_SPEED = 15


class MysteryAlien(Turtle):
    def __init__(self):
        """Initiates class MysteryAlien, inherits from Turtle super class, sets initial attributes"""
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 3)
        self.penup()
        self.color("#191D88")
        self.hideturtle()
        self.move_speed = MOVE_SPEED
        self.goto(STARTING_POINT)

    def trigger(self):
        """Method is randomised. If MysteryAlien not visible, shows it and moves it across the screen. Randomises the
        attribute move_speed."""
        random_chance = random.randint(1, 40)
        if random_chance == 1 and not self.isvisible():
            self.goto(STARTING_POINT)
            self.showturtle()
            self.move_speed += random.randint(-10, 5)

    def move(self):
        """Moves MysteryAlien horizontally across the screen. If it reaches the right screen limit, hides and moves
        back to starting point"""
        self.forward(self.move_speed)
        if self.xcor() > 400:
            self.hideturtle()
            self.goto(STARTING_POINT)
            self.move_speed = MOVE_SPEED
