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

with open("highscore.txt") as file:
    highscore = int(file.read())

score_board = ScoreBoard(highscore)

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        score_board.score += 1
        score_board.update_score()
        snake.extend()
        food.goto(random.randint(-280, 280), random.randint(-280, 260))

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        score_board.restart()
        with open("highscore.txt", mode="w") as file:
            file.write(str(score_board.highscore))

    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 10:
            snake.reset()
            score_board.restart()
            with open("highscore.txt", mode="w") as file:
                file.write(str(score_board.highscore))
