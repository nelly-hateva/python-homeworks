import unittest
from random import randint, shuffle, choice
from solution import *


class Vector2DTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Vec2D(3, 4) + Vec2D(5, 6), Vec2D(8, 10))
        with self.assertRaises(TypeError):
            Vec2D(3, 4) + 5
        with self.assertRaises(TypeError):
            3.14 + Vec2D(0, 0)

    def test_substraction(self):
        self.assertEqual(Vec2D(3, 4) - Vec2D(5, 6), Vec2D(-2, -2))
        with self.assertRaises(TypeError):
            Vec2D(3, 4) - 5
        with self.assertRaises(TypeError):
            900 - Vec2D(3, 4)

    def test_multiplication(self):
        self.assertEqual(2 * Vec2D(3, 4), Vec2D(6, 8))
        self.assertEqual(Vec2D(3, 4) * 2, Vec2D(6, 8))
        with self.assertRaises(TypeError):
            Vec2D(3, 4) * Vec2D(5, 6)

    def test_negation(self):
        self.assertEqual(Vec2D(1, 1), -Vec2D(-1, -1))


class WorldTest(unittest.TestCase):
    def test_bigbang(self):
        world = World(10)
        self.assertEqual(len(world), 10)

        bigworld = World(100)
        self.assertEqual(len(bigworld), 100)

    def test_world_indexing(self):
        world = World(10)
        with self.assertRaises(IndexError):
            cell = world[10][10]
        with self.assertRaises(IndexError):
            cell = world[5][1337]
        with self.assertRaises(IndexError):
            cell = world[1337]
        with self.assertRaises(IndexError):
            cell = world[1337][1337]

        row, col = randint(0, 9), randint(0, 9)
        self.assertIsInstance(world[row][col], Cell)

    def test_world_manipulation(self):
        world = World(10)
        row, col = randint(0, 9), randint(0, 9)
        world[row][col] = Cell(Food(energy=5))

        self.assertFalse(world[row][col].is_empty())
        self.assertEqual(world[row][col].contents.energy, 5)

        world[row][col] = Cell(PythonHead())
        self.assertFalse(world[row][col].is_empty())
        self.assertIsInstance(world[row][col].contents, PythonHead)

        world[row][col] = Cell(PythonPart())
        self.assertFalse(world[row][col].is_empty())
        self.assertIsInstance(world[row][col].contents, PythonPart)

    def test_cell(self):
        cell = Cell(Food(energy=5))
        self.assertFalse(cell.is_empty())
        self.assertEqual(cell.contents.energy, 5)

    def test_cell_empty(self):
        emptycell = Cell()
        self.assertTrue(emptycell.is_empty())

    def test_cell_invalid(self):
        with self.assertRaises(TypeError):
            badcell = Cell("snakesandladders")


class PythonTest(unittest.TestCase):
    def test_python_placement(self):
        directions = [Python.UP, Python.DOWN, Python.LEFT, Python.RIGHT]
        direction = choice(directions)

        world = World(25)
        py_size = randint(3, 5)
        py = Python(world, Vec2D(10, 10), py_size, direction)
        self.assertIsInstance(world[10][10].contents, PythonHead)

        position = Vec2D(10, 10)
        for part_num in range(1, py_size + 1):
            x, y = position - direction * part_num
            self.assertIsInstance(world[x][y].contents, PythonPart)

    def test_python_movement_basic(self):
        directions = [Python.UP, Python.DOWN, Python.LEFT, Python.RIGHT]
        direction = choice(directions)

        world = World(25)
        py_size = randint(3, 5)
        py = Python(world, Vec2D(10, 10), py_size, direction)
        self.assertIsInstance(world[10][10].contents, PythonHead)
        py.move(direction)
        x, y = Vec2D(10, 10) + direction

        self.assertIsInstance(world[x][y].contents, PythonHead)
        for part_num in range(1, py_size + 1):
            x, y = Vec2D(10, 10) + direction - direction * part_num
            self.assertIsInstance(world[x][y].contents, PythonPart)
        #self.assertEqual(world[][], None)

    def test_move_backwards(self):
        directions = [Python.UP, Python.DOWN, Python.LEFT, Python.RIGHT]
        direction = choice(directions)

        world = World(20)
        py_size = randint(3, 5)
        py = Python(world, Vec2D(10, 10), py_size, direction)

        py.move(direction)
        with self.assertRaises(ValueError):
            py.move(-direction)

    def test_wallpunch_death(self):
        world = World(20)
        py = Python(world, Vec2D(5, 5), 3, Python.LEFT)

        with self.assertRaises(Death):
            {py.move(Python.LEFT) for repeat in range(0, 10)}

    def test_growth(self):
        world = World(20)
        py = Python(world, Vec2D(10, 10), 3, Python.LEFT)
        food = Food(energy=5)
        world[8][10] = Cell(food)

        py.move(Python.LEFT)
        self.assertEqual(py.size, 3)

        py.move(Python.LEFT)
        self.assertIsInstance(world[8][10].contents, PythonHead)
        self.assertEqual(py.size, 4)

    def test_ouroboros_death(self):
        world = World(25)
        py = Python(world, Vec2D(10, 10), 5, Python.LEFT)
        py.move(Python.LEFT)
        py.move(Python.UP)
        py.move(Python.UP)
        py.move(Python.RIGHT)

        with self.assertRaises(Death):
            py.move(Python.DOWN)
            py.move(Python.DOWN)

    def test_snake_death(self):
        world = World(20)
        py1 = Python(world, Vec2D(5, 5), 3, Python.LEFT)
        py2 = Python(world, Vec2D(5, 8), 3, Python.RIGHT)

        with self.assertRaises(Death):
            {py2.move(Python.UP) for repeat in range(0, 5)}


if __name__ == '__main__':
    unittest.main()
