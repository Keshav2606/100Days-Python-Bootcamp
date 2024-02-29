import pandas as pd
from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B2F3FF"


def check_answer():
    global random_word
    if user_input.get().lower() != random_word["English"].lower():
        show_answer()
    to_learn.remove(random_word)
    random_word = random.choice(to_learn)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(word, text=random_word["Spanish"], fill="black")
    user_input.delete(0, END)


def show_answer():
    messagebox.showinfo(title="Warning", message=f"Wrong Answer!\nRight Answer is: {random_word['English']}")


data = pd.read_csv("./data/Spanish_most_frequent_words.csv")
to_learn = data.to_dict(orient="records")
random_word = random.choice(to_learn)

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)

title = canvas.create_text(400, 150, text="Spanish", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=f"{random_word['Spanish']}", font=("Arial", 60, "bold"))
user_input = Entry()
canvas.create_window(400, 376, window=user_input)
canvas.grid(column=0, row=0, columnspan=2)

dont_know_btn = Button(text="Don't Know", command=show_answer)
dont_know_btn.config(pady=2, padx=2)
dont_know_btn.grid(column=0, row=1)

submit_btn = Button(text="Submit", command=check_answer)
submit_btn.config(pady=2, padx=2)
submit_btn.grid(column=1, row=1)

window.mainloop()
