from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_left=True):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(4, 1)
        self.color("white")
        if position_left:
            self.setx(-380)
        else:
            self.setx(380)

    def move_up(self):
        self.sety(self.ycor() + 40)

    def move_down(self):
        self.sety(self.ycor() - 40)
