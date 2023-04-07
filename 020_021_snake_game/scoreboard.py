from turtle import Turtle
import os.path

class ScoreBoard(Turtle):

    def __init__(self, current_score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 450)
        self.highest_score = self.fetch_highest_score()
        self.write(f"Score {current_score}, highest: {self.highest_score}", False, "center", ("Arial", 15, "normal"))

    def update_score(self, score):
        self.clear()
        if self.highest_score < score:
            self.highest_score = score
        self.write(f"Score {score}, highest: {self.highest_score}", False, "center", ("Arial", 15, "normal"))

    def fetch_highest_score(self):
        if os.path.isfile("score_backup.txt"):
            with open("score_backup.txt") as score_backup:
                return int(score_backup.read())
        else:
            return 0

    def save_highest_score(self):
        with open("score_backup.txt", "w") as score_backup:
            score_backup.write(str(self.highest_score))
