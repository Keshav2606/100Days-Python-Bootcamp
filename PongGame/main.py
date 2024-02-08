from turtle import Screen
from paddle import Paddle
from separator import Separator
from scoreboard import ScoreBoard
from ball import Ball

LEFT = -390
RIGHT = 390

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()

y_pos = [300, 250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250, -300]
for pos in y_pos:
    separator = Separator()
    separator.goto(x=0, y=pos)

l_score = 0
r_score = 0
scoreboard = ScoreBoard(l_score, r_score)
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()

    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(left_paddle.go_down, "s")
    screen.onkey(right_paddle.go_down, "Down")

screen.exitonclick()
