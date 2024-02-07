import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def coordinates(self):
        xcor = self.xcor()
        ycor = self.ycor()
        coord = (xcor, ycor)
        return coord
