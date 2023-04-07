STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.move_to_start()
        self.setheading(90)

    def move(self):
        self.forward(20)

    def move_to_start(self):
        self.goto(0, -280)

    def die_turtle(self):
        self.color("red")
        self.shape("circle")
        self.shapesize(2)
