from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(x=0, y=270)
        arg = f"Score: {self.score}"
        self.write(arg, move=True, align="center", font=('Courier', 16, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", True, "center",('Courier', 30, 'normal'))
