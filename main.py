from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Tracer is off so screen only gets updated when we need it to:
screen.tracer(0)

snake = Snake()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
