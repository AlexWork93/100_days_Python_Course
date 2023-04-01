import turtle
import random
import colorgram

turtle.colormode(255)


def get_list_of_colors_from_image(path_to_img, amount_of_colors):
    colors_from_colorgram = colorgram.extract(path_to_img, amount_of_colors)
    result_colors = []
    for i in range(len(colors_from_colorgram) - 1):
        new_color = (colors_from_colorgram[i].rgb.r, colors_from_colorgram[i].rgb.g, colors_from_colorgram[i].rgb.b)
        if colors_from_colorgram[i].rgb.r < 240 \
                and colors_from_colorgram[i].rgb.g < 240 \
                and colors_from_colorgram[i].rgb.b < 240:
            result_colors.append(new_color)
    return result_colors


colors = get_list_of_colors_from_image("depositphotos_80366896-stock-illustration-seamless-watercolor-dots-pattern.jpg",
                                       20)

Timmy = turtle.Turtle()
Timmy.speed(0)
Screen = turtle.Screen()
Timmy.pensize(20)
Timmy.penup()
Timmy.setx(-200)
Timmy.sety(-200)

for _ in range(10):
    current_position_y = Timmy.ycor()
    current_position_x = Timmy.xcor()
    for _ in range(10):
        Timmy.dot(20, random.choice(colors))
        Timmy.forward(50)
    Timmy.sety(current_position_y + 50)
    Timmy.setx(current_position_x)

Timmy.hideturtle()
Screen.exitonclick()
