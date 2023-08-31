from turtle import Turtle
import random

NUMBER_OF_ROWS = 4
NUMBER_OF_ALIENS = 11
MOVE_DISTANCE = 2
MOVE_DOWN = 20
SHOOT_SPEED = 15
STARTING_POSITION = (-225, 310)
COLORS = ["#793FDF", "#7091F5", "#97FFF4", "#FFFD8C"]


class Aliens:
    def __init__(self, y):
        """Initiates class Aliens, with input y (for y coordinate), calls functions create_aliens() and
        create_shooter() depending on the set amounts for number_of_rows and number_of_aliens (per row), sets initial
        move speed"""
        self.all_aliens = []
        self.all_shooters = []
        self.x = -225
        self.y = y
        for line in range(NUMBER_OF_ROWS):
            for alien in range(NUMBER_OF_ALIENS):
                self.create_aliens(position=(self.x, self.y), color=COLORS[line])
                self.create_shooter(position=(self.x, self.y))
                self.x += 50
            self.y -= 50
            self.x = -225
        self.move_speed = MOVE_DISTANCE

    def create_aliens(self, position, color):
        """Creates alien based on Turtle Object with input position (for x and y coordinates), sets initial
        attributes, adds single object 'alien' to list of objects 'all_aliens'"""
        alien = Turtle("circle")
        alien.shapesize(0.7, 1.5)
        alien.penup()
        alien.color(color)
        alien.color_code = color
        alien.goto(position)
        self.all_aliens.append(alien)

    def create_shooter(self, position):
        """Creates alien-shooter based on Turtle Object with input position (for x and y coordinates), sets initial
        attributes, adds single object 'shooter' to list of objects 'all_shooters'"""
        shooter = Turtle("square")
        shooter.shapesize(0.1, 0.5)
        shooter.penup()
        shooter.color("white")
        shooter.hideturtle()
        shooter.goto(position)
        self.all_shooters.append(shooter)

    def move(self):
        """Calls method forward() with the distance move_speed for all objects in the lists 'all_aliens' and
        'all_shooters' with. If shooter object is visible (equals moving south on the screen) distance is set to
        shoot_speed. Calls method check_borders."""
        for alien in self.all_aliens:
            alien.forward(self.move_speed)
        for shooter in self.all_shooters:
            if shooter.heading() == 270:
                shooter.forward(SHOOT_SPEED)
            else:
                shooter.forward(self.move_speed)
        self.check_borders()

    def check_borders(self):
        """Checks if any of the objects in 'all_aliens' and 'all_shooters' has reached the left or right limit of the
        screen. If so, calls method increase_speed, changes heading to opposite direction and moves all objects south
        by reducing the y coordinate. Method is passed if shooter is visible (as equals to shooter moving south).
        """
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
            if shooter.heading() == 270:
                pass
            elif right_screen:
                shooter.setheading(180)
                shooter.sety(shooter.ycor() - MOVE_DOWN)
            elif left_screen:
                shooter.setheading(0)
                shooter.sety(shooter.ycor() - MOVE_DOWN)

    def increase_speed(self):
        """Increases attribute move_speed by adding one pixel"""
        self.move_speed += 1

    def trigger_shooter(self):
        """Method randomised, if triggered, calls a random object from the list all_aliens and the corresponding
        shooter. If shooter is not visible (equals not in use), changes heading to south and changes to visible. If
        shooter hits lower screen limit, shooter hides, goes to coordinates and changes to the heading of
        corresponding alien"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_alien = random.choice(self.all_aliens)
            index = self.all_aliens.index(random_alien)
            random_shooter = self.all_shooters[index]
            if (random_shooter.heading() == 0 or random_shooter.heading() == 90) and random_shooter.ycor() > -250:
                random_shooter.setheading(270)
                random_shooter.showturtle()
                if random_shooter.ycor() < -400:
                    random_shooter.hideturtle()
                    random_shooter.goto(self.all_aliens[index].xcor(), self.all_aliens[index].ycor())
                    random_shooter.setheading(self.all_aliens[index].heading())

    def win(self):
        """Returns True, if any object in list all_aliens reaches the bottom of the screen"""
        bottom_screen = any(alien.ycor() < -360 for alien in self.all_aliens)
        if bottom_screen:
            return True
