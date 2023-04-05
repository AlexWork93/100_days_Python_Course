from turtle import Turtle


def create_segment(x=0.0, y=0.0):
    segment = Turtle()
    segment.shape("square")
    segment.color("white")
    segment.turtlesize = 20
    segment.penup()
    segment.setx(x)
    segment.sety(y)
    return segment


class Snake:
    snake = []
    collision = False

    def __init__(self):
        self.snake.append(create_segment())
        for _ in range(10):
            self.snake.append(create_segment(self.snake[-1].xcor() - 20, 0))

    def detect_self_collision(self):
        for i in self.snake[1:]:
            print(self.collision)
            if self.snake[0].distance(i) <= 25:
                return True
            return False

    def detect_border_collision(self):
        if self.snake[0].xcor() < -500 \
                or self.snake[0].xcor() > 500 \
                or self.snake[0].ycor() < -500 \
                or self.snake[0].ycor() > 500:
            return True
        return False

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].setx(self.snake[i - 1].xcor())
            self.snake[i].sety(self.snake[i - 1].ycor())
            self.collision = self.detect_self_collision()
        self.snake[0].forward(20)
        self.collision = self.detect_border_collision()

    def move_right(self):
        self.snake[0].setheading(0)

    def move_left(self):
        self.snake[0].setheading(180)

    def move_up(self):
        self.snake[0].setheading(90)

    def move_down(self):
        self.snake[0].setheading(270)
