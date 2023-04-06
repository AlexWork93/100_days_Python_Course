import turtle
from turtle import Turtle


class Score(Turtle):
    score = 0

    def __init__(self, position_left=True):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        if position_left:
            self.setx(-70)
            self.sety(250)
        else:
            self.setx(70)
            self.sety(250)
        self.write(self.score, False, "center", ("Arial", 40, "normal"))


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, False, "center", ("Arial", 40, "normal"))
