from turtle import Screen
import time
from player import PlayerShip, Shooter
from aliens import Aliens

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

playership = PlayerShip()
shooter = Shooter()
aliens = Aliens()


def shoot():
    if shooter.isvisible():
        pass
    else:
        shooter.goto(x=playership.xcor(), y=-370)
        shooter.showturtle()


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

    if shooter.ycor() > 290:
        shooter.hideturtle()

screen.exitonclick()
