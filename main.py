from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Tracer is off so screen only gets updated when we need it to:
screen.tracer(0)


def create_snake():
    '''Builds snake avatar. Returns list of snake segments.'''
    # Starting pos for each of the 3 squares that the snake consists of
    starting_position = [0, 0]
    snake_segments = []
    # Creates & places the 3 squares that the snake consists of
    for _ in range(3):
        segment = Turtle(shape='square')
        segment.penup()
        segment.color('white')
        segment.setposition(tuple(starting_position))
        snake_segments.append(segment)
        starting_position[0] -= 20
    return snake_segments


game_is_on = True
segments = create_snake()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Starting from the last segment (back of the snake), move each segment to the position of the segment in front of it (like a real worm would move)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

screen.exitonclick()
