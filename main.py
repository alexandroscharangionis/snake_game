from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


def create_snake():
    '''Creates snake avatar'''
    # Starting pos for each of the 3 squares that the snake consists of
    starting_position = [0, 0]

    # Creates & places the 3 squares that the snake consists of
    for _ in range(3):
        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.setposition(tuple(starting_position))
        starting_position[0] -= 20


screen.exitonclick()
