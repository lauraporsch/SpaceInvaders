from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high-score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-380, 360)
        self.update_scoreboard()

    def update_scoreboard(self):
        """clears ScoreBoard and writes new ScoreBoard with current score"""
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 20
        self.update_scoreboard()


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(400, 360)
        self.update_lives()

    def update_lives(self):
        self.clear()
        current_lives = ""
        for heart in range(self.lives):
            current_lives += "❤️"
        self.write(f"{current_lives}", align="right", font=FONT)

    def loose_life(self):
        self.lives -= 1
        self.update_lives()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
