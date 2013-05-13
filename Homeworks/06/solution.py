class WorldObject:
    pass


class Cell:
    def __init__(self, contents=None):
        if isinstance(contents, WorldObject) or contents is None:
            self.contents = contents
        else:
            raise TypeError

    def contents(self):
        return self.contents

    def is_empty(self):
        return self.contents is None


class World():
    def __init__(self, width):
        self.width = width
        self.cells = [[Cell()] * width] * width

    def __len__(self):
        return self.width

    def __getitem__(self, index):
        if index < 0 or index > self.width:
            raise IndexError
        else:
            return self.cells[index]


class Vec2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def __iter__(self):
        yield self.x
        yield self.y


class PythonPart(WorldObject):
    pass


class PythonHead(PythonPart):
    pass


class Python:
    LEFT = Vec2D(-1, 0)
    RIGHT = Vec2D(1, 0)
    UP = Vec2D(0, 1)
    DOWN = Vec2D(0, -1)

    def __init__(self, world, coords, size, direction):
        self.world = world
        self.coords = coords
        self.size = size
        self.direction = direction
        self.head = PythonHead()

    def move(self, direction):
        pass


class Food(WorldObject):
    def __init__(self, energy):
        self.energy = energy


class Death(Exception):
    pass
