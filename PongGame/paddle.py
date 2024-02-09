from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.y_move = 20
        self.shapesize(stretch_len=0.6, stretch_wid=2.5)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 265:
            new_y = self.ycor() + self.y_move
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -265:
            new_y = self.ycor() - self.y_move
            self.goto(self.xcor(), new_y)
