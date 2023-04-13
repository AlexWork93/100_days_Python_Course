from tkinter import *


def calculate():
    label_km_value.configure(text=f"{round(int(input_miles.get()) * 1.609, 2)}")


window = Tk()
window.minsize(width=380, height=130)
window.configure(padx=30, pady=30)

label_km = Label(text="km")
label_km.grid(column=2, row=1)

label_km_value = Label(text="")
label_km_value.grid(column=1, row=1)

label_miles = Label(text="miles")
label_miles.grid(column=2, row=0)

input_miles = Entry()
input_miles.grid(column=1, row=0)

is_equal_to_label = Label(text="Is equal to: ")
is_equal_to_label.grid(column=0, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
