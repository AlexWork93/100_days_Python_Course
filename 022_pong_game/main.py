from turtle import Screen
import Paddle
import time
import Ball
import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle_left = Paddle.Paddle()
paddle_right = Paddle.Paddle(False)
score_left = Score.Score()
score_Right = Score.Score(False)

ball = Ball.Ball()

screen.listen()
screen.onkeypress(paddle_left.move_up, "q")
screen.onkeypress(paddle_left.move_down, "a")

screen.onkeypress(paddle_right.move_up, "w")
screen.onkeypress(paddle_right.move_down, "s")

game = True

while game:
    time.sleep(0.05)
    ball.move()
    screen.update()
    if ball.xcor() >= 365 or ball.xcor() <= -365:
        if ball.distance(paddle_left) < 60:
            ball.change_x()
            score_left.update_score()
        elif ball.distance(paddle_right) < 60:
            ball.change_x()
            score_Right.update_score()
        else:
            game = False
            print("Game Over")

    if score_Right.score % 3 == 0 and ball.can_increase_speed:
        ball.increase_movement_speed()

    if not score_Right.score % 3 == 0:
        ball.can_increase_speed = True


screen.exitonclick()
