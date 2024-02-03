import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)
timmy.home()
timmy.speed(13)
timmy.color("purple")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)
screen.exitonclick()
