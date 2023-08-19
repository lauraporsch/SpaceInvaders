from turtle import Screen
import time
import random
from player import PlayerShip, Shooter
from aliens import Aliens
from boards import Score, Lives
from mystery_alien import MysteryAlien

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

playership = PlayerShip()
shooter = Shooter()
aliens = Aliens()
score = Score()
lives = Lives()
mystery = MysteryAlien()


def shoot():
    if shooter.isvisible():
        pass
    else:
        shooter.goto(x=playership.xcor(), y=-370)
        shooter.showturtle()


def alien_gets_shot():
    for alien in aliens.all_aliens:
        if shooter.isvisible() and alien.distance(shooter) < 20:
            aliens.all_aliens.remove(alien)
            alien.goto(-1000, -1000)
            shooter.hideturtle()
            score.increase(20)
            if score.score != 0 and len(aliens.all_aliens) % 5 == 0:
                aliens.increase_speed()


def mystery_gets_shot():
    if mystery.isvisible() and shooter.isvisible() and mystery.distance(shooter) < 50:
        mystery.hideturtle()
        shooter.hideturtle()
        mystery_points = random.choice([50, 60, 70, 80, 90, 100])
        score.increase(mystery_points)


screen.listen()
screen.onkeypress(playership.go_right, "Right")
screen.onkeypress(playership.go_left, "Left")
screen.onkeypress(shoot, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    shooter.move()
    aliens.move()
    alien_gets_shot()
    mystery.move()
    mystery.trigger()
    mystery_gets_shot()

    if shooter.ycor() > 345:
        shooter.hideturtle()

    if lives.lives == 0 or aliens.win():
        lives.game_over()


screen.exitonclick()
