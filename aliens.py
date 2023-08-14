from turtle import Turtle

NUMBER_OF_ROWS = 4
NUMBER_OF_ALIENS = 10
MOVE_DISTANCE = 5


class Aliens:
    def __init__(self):
        self.all_aliens = []
        self.x = -225
        self.y = 350
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
            right_screen = any(alien.xcor() > 380 for alien in self.all_aliens)
            left_screen = any(alien.xcor() < -380 for alien in self.all_aliens)
            if right_screen:
                alien.setheading(180)
            elif left_screen:
                alien.setheading(0)
