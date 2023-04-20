from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')

screen = Tk()
try:
    french_words_dict = pandas.read_csv('data/words_to_learn.csv').to_dict(orient="records")
except FileNotFoundError and pandas.errors.EmptyDataError:
    french_words_dict = pandas.read_csv('data/french_words.csv').to_dict(orient="records")


image_flash_card_front = PhotoImage(file='images/card_front.png')
image_flash_card_back = PhotoImage(file='images/card_back.png')
image_button_right = PhotoImage(file='images/right.png')
image_button_wrong = PhotoImage(file='images/wrong.png')

timer = ''
new_data_to_show = {}


def flip_card():
    screen.after_cancel(timer)
    canvas_flash_card.itemconfig(text_field_language, text="English")
    canvas_flash_card.itemconfig(text_field_word, text=new_data_to_show["English"])
    canvas_flash_card.itemconfig(canvas_flash_card_image, image=image_flash_card_back)


def show_new_word():
    global timer
    global new_data_to_show
    global french_words_dict
    try:
        new_data_to_show = random.choice(french_words_dict)
    except IndexError:
        messagebox.showwarning(title="warning", message="You have completed all words\nList of words will be reset")
        french_words_dict = pandas.read_csv('data/french_words.csv').to_dict(orient="records")

    canvas_flash_card.itemconfig(text_field_language, text="French")
    canvas_flash_card.itemconfig(text_field_word, text=new_data_to_show["French"])
    canvas_flash_card.itemconfig(canvas_flash_card_image, image=image_flash_card_front)
    timer = screen.after(3000, flip_card)


def i_know_this_word():
    try:
        screen.after_cancel(timer)
    except ValueError:
        pass
    global french_words_dict
    french_words_dict.remove(new_data_to_show)
    pandas.DataFrame(french_words_dict).to_csv('data/words_to_learn.csv', index=False)
    show_new_word()


def i_dont_know_this_word():
    try:
        screen.after_cancel(timer)
    except ValueError:
        pass
    show_new_word()


screen.configure(pady=30, padx=30, bg=BACKGROUND_COLOR)

canvas_flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_flash_card_image = canvas_flash_card.create_image(400, 263, image=image_flash_card_front)
text_field_language = canvas_flash_card.create_text(400, 150, text="00:00", fill='black', font=LANGUAGE_FONT)
text_field_word = canvas_flash_card.create_text(400, 263, text="00:00", fill='black', font=WORD_FONT)

canvas_flash_card.grid(column=0, row=0, columnspan=2)

button_right = Button(image=image_button_right, bg=BACKGROUND_COLOR, highlightthickness=0, command=i_know_this_word)
button_right.grid(column=1, row=1)
button_wrong = Button(image=image_button_wrong, bg=BACKGROUND_COLOR, highlightthickness=0,
                      command=i_dont_know_this_word)
button_wrong.grid(column=0, row=1)
show_new_word()
screen.mainloop()
