from turtle import Turtle

NUMBER_OF_ROWS = 4
NUMBER_OF_ALIENS = 10
MOVE_DISTANCE = 5
MOVE_DOWN = 20


class Aliens:
    def __init__(self):
        self.all_aliens = []
        self.x = -225
        self.y = 330
        for line in range(NUMBER_OF_ROWS):
            for alien in range(NUMBER_OF_ALIENS):
                self.create_aliens(position=(self.x, self.y))
                self.x += 50
            self.y -= 50
            self.x = -225

    def create_aliens(self, position):
        alien = Turtle("turtle")
        alien.penup()
        alien.color("white")
        alien.goto(position)
        self.all_aliens.append(alien)

    def move_aliens(self):
        for alien in self.all_aliens:
            alien.forward(MOVE_DISTANCE)
        self.check_borders()

    def check_borders(self):
        right_screen = any(alien.xcor() > 370 for alien in self.all_aliens)
        left_screen = any(alien.xcor() < -370 for alien in self.all_aliens)
        for alien in self.all_aliens:
            if right_screen:
                alien.setheading(180)
                alien.sety(alien.ycor() - MOVE_DOWN)
            elif left_screen:
                alien.setheading(0)
                alien.sety(alien.ycor() - MOVE_DOWN)

    def aliens_win(self):
        bottom_screen = any(alien.ycor() < -360 for alien in self.all_aliens)
        for alien in self.all_aliens:
            if bottom_screen:
                return True
