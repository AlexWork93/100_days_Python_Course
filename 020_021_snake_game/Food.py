from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.penup()
        self.setx(random.randint(-200, 200))
        self.sety(random.randint(-200, 200))

    # def remove_from_board(self):
    #     self.
    def move_to_new_position(self):
        self.setx(random.randint(-200, 200))
        self.sety(random.randint(-200, 200))
