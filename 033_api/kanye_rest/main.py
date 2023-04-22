from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    kanye_quote = response.json()['quote']
    canvas_quote.itemconfig(text_kanye_quote, text=kanye_quote)
    print(response.json()['quote'])


screen = Tk()
screen.configure(padx=100, pady=50)

image_bg = PhotoImage(file='kanye_rest/background.png')
image_kanye_button = PhotoImage(file='kanye_rest/kanye.png')

canvas_quote = Canvas(width=300, height=414, highlightthickness=0)
canvas_quote.create_image(150, 207, image=image_bg)
text_kanye_quote = canvas_quote.create_text(150, 207, width=270, text="bla bla", font="Arial, 24")
canvas_quote.grid(column=0, row=0)

button_kanye = Button()
button_kanye.configure(image=image_kanye_button, highlightthickness=0, command=get_quote)
button_kanye.grid(column=0, row=1)

screen.mainloop()
