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
        print(py.dump_world())
        self.assertIsInstance(world[10][10].contents, PythonHead)

        position = Vec2D(10, 10)
        for part_num in range(py_size):
            x, y = position - direction
            self.assertIsInstance(world[x][y].contents, PythonPart)


if __name__ == '__main__':
    unittest.main()
