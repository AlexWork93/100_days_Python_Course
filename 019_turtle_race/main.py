from turtle import Turtle, Screen
import random

turtles = {}
screen = Screen()
turtle_color = screen.textinput("Make your bet", "red, green, orange, yellow, blue, purple")
# screen.colormode(255)
colors = ["red", "green", "orange", "yellow", "blue", "purple"]

def draw_finish_line():
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(410, -150)
    tim.left(90)
    tim.pensize(6)
    tim.pendown()
    tim.goto(410, 150)


def get_random_color():
    r = random.randint(0, 240)
    g = random.randint(0, 240)
    b = random.randint(0, 240)
    return r, g, b


def get_turtle_x(turtle):
    return turtle.xcor()


def get_random_amount_for_next_step():
    return random.randint(2, 45)


for i in range(5):
    turtles[colors[i]] = Turtle()
    turtles[colors[i]].penup()
    turtles[colors[i]].shape("turtle")
    turtles[colors[i]].color(colors[i])

screen.screensize(500, 400)

turtles[colors[0]].goto(-430, 100)
turtles[colors[1]].goto(-430, 50)
turtles[colors[2]].goto(-430, 0)
turtles[colors[3]].goto(-430, -50)
turtles[colors[4]].goto(-430, -100)

draw_finish_line()

should_move = True
while should_move:
    for key in turtles:
        turtles[key].forward(get_random_amount_for_next_step())
        if get_turtle_x(turtles[key]) > 400:
            should_move = False
            screen.textinput(f"{key} win", f"{key} win")
            break
screen.exitonclick()
