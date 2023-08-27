from turtle import Turtle

STARTING_POSITION = (0, -370)
MOVE_DISTANCE = 30
SHOOT_DISTANCE = 40
X_LEFT_SCREEN = -360
X_RIGHT_SCREEN = 360


class PlayerShip(Turtle):
    def __init__(self):
        """Initiates class PlayerShip, inherits from Turtle super class, sets initial attributes, calls method
        go_to_start()"""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2)
        self.penup()
        self.color("white")
        self.go_to_start()

    def go_to_start(self):
        """Calls method goto() with set input starting_position"""
        self.goto(STARTING_POSITION)

    def go_right(self):
        """If PlayerShip is left of right screen limit, calls method forward with set distance move_distance and
        moves PlayerShip horizontally across the screen towards the right."""
        if self.xcor() > X_RIGHT_SCREEN:
            pass
        else:
            self.forward(MOVE_DISTANCE)

    def go_left(self):
        """If PlayerShip is right of left screen limit, calls method backward with set distance move_distance and
        moves PlayerShip horizontally across the screen towards the left."""
        if self.xcor() < X_LEFT_SCREEN:
            pass
        else:
            self.backward(MOVE_DISTANCE)


class Shooter(Turtle):
    """Initiates class Shooter, inherits from Turtle super class, sets initial attributes, calls method
    go_to_start()"""
    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        """Calls method goto() with set input starting_position"""
        self.goto(STARTING_POSITION)

    def move(self):
        """Calls method forward() with set input shoot_distance"""
        self.forward(SHOOT_DISTANCE)
