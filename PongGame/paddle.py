from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.6, stretch_wid=2.5)
        self.goto(x=coor[0], y=coor[1])

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
