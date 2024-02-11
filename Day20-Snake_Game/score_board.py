from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, highscore):
        super().__init__()
        self.score = 0
        self.highscore = highscore
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=0, y=270)
        arg = f"Score: {self.score} High Score: {self.highscore}"
        self.write(arg, move=True, align="center", font=('Courier', 16, 'normal'))

    def restart(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()
