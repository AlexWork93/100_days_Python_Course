from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-100, 260)
        self.score = 0
        self.update_and_print_score()

    def update_and_print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)
        self.score += 1

    def print_game_over(self):
        self.clear()
        self.goto(-210, 250)
        self.write(f"Score: {self.score -1}", False, "center", FONT)
        self.goto(50, 230)
        self.write("GAME OVER", False, "center", ("Courier", 48, "normal"))



