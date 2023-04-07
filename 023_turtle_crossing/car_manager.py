COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_Y_COORDINATE = [0, 40, 80, 120, 160, 200, 240, -40, -80, -120, -160, -200]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self, speed_multiplier):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 3)
        self.movement_speed = MOVE_INCREMENT * speed_multiplier
        self.goto(300, random.choice(START_Y_COORDINATE))

    def move(self):
        self.setx(self.xcor() - self.movement_speed)
