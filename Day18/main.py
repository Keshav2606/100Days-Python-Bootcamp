from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colors = ["blue", "aqua", "green", "yellow", "brown", "cyan", "orange", "violet"]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for sides in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()
