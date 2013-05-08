from itertools import count as count

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
ROTATED = {UP: LEFT, DOWN: RIGHT, LEFT: DOWN, RIGHT: UP}


def dragon_fractal():
    grapfic = []
    yield UP
    grapfic.append(UP)

    while True:
        for j in count(0):
            for i in range(2 ** j - 1, -1, -1):
                line = grapfic[i]
                yield ROTATED[line]
                grapfic.append(ROTATED[line])
