from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
score_board = ScoreBoard()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score_board.score += 1
        score_board.refresh()
        snake.extend()
        food.goto(random.randint(-280, 280), random.randint(-280, 260))

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            is_game_on = False
            score_board.game_over()
