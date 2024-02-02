import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.width(8)
timmy.speed(10)
colors = ["blue", "aqua", "green", "IndianRed", "pink", "cyan", "orange", "violet"]
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))