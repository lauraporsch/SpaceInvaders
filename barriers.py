from turtle import Turtle

LENGTH = 10
WIDTH = 10
STARTING_X = [-350, -150, 50, 250]



class Barrier:
    def __init__(self):
        self.whole_barrier = []
        self.y = -250
        for x in STARTING_X:
            self.x = x
            for length in range(LENGTH):
                for width in range(WIDTH):
                    self.create_barrier(position=(self.x, self.y))
                    self.x += 10
                self.y += 10
                self.x = x
            self.y = -250

    def create_barrier(self, position):
        barrier = Turtle("square")
        barrier.shapesize(0.5, 0.5)
        barrier.penup()
        barrier.color("white")
        barrier.goto(position)
        self.whole_barrier.append(barrier)
