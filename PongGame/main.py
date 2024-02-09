from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()

l_score = 0
r_score = 0
left_scoreboard = ScoreBoard(l_score, (-50, 220))
right_scoreboard = ScoreBoard(r_score, (50, 220))

screen.listen()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with the paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 360 or ball.distance(left_paddle) < 40 and ball.xcor() < -360:
        ball.paddle_bounce()
        SLEEP_TIME *= 0.9
        left_paddle.y_move += 2
        right_paddle.y_move += 2

    # Detect paddle out of bound
    if ball.xcor() > 380:
        l_score += 1
        ball.home()
        ball.x_move *= -1
        SLEEP_TIME = 0.1
        left_paddle.y_move = 20
        right_paddle.y_move = 20
        left_scoreboard.refresh(l_score)

    elif ball.xcor() < -380:
        r_score += 1
        ball.home()
        ball.x_move *= -1
        SLEEP_TIME = 0.1
        right_scoreboard.refresh(r_score)

