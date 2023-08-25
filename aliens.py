from turtle import Turtle
import random

NUMBER_OF_ROWS = 4
NUMBER_OF_ALIENS = 11
MOVE_DISTANCE = 2
MOVE_DOWN = 20
SHOOT_SPEED = 15
STARTING_POSITION = (-225, 310)


class Aliens:
    def __init__(self, y):
        self.all_aliens = []
        self.all_shooters = []
        self.x = -225
        self.y = y
        for line in range(NUMBER_OF_ROWS):
            for alien in range(NUMBER_OF_ALIENS):
                self.create_aliens(position=(self.x, self.y))
                self.create_shooter(position=(self.x, self.y))
                self.x += 50
            self.y -= 50
            self.x = -225
        self.move_speed = MOVE_DISTANCE

    def create_aliens(self, position):
        alien = Turtle("turtle")
        alien.penup()
        alien.color("white")
        alien.goto(position)
        self.all_aliens.append(alien)

    def create_shooter(self, position):
        shooter = Turtle("classic")
        shooter.penup()
        shooter.color("white")
        shooter.hideturtle()
        shooter.goto(position)
        self.all_shooters.append(shooter)

    def move(self):
        for alien in self.all_aliens:
            alien.forward(self.move_speed)
        for shooter in self.all_shooters:
            if shooter.isvisible():
                shooter.forward(SHOOT_SPEED)
            else:
                shooter.forward(self.move_speed)
        self.check_borders()

    def check_borders(self):
        right_screen = any(alien.xcor() > 370 for alien in self.all_aliens)
        left_screen = any(alien.xcor() < -370 for alien in self.all_aliens)
        if right_screen or left_screen:
            self.increase_speed()
        for alien in self.all_aliens:
            if right_screen:
                alien.setheading(180)
                alien.sety(alien.ycor() - MOVE_DOWN)
            elif left_screen:
                alien.setheading(0)
                alien.sety(alien.ycor() - MOVE_DOWN)
        for shooter in self.all_shooters:
            if shooter.isvisible():
                pass
            elif right_screen:
                shooter.setheading(180)
                shooter.sety(shooter.ycor() - MOVE_DOWN)
            elif left_screen:
                shooter.setheading(0)
                shooter.sety(shooter.ycor() - MOVE_DOWN)

    def increase_speed(self):
        self.move_speed += 1

    def trigger_shooter(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            random_alien = random.choice(self.all_aliens)
            index = self.all_aliens.index(random_alien)
            random_shooter = self.all_shooters[index]
            if not random_shooter.isvisible() and random_shooter.ycor() < -250:
                random_shooter.goto(random_alien.xcor(), random_alien.ycor())
                random_shooter.setheading(random_alien.heading())
            elif not random_shooter.isvisible() and random_shooter.ycor() > -250:
                random_shooter.setheading(270)
                random_shooter.showturtle()
            elif random_shooter.ycor() < -380:
                random_shooter.hideturtle()
                random_shooter.goto(random_alien.xcor(), random_alien.ycor())
                random_shooter.setheading(random_alien.heading())

    def win(self):
        bottom_screen = any(alien.ycor() < -360 for alien in self.all_aliens)
        if bottom_screen:
            return True
