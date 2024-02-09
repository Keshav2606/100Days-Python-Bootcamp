from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.ht()
        self.level = level + 1
        self.penup()
        self.goto((-200, 250))
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", ("Courier", 30, "normal"))
