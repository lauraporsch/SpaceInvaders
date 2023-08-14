from turtle import Turtle

STARTING_POSITION = (0, -370)
MOVE_DISTANCE = 15
X_LEFT_SCREEN = -360
X_RIGHT_SCREEN = 360


class PlayerShip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.penup()
        self.color("white")
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_right(self):
        if self.xcor() > X_RIGHT_SCREEN:
            pass
        else:
            self.forward(MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() < X_LEFT_SCREEN:
            pass
        else:
            self.backward(MOVE_DISTANCE)


class Shooter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)


