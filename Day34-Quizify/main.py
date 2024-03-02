import requests
import random
import html
from tkinter import *
from tkinter import messagebox


question = ""
correct_answer = ""
score = 0
ques_count = 0

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()
questions_list = data["results"]


def next_question():
    global question, correct_answer
    current_question_data = random.choice(questions_list)
    questions_list.remove(current_question_data)
    question = html.unescape(current_question_data["question"])
    correct_answer = current_question_data["correct_answer"]
    canvas.config(bg="white")
    canvas.itemconfig(question_text, text=question)


def true_answer_check():
    global score, ques_count
    if correct_answer == "True":
        canvas.config(bg="Green")
        score += 1
    else:
        canvas.config(bg="red")

    ques_count += 1
    score_label.config(text=f"Score: {score}/{ques_count}")
    if ques_count < 10:
        window.after(2000, func=next_question)
    else:
        messagebox.showinfo("Quiz Finished.", f"You Completed the Quiz\nYou Final Score is: {score}/{ques_count}")


def false_answer_check():
    global score, ques_count
    if correct_answer == "False":
        canvas.config(bg="green")
        score += 1

    else:
        canvas.config(bg="red")

    ques_count += 1
    score_label.config(text=f"Score: {score}/{ques_count}")
    if ques_count < 10:
        window.after(2000, func=next_question)
    else:
        messagebox.showinfo("Quiz Finished.", f"You Completed the Quiz\nYou Final Score is: {score}/{ques_count}")


window = Tk()
window.title("Quizify")
window.config(padx=20, pady=20, bg="#375362")


score_label = Label(text=f"Score: {score}")
score_label.config(padx=20, pady=20, bg="#375362", fg="white")
score_label.grid(column=1, row=0)

canvas = Canvas(width=300, height=250)
canvas.config()
question_text = canvas.create_text(150, 125, width=280, text=question, font=("Arial", 20, "italic"))
canvas.grid(column=0, row=1, columnspan=2)

true_btn = Button(text="True", command=true_answer_check)
true_btn.config(pady=4, padx=4, bg="green", fg="white")
true_btn.grid(column=1, row=2, pady=12)

false_btn = Button(text="False", command=false_answer_check)
false_btn.config(pady=4, padx=4, bg="red", fg="white")
false_btn.grid(column=0, row=2, pady=12)

next_question()

window.mainloop()
