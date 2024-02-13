from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset_func():
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"

    if min < 10:
        min = f"0{min}"

    time = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        REPS += 1


def start_func():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS == 8:
        count_down(long_break_sec)
    elif REPS % 2 != 0:
        count_down(work_sec)
    elif REPS % 2 == 0:
        count_down(short_break_sec)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", command=start_func, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", command=reset_func, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
