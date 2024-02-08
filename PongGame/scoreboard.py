from turtle import Turtle

LEFT_X = -50
RIGHT_x = 50


class ScoreBoard(Turtle):
    def __init__(self, l_score, r_score):
        super().__init__()
        self.create_scoreboard(l_score, LEFT_X)
        self.create_scoreboard(r_score, RIGHT_x)

    def create_scoreboard(self, score, x):
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x=x, y=220)
        self.write(f"{score}", True, "center", ("Courier", 40, "normal"))
