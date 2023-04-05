from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, current_score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 450)
        self.write(f"Score {current_score}", False, "center", ("Arial", 15, "normal"))

    def update_score(self, score):
        self.clear()
        self.write(f"Score {score}", False, "center", ("Arial", 15, "normal"))


