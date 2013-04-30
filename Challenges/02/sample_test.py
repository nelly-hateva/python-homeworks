import unittest
import solution


class DragonFractalTests(unittest.TestCase):

    def test_dragon_fractal(self):
        dragon = solution.dragon_fractal()
        self.assertEqual('up', next(dragon))
        self.assertEqual('left', next(dragon))
        self.assertEqual('down', next(dragon))
        self.assertEqual('left', next(dragon))
        self.assertEqual('down', next(dragon))

if __name__ == '__main__':
    unittest.main()
