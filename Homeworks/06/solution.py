from random import randint, choice


class Vec2D:
    def __init__(self, x, y):
        self._x, self._y = x, y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        if isinstance(other, Vec2D):
            return Vec2D(self._x + other.x, self._y + other.y)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vec2D):
            return Vec2D(self._x - other.x, self._y - other.y)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2D(self._x * other, self._y * other)
        else:
            raise TypeError
    __rmul__ = __mul__

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __eq__(self, other):
        if isinstance(other, Vec2D):
            return self._x == other.x and self._y == other.y
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Vec2D):
            return self._x != other.x or self._y != other.y
        else:
            return False

    def __repr__(self):
        return 'Vec2d(%s, %s)' % (self.x, self.y)

    def __iter__(self):
        return iter((self._x, self._y))


class WorldObject:
    pass


class Cell:
    def __init__(self, contents=None):
        if isinstance(contents, WorldObject) or contents is None:
            self._contents = contents
        else:
            raise TypeError

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if isinstance(value, WorldObject) or value is None:
            self._contents = value
        else:
            raise TypeError

    def is_empty(self):
        return self.contents is None

    def __str__(self):
        return ".." if self.is_empty() else str(self.contents)


class Food(WorldObject):
    def __init__(self, energy):
        self.energy = energy

    def __str__(self):
        return "AA"


class World():
    class Column:
        def __init__(self, width):
            self._data = [Cell() for _ in range(width)]
            self._width = width

        @property
        def width(self):
            return self._width

        @property
        def data(self):
            return self._data

        def __getitem__(self, key):
            if not isinstance(key, int):
                raise TypeError
            if key not in range(self.width):
                raise IndexError

            return self.data[key]

        def __setitem__(self, key, value):
            if not isinstance(key, int):
                raise TypeError
            if key not in range(self.width):
                raise IndexError

            self.data[key] = value

    def __init__(self, width):
        self._width = width
        self._cells = [World.Column(width) for _ in range(width)]

    @property
    def width(self):
        return self._width

    @property
    def cells(self):
        return self._cells

    def __len__(self):
        return self.width

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key not in range(self.width):
            raise IndexError

        return self.cells[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError
        if key not in range(self.width):
            raise IndexError

        self.cells[index] = value

    def __str__(self):
        rows = (
            ''.join(str(self.cells[x][y]) for x in range(self.width))
            for y in range(self.width)
        )
        return '\n'.join(rows)


class PythonPart(WorldObject):
    def __str__(self):
        return "##"


class PythonHead(PythonPart):
    def __str__(self):
        return "@@"


class Python:
    LEFT = Vec2D(-1, 0)
    RIGHT = Vec2D(1, 0)
    UP = Vec2D(0, -1)
    DOWN = Vec2D(0, 1)

    def __init__(self, world, coords, size, direction):
        self.world = world
        self.coords = coords
        self.size = size
        self.direction = direction

        self.head = PythonHead()
        x, y = coords
        self.world[x][y].contents = self.head
        for part_num in range(1, size + 1):
            x, y = coords - direction * part_num
            self.world[x][y].contents = PythonPart()

    def move(self, direction):
        if self.direction == -direction:
            raise ValueError
        self.direction = direction
        self.coords += direction
        x, y = self.coords
        try:
            found = self.world[x][y].contents
        except IndexError:
            raise Death

        if isinstance(found, PythonPart):
            raise Death
        if isinstance(found, Food):
            self.size += 1
        self.world[x][y].contents = self.head


class Death(Exception):
    pass
