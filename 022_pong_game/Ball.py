from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(random.randint(135, 200))
        self.x = 10
        self.y = 10
        self.can_increase_speed = False

    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.change_y()

        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def change_x(self):
        self.x = self.x * -1

    def change_y(self):
        self.y = self.y * -1

    def increase_movement_speed(self):
        self.x *= 1.3
        self.y *= 1.3
        self.can_increase_speed = False

