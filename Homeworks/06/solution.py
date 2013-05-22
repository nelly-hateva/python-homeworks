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

    def __iter__(self):
        return iter((self._x, self._y))

    def __repr__(self):
        return 'Vec2D(%s, %s)' % (self.x, self.y)


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
            ''.join(str(self._cells[x][y]) for x in range(self._width))
            for y in range(self._width)
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
        self.parts = []
        x, y = self.coords
        self.world[x][y].contents = self.head
        #print("head at",x,y)
        for part_num in range(1, size + 1):
            x, y = coords - direction * part_num
            self.parts.append(Vec2D(x, y))
            self.world[x][y].contents = PythonPart()
            #print("part at",x,y)

    def move(self, direction):
        if self.direction == -direction:
            raise ValueError
        self.direction = direction
        newpos = self.coords + direction
        x, y = newpos

        try:
            found = self.world[x][y].contents
        except IndexError:
            raise Death

        if isinstance(found, PythonPart):
            raise Death
        if isinstance(found, Food):
            self.size += 1

        x, y = self.parts.pop()
        self.world[x][y].contents = None
        #print("remove part at",x,y)
        x, y = newpos
        self.world[x][y].contents = self.head
        #print("move head at",x,y)
        x, y = self.coords
        self.world[x][y].contents = PythonPart()
        self.parts.append(Vec2D(x, y))
        #print("part at",x,y)
        for part_num in range(self.size - 1):
            x, y = self.parts.pop(0)
            self.world[x][y].contents = PythonPart()
            self.parts.append(Vec2D(x, y))
            #print("part at",x,y)
        self.coords = newpos


class Death(Exception):
    pass
