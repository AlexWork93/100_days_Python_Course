import time
from turtle import Screen

import snake as snake_file
from Food import Food
import scoreboard as sb


screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")
screen.tracer(0)
print("================================")
print(screen.getcanvas().winfo_screen())
print("================================")

snake = snake_file.Snake()

current_score = 0

score_board = sb.ScoreBoard(current_score)


screen.listen()
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")

playing = True
food = Food()


while playing:
    screen.update()
    if snake.snake[0].distance(food) <= 20:
        print("HIT"*10)
        for _ in range(10):
            snake.snake.append(snake_file.create_segment(snake.snake[-1].xcor(), snake.snake[-1].ycor()))
        food.move_to_new_position()
        current_score += 1
        score_board.update_score(current_score)

    time.sleep(0.1)
    snake.move()
    if snake.collision:
        print("Game over")
        playing = False

    # food = Food()

# screen.update()

screen.exitonclick()
