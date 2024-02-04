from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
is_race_on = False
user_bet = screen.textinput("Make a bet.", "Who will win the race? Enter the color: ").lower()
colors = ["red", "blue", "green", "yellow", "orange", "brown"]
y_pos = [-100, -60, -20, 20, 60, 100]
turtles = []

for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winner = None
while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()

if user_bet == winner:
    print("Yay! You Won the bet.")
else:
    print("You lost the bet..")

print(f"{winner.capitalize()} turtle is the Winner.")
