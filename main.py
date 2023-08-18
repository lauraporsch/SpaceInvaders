from turtle import Screen
import time
from player import PlayerShip, Shooter
from aliens import Aliens
from boards import Score, Lives

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

playership = PlayerShip()
shooter = Shooter()
aliens = Aliens()
score = Score()
lives = Lives()


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
            score.increase_score()


screen.listen()
screen.onkeypress(playership.go_right, "Right")
screen.onkeypress(playership.go_left, "Left")
screen.onkeypress(shoot, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    shooter.move()
    aliens.move_aliens()
    alien_gets_shot()

    if shooter.ycor() > 290:
        shooter.hideturtle()

    if lives.lives == 0 or aliens.aliens_win():
        lives.game_over()

screen.exitonclick()
