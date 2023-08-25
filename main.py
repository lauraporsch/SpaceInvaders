from turtle import Screen
import time
import random
from player import PlayerShip, Shooter
from aliens import Aliens
from boards import Score, Lives
from mystery_alien import MysteryAlien
from barriers import Barrier

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

STARTING_POSITION = 310

playership = PlayerShip()
shooter = Shooter()
aliens = Aliens(y=STARTING_POSITION)
score = Score()
lives = Lives()
mystery = MysteryAlien()
barrier = Barrier()


def shoot():
    if shooter.isvisible():
        pass
    else:
        shooter.goto(x=playership.xcor(), y=-370)
        shooter.showturtle()


def alien_gets_shot():
    for shot_alien in aliens.all_aliens:
        if shooter.isvisible() and shot_alien.distance(shooter) < 20:
            aliens.all_aliens.remove(shot_alien)
            shot_alien.goto(-1000, -1000)
            shooter.hideturtle()
            score.increase(20)


def mystery_gets_shot():
    if mystery.isvisible() and shooter.isvisible() and mystery.distance(shooter) < 50:
        mystery.hideturtle()
        shooter.hideturtle()
        mystery_points = random.choice([50, 60, 70, 80, 90, 100])
        score.increase(mystery_points)


def player_gets_shot():
    for alien_shot in aliens.all_shooters:
        if alien_shot.isvisible() and alien_shot.distance(playership) < 20 and alien_shot.ycor() < -370:
            lives.loose()
            playership.go_to_start()
            alien_shot.hideturtle()
            time.sleep(0.5)


def barrier_gets_shot():
    for brick in barrier.whole_barrier:
        if brick.isvisible():
            for alien_shooting in aliens.all_shooters:
                if alien_shooting.isvisible() and alien_shooting.distance(brick) < 20:
                    brick.hideturtle()
                    alien_shooting.hideturtle()
            if shooter.isvisible() and shooter.distance(brick) < 25:
                brick.hideturtle()
                shooter.hideturtle()


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
    aliens.trigger_shooter()
    alien_gets_shot()
    mystery.move()
    mystery.trigger()
    mystery_gets_shot()
    player_gets_shot()
    barrier_gets_shot()

    if shooter.ycor() > 345:
        shooter.hideturtle()

    if lives.lives == 0 or aliens.win():
        lives.game_over()
        score.update_highscore()
        for alien in aliens.all_aliens:
            alien.hideturtle()
        for alien_shooter in aliens.all_shooters:
            alien_shooter.hideturtle()
        mystery.hideturtle()

    if not aliens.all_aliens:
        STARTING_POSITION -= 50
        for alien_shooter in aliens.all_shooters:
            alien_shooter.hideturtle()
        aliens = Aliens(y=STARTING_POSITION)


screen.exitonclick()
