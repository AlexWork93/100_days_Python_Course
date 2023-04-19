from tkinter import *
from tkinter import messagebox
import pandas
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
    if is_ok:
        try:
            my_dict = pandas.read_csv('data.csv')
        except:
            my_dict = pandas.DataFrame({'resource': [], 'email': [], 'password': []})
            print("An exception occurred")
        resources = my_dict['resource'].to_list()
        resources.append(website)
        emails = my_dict['email'].to_list()
        emails.append(email)
        passwords = my_dict['password'].to_list()
        passwords.append(password)
        new_dict = {"resource": resources,
                    "email": emails,
                    "password": passwords}

        print(type(resources))
        pandas.DataFrame(new_dict).to_csv("data.csv")
        print("Save")
        clear_entries()


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
button_save_password = Button(text='Add', width=41, command=save_password)
button_save_password.grid(column=1, row=5, columnspan=2)

canvas_lock.grid(column=1, row=1)
screen.mainloop()
