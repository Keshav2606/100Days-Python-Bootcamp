from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.clipboard_clear()
    password_input.clipboard_append(password)
    password_input.delete(0, END)
    password_input.insert(0, f"{password_input.clipboard_get()}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    message = f'''These are the data Entered:
Email: {email_input.get()}
Password: {password_input.get()}
Is this Okay?'''
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

    }}

    if len(website_input.get()) < 1 or len(password_input.get()) < 1:
        messagebox.showinfo(title="Oops..", message="Please make sure you haven't left any field empty.")
    else:
        is_okay = messagebox.askyesno(f"{website_input.get()}", message)

        if is_okay:
            with open("password_file.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)

            print("Password Saved Successfully.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1, sticky="e")
website_label.config(padx=10, pady=10)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username: ", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2, sticky="e")
email_label.config(padx=10, pady=10)

email_input = Entry(width=40)
email_input.insert(0, "mishraji2606@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3, sticky="e")
password_label.config(padx=10, pady=10)

password_input = Entry(width=40)
password_input.grid(column=1, row=3, columnspan=2)

passwd_generate_btn = Button(text="Generate Password", command=generate_password)
passwd_generate_btn.grid(column=1, row=4)

add_btn = Button(text="ADD", width=15, command=save_password, bg="blue", fg="white")
add_btn.grid(column=2, row=4, sticky="w")

window.mainloop()
