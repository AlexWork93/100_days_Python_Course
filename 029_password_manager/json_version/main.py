from tkinter import *
from tkinter import messagebox
import json
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    pass_letters = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    pass_num = [random.choice(numbers) for _ in range(0, random.randint(2, 4))]
    pass_symb = [random.choice(symbols) for _ in range(0, random.randint(2, 4))]
    password = []
    password.extend(pass_letters)
    password.extend(pass_num)
    password.extend(pass_symb)
    random.shuffle(password)
    password = ''.join(password)
    entry_password.delete(0, END)
    entry_password.insert(END, password)
    print("Generate")
    print(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_password.get()

    if website == "":
        messagebox.showwarning(title="warning", message="Please enter a website")
        return
    elif email == "":
        messagebox.showwarning(title="warning", message="Please enter a email")
        return
    elif not '@' in email:
        messagebox.showwarning(title="warning", message="Email is incorrect")
        return
    elif password == "":
        messagebox.showwarning(title="warning", message="Please enter a password")
        return

    is_ok = messagebox.askokcancel(title="Confirm data",
                                   message=f"Is this data correct?\nWebsite: {website}\nEmail: {email}\nPassword: {password}")

    new_entry = {website: {"email": email, "password": password}}
    saved_passwords = {}
    if is_ok:
        try:
            with open("data.json", "r") as data_json:
                saved_passwords = json.load(data_json)
        except FileNotFoundError:
            saved_passwords = new_entry
        except json.decoder.JSONDecodeError:
            saved_passwords = new_entry
        else:
            saved_passwords.update(new_entry)
        finally:
            with open("data.json", "w") as data_json:
                json.dump(saved_passwords, data_json)
        clear_entries()


def search_entry():
    try:
        with open("data.json", "r") as data_json:
            saved_passwords = json.load(data_json)
    except FileNotFoundError:
        messagebox.showwarning(title="warning", message="You have no passwords saved")
    website = entry_website.get()
    if website == "":
        messagebox.showwarning(title="warning", message="Please enter a website")
        return
    if website not in saved_passwords:
        messagebox.showwarning(title="warning", message="You don't have data for this website")
    else:
        messagebox.showwarning(title=website, message=f"Website: {website}\nEmail: {saved_passwords[website]['email']}\nPassword: {saved_passwords[website]['password']}")


def clear_entries():
    entry_website.delete(0, END)
    entry_email_username.delete(0, END)
    entry_email_username.insert(END, 'DefaultEmail@.email')
    entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.configure(padx=20, pady=20)

canvas_lock = Canvas(width=200, height=200)
image_lock = PhotoImage(file='logo.png')
canvas_lock.create_image(100, 100, image=image_lock)

label_website = Label(text='Website:')
label_website.grid(column=0, row=2)
label_email_username = Label(text='Email/Username:', )
label_email_username.grid(column=0, row=3)
label_password = Label(text='Password:')
label_password.grid(column=0, row=4)

entry_website = Entry(width=41)
entry_website.focus()
entry_website.grid(column=1, row=2, columnspan=2)
entry_email_username = Entry(width=41)
entry_email_username.grid(column=1, row=3, columnspan=2)
entry_email_username.insert(END, 'DefaultEmail@.email')
entry_password = Entry(width=21)
entry_password.grid(column=1, row=4)

button_generate_password = Button(text='Generate Password', command=generate_password)
button_generate_password.grid(column=2, row=4)
button_search_password = Button(text='Search', command=search_entry)
button_search_password.grid(column=3, row=2)
button_save_password = Button(text='Add', width=41, command=save_password)
button_save_password.grid(column=1, row=5, columnspan=2)

canvas_lock.grid(column=1, row=1)
screen.mainloop()
