import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")

states = data["state"].tolist()
x_positions = data["x"].tolist()
y_positions = data["y"].tolist()

guessed_states = []
while len(guessed_states) < 50:
    user_input = screen.textinput(f"{len(guessed_states)}/{len(states)}", "Guess the states name?").title()
    if user_input in states:
        guessed_states.append(user_input)
        index = states.index(user_input)
        state_name = turtle.Turtle()
        state_name.ht()
        state_name.penup()
        state_name.goto(x_positions[index], y_positions[index])
        state_name.write(f"{user_input}", False, "center", ("Arial", 12, "normal"))

    elif user_input == "Exit":
        break

missed_states = []
for state in states:
    if state not in guessed_states:
        index = states.index(state)
        missed_states.append(state)

missed_states_df = pd.DataFrame(missed_states)
print(missed_states_df)
missed_states_df.to_csv("states_to_learn.csv")
