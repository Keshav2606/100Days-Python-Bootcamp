import random
import turtle as t

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

t.colormode(255)
timmy = t.Turtle()
timmy.width(8)
timmy.speed("fastest")
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.pencolor(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))