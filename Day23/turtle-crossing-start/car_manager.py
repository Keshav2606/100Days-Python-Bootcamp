import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2.0, stretch_wid=1.0)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-200, 200))
        self.setheading(180)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT))
