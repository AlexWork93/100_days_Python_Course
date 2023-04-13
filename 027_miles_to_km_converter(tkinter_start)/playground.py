from tkinter import *


def change_label():
    label['text'] = input_field.get().title()


window = Tk()
window.minsize(500, 300)

label = Label(text="My Label")
label.grid(column=0, row=0)

input_field = Entry()
input_field.grid(column=0, row=2)

button = Button(text="Press ME", command=change_label)
button.grid(column=1, row=1)

button_01 = Button(text="Press ME", command=change_label)
button_01.grid(column=2, row=0)

text_field = Text()
text_field.grid(column=3, row=2)

window.mainloop()
