from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


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
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
