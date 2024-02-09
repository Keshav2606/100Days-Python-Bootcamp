from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, score, position):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(f"{score}", False, "center", ("Courier", 40, "normal"))

    def refresh(self, score):
        self.clear()
        self.write(f"{score}", False, "center", ("Courier", 40, "normal"))
