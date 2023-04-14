import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

num_of_session = 0
timer = None
speed = 1000
run = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global num_of_session
    global run
    run = False
    if timer:
        tomato_canvas.after_cancel(timer)
    num_of_session = 0
    label_checkmarks.configure(text='')
    tomato_canvas.itemconfig(timer_text, text="00:00")
    label_timer.configure(text='Timer')
    label_timer.grid(padx=180)
    print("reset timer")


def switch_test_mode():
    global speed
    if speed == 1000:
        speed = 1
        button_test_mode.configure(fg=RED)
    else:
        speed = 1000
        button_test_mode.configure(fg=GREEN)
    reset_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global run
    if not run:
        run = True
        global num_of_session
        num_of_session += 1
        if num_of_session % 8 == 0:
            countdown(LONG_BREAK_MIN * 60)
            label_timer.configure(text='Take a rest:)')
            label_timer.grid(padx=4)

            print("long")
        elif num_of_session % 2 == 0:
            countdown(SHORT_BREAK_MIN * 60)
            label_timer.configure(text='Take a rest:)')
            label_timer.grid(padx=4)

            print('short')
        else:
            countdown(WORK_MIN * 60)
            label_timer.configure(text='Time to work')
            label_timer.grid(padx=26)

            print('work')
        print(num_of_session)
        label_checkmarks.configure(text=CHECKMARK * math.floor(num_of_session / 2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(value):
    amount_of_min = math.floor(value / 60)
    amount_of_sec = value % 60
    if amount_of_sec < 10:
        amount_of_sec = f"0{amount_of_sec}"
    tomato_canvas.itemconfig(timer_text, text=f"{amount_of_min}:{amount_of_sec}")
    # print(f"{amount_of_min}:{amount_of_sec}")
    if value > 0:
        global timer
        timer = tomato_canvas.after(speed, countdown, value - 1)
    else:
        global run
        run = False
        start_timer()

    # ---------------------------- UI SETUP ------------------------------- #


screen = tkinter.Tk()
screen.configure(padx=100, pady=50, background=YELLOW)
screen.title("Pomodoro")

tomato_img = tkinter.PhotoImage(file='tomato.png')
tomato_canvas = tkinter.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_canvas.create_image(100, 112, image=tomato_img)
timer_text = tomato_canvas.create_text(100, 150, text="00:00", fill='white', font=(FONT_NAME, 34, 'bold'))
tomato_canvas.grid(column=1, row=1)

label_timer = tkinter.Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 55))
label_timer.grid(column=1, row=0, padx=180)

button_start = tkinter.Button(text="Start", background=YELLOW, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text="Reset", background=YELLOW, command=reset_timer)
button_reset.grid(column=2, row=2)

button_test_mode = tkinter.Button(text="Test mode", background=YELLOW, fg=GREEN, command=switch_test_mode)
button_test_mode.grid(column=2, row=3)

label_checkmarks = tkinter.Label(text="", fg=GREEN, background=YELLOW, font=(FONT_NAME, 34, 'bold'))
label_checkmarks.grid(column=1, row=3)

screen.mainloop()
