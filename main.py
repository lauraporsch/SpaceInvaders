from turtle import Screen
import time
import random
from player import PlayerShip, Shooter
from aliens import Aliens
from boards import Score, Lives
from mystery_alien import MysteryAlien
from barriers import Barrier

STARTING_POSITION = 310

# ---------------------------- SET UP SCREEN ------------------------------- #
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

playership = PlayerShip()
shooter = Shooter()
aliens = Aliens(y=STARTING_POSITION)
score = Score()
lives = Lives()
mystery = MysteryAlien()
barrier = Barrier()


# ---------------------------- DEFINE FUNCTIONS ------------------------------- #
def shoot():
    """Pass if shooter is already visible, if not, shooter goes to center of playership and turns visible"""
    if shooter.isvisible():
        pass
    else:
        shooter.goto(x=playership.xcor(), y=-370)
        shooter.showturtle()
# as a workaround in the Turtle Module, the player shooter is always moving but not visible. To create the impression
# of a triggered shot, the shooter gets visible and moved to the center of the playership to start moving from there


def alien_gets_shot():
    """If any alien is within 20 pixels of the visible player-shooter, alien gets removed from list, shooter gets
    hidden and player score increased by 20 points"""
    for shot_alien in aliens.all_aliens:
        if shooter.isvisible() and shot_alien.distance(shooter) < 20:
            aliens.all_aliens.remove(shot_alien)
            shot_alien.goto(-1000, -1000)
            shooter.hideturtle()
            score.increase(20)
# Turtle Module does not allow to delete single object from the Screen. Workaround: moving object out of visible screen


def mystery_gets_shot():
    """If mystery-alien is within 50 pixels of the visible player-shooter, mystery-alien and shooter gets hidden and
    player score increased by a random choice of points"""
    if mystery.isvisible() and shooter.isvisible() and mystery.distance(shooter) < 50:
        mystery.hideturtle()
        shooter.hideturtle()
        mystery_points = random.choice([50, 60, 70, 80, 90, 100])
        score.increase(mystery_points)
# Distance in the Turtle Module is measured from the center of the object. Therefore, a bigger object requires a
# higher pixel count for the distance method


def player_gets_shot():
    """If any visible alien-shooter is within 20 pixels of the player-ship, player looses a live, player-ship goes
    back to starting position, alien-shooter gets hidden, 0.5 seconds sleep to reset gameplay"""
    for alien_shot in aliens.all_shooters:
        if alien_shot.isvisible() and alien_shot.distance(playership) < 20 and alien_shot.ycor() < -370:
            lives.loose()
            playership.go_to_start()
            alien_shot.hideturtle()
            time.sleep(0.5)


def barrier_gets_shot():
    """If any part of the barrier is within 20/25 pixels of the visible alien- /player-shooter, brick gets deleted
    from screen, shooter gets hidden"""
    for brick in barrier.whole_barrier:
        if brick.isvisible():
            for alien_shooting in aliens.all_shooters:
                if alien_shooting.isvisible() and alien_shooting.distance(brick) < 20:
                    brick.hideturtle()
                    alien_shooting.hideturtle()
            if shooter.isvisible() and shooter.distance(brick) < 25:
                brick.hdieturtle()
                shooter.hideturtle()


# ---------------------------- DEFINE KEYBOARD EVENTS ------------------------------- #
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
    mystery.move()

    aliens.trigger_shooter()
    mystery.trigger()

    alien_gets_shot()
    mystery_gets_shot()
    player_gets_shot()
    barrier_gets_shot()

    # if player-shooter reaches top of screen it gets hidden and goes back to starting point (to be ready for next shot)
    if shooter.ycor() > 345:
        shooter.hideturtle()
        shooter.go_to_start()

    if lives.lives == 0 or aliens.win():
        lives.game_over()
        score.update_highscore()
        game_is_on = False

    if not aliens.all_aliens:
        STARTING_POSITION -= 50
        for alien_shooter in aliens.all_shooters:
            alien_shooter.hideturtle()
        aliens = Aliens(y=STARTING_POSITION)


screen.exitonclick()

