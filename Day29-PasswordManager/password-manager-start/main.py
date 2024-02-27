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
    website = website_input.get().capitalize()
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
        is_okay = messagebox.askyesno(f"{website_input.get()}",
                                      f"These are the data Entered:\nEmail: {email_input.get()}\nPassword: {password_input.get()}\nIs this Okay?")

        if is_okay:
            with open("password_file.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)

            with open("password_file.json", mode="w") as file:
                json.dump(data, file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)

            print("Password Saved Successfully.")


def search():
    website_name = website_input.get().capitalize()
    with open("password_file.json", mode="r") as file:
        data_dict = json.load(file)
        try:
            email = data_dict[website_name]["email"]
            passwd = data_dict[website_name]["password"]
        except KeyError:
            messagebox.showinfo("Details", "Data regarding website is not Available.")
        else:
            messagebox.showinfo("Details", f"Website: {website_name}\nEmail Id: {email}\nPassword: {passwd}")


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

website_input = Entry(width=34)
website_input.grid(column=1, row=1)
website_input.focus()

search_btn = Button(text="Search", command=search)
search_btn.config(padx=30, pady=1)
search_btn.grid(column=2, row=1, sticky="e")

email_label = Label(text="Email/Username: ", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2, sticky="e")
email_label.config(padx=10, pady=10)

email_input = Entry(width=60)
email_input.insert(0, "mishraji2606@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky="w")

password_label = Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3, sticky="e")
password_label.config(padx=10, pady=10)

password_input = Entry(width=34)
password_input.grid(column=1, row=3, columnspan=1)

passwd_generate_btn = Button(text="Generate Password", command=generate_password)
passwd_generate_btn.grid(column=2, row=3, sticky="e")

add_btn = Button(text="ADD", width=50, command=save_password, bg="blue", fg="white")
add_btn.config(padx=3, pady=1)
add_btn.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
