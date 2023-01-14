from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Tracer is off so screen only gets updated when we need it to:
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision between snake and food:
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
