from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Score(Turtle):
    """Initiates class Score, inherits from Turtle super class, sets initial attributes, gets value for attribute
    high_score from file 'high-score.txt', calls method update()."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high-score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-380, 360)
        self.update()

    def update(self):
        """clears Score and writes new Score with current score"""
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="left", font=FONT)

    def increase(self, points):
        """Increases attribute score by input 'points', calls method update"""
        self.score += points
        self.update()

    def update_highscore(self):
        """If score is higher than saved high score, opens files 'high-score.txt' and writes score. Resets score to
        0, calls method update()."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high-score.txt", mode="w") as file:
                file.write(str(self.score))
            self.score = 0
            self.update()


class Lives(Turtle):
    """Initiates class Lives, inherits from Turtle super class, sets initial attributes, calls method update()."""
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(400, 360)
        self.update()

    def update(self):
        """clears Lives and writes new Lives with current_lives"""
        self.clear()
        current_lives = ""
        for heart in range(self.lives):
            current_lives += "❤️"
        self.write(f"{current_lives}", align="right", font=FONT)

    def loose(self):
        """Reduces attribute lives by one, calls method update()."""
        self.lives -= 1
        self.update()

    def game_over(self):
        """Clears Lives, moves Lives to center of screen, writes 'GAME OVER'"""
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
