import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

level = 0

player = Player()
scoreboard = Scoreboard(level)

screen.onkey(player.move, "Up")


is_game_on = True
loop_count = 0
cars = []
while is_game_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        scoreboard.level_up()
        player.goto((0, -280))

    if loop_count % 6 == 0:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.move(level)
        if car.distance(player) < 30:
            player.home()
            player.write("Game Over.", False, "center", ("Courier", 24, "normal"))
            is_game_on = False

    loop_count += 1

screen.exitonclick()
