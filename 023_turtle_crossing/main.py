import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def reset_screen(screen):
    screen.clear()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    return screen

screen = Screen()
screen = reset_screen(screen)
player_turtle = Player()
score_board = Scoreboard()


should_spawn = True
spawn_timer = 0

cars = []
speed_multiplier = 1

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.onkeypress(player_turtle.move, "w")

    if should_spawn:
        for _ in range(1, 4):
            cars.append(CarManager(speed_multiplier))
        should_spawn = False
    if spawn_timer > 10:
        should_spawn = True
        spawn_timer = 0
    spawn_timer += 1

    for i in cars:
        i.move()
        if i.distance(player_turtle) < 30:
            player_turtle.die_turtle()
            time.sleep(1)
            score_board.print_game_over()
            game_is_on = False

    if player_turtle.ycor() > 280:
        speed_multiplier += 1
        screen = reset_screen(screen)
        player_turtle = Player()
        score_board.update_and_print_score()

    screen.update()

screen.exitonclick()

