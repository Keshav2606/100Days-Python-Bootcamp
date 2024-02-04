from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

screen.listen()


def mov_forward():
    timmy.forward(10)


def mov_backward():
    timmy.back(10)


def mov_clockwise():
    timmy.right(5)


def mov_counterclockwise():
    timmy.left(5)


def reset():
    screen.reset()


screen.onkey(key="w", fun=mov_forward)
screen.onkey(key="s", fun=mov_backward)
screen.onkey(key="d", fun=mov_clockwise)
screen.onkey(key="a", fun=mov_counterclockwise)
screen.onkey(reset, "c")

screen.exitonclick()
