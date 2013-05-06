import turtle
from solution import dragon_fractal


LINE_LENGTH = 1
DELAY_MS = 0
REPEAT_TIMES = 16


def str_to_heading(str_):
    if str_ == 'up':
        return 90
    elif str_ == 'left':
        return 180
    elif str_ == 'right':
        return 0
    elif str_ == 'down':
        return 270
    else:
        raise Exception('Unknown heading {}'.format(str_))

turtle.hideturtle()
turtle.speed(0)
turtle.delay(DELAY_MS)

dragon_iterator = iter(dragon_fractal())
for _ in range(2 ** REPEAT_TIMES):
    step_direction = next(dragon_iterator)
    turtle.setheading(str_to_heading(step_direction))
    turtle.forward(LINE_LENGTH)

turtle.done()
