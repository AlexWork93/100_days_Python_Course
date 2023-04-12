import turtle
from turtle import Turtle, Screen
import pandas
import time


screen = Screen()

background = "blank_states_img.gif"
screen.addshape(background)

turtle.shape(background)
states_dataframe = pandas.read_csv('50_states.csv')
cursor_turtle = Turtle()
cursor_turtle.penup()
cursor_turtle.hideturtle()

guessed_counter = 0

continue_playing = True
while continue_playing:
    user_input = screen.textinput(f"Guess the state({guessed_counter}/51)", "Enter the name of any State").title()
    if user_input in states_dataframe.state.to_list():
        matched_line = states_dataframe[states_dataframe.state == user_input]
        state_name = matched_line.state.item()
        coordinate_x = matched_line.x.item()
        coordinate_y = matched_line.y.item()
        cursor_turtle.goto((coordinate_x, coordinate_y))
        cursor_turtle.write(state_name, False, "left")
        print(f"{state_name}, {coordinate_x}, {coordinate_y}")
        guessed_counter += 1
        time.sleep(2)

screen.mainloop()