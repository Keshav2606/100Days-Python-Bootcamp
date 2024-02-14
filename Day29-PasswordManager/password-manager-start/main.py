from tkinter import *
from tkinter import ttk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    new_window = Toplevel(window)
    new_window.title(website_input.get())
    new_window.config(padx=12, pady=12)
    new_window.minsize(200, 100)
    confirm_email = Label(new_window, text=f"Email: {email_input.get()}")
    confirm_email.grid(column=0, row=0, sticky="w")
    confirm_password = Label(new_window, text=f"Password: {password_input.get()}")
    confirm_password.grid(column=0, row=1, sticky="w")
    confirm_label = Label(new_window, text="Is this Okay?")
    confirm_label.grid(column=0, row=2, sticky="w")
    yes_btn = Button(new_window, text="Yes", command=save_password)
    yes_btn.config(padx=8, pady=2, fg="white", bg="blue")
    yes_btn.grid(column=2, row=3)
    no_btn = Button(new_window, text="No", command=new_window.destroy)
    no_btn.config(padx=8, pady=2)
    no_btn.grid(column=1, row=3)


def save_password():
    with open("password_file.txt", mode="w") as file:
        file.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=100, pady=100)

canvas = Canvas(width=100, height=100, bg="#f7f5dd")
logo = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)
website_label.config(padx=10, pady=10)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username: ", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2)
email_label.config(padx=10, pady=10)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=10)

password_input = Entry(width=15)
password_input.grid(column=1, row=3)

passwd_generate_btn = Button(text="Generate Password")
passwd_generate_btn.grid(column=2, row=3)

add_btn = Button(text="ADD", width=35, command=add, bg="blue", fg="white")
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
