import unittest
import solution


class HoroscopeTest(unittest.TestCase):
    def assert_sign(self, span, name):
        for (start_day, end_day), month in span:
            for day in range(start_day, end_day + 1):
                self.assertEqual(solution.what_is_my_sign(day, month), name)

    def test_aquarius(self):
        self.assert_sign([((20, 31), 1), ((1, 18), 2)], 'Водолей')

    def test_pisces(self):
        self.assert_sign([((19, 29), 2), ((1, 20), 3)], 'Риби')

    def test_aries(self):
        self.assert_sign([((21, 31), 3), ((1, 20), 4)], 'Овен')

    def test_taurus(self):
        self.assert_sign([((21, 30), 4), ((1, 20), 5)], 'Телец')

    def test_gemini(self):
        self.assert_sign([((21, 30), 5), ((1, 20), 6)], 'Близнаци')

    def test_cancer(self):
        self.assert_sign([((21, 30), 6), ((1, 21), 7)], 'Рак')

    def test_leo(self):
        self.assert_sign([((22, 31), 7), ((1, 22), 8)], 'Лъв')

    def test_virgo(self):
        self.assert_sign([((23, 31), 8), ((1, 22), 9)], 'Дева')

    def test_virgo(self):
        self.assert_sign([((23, 30), 9), ((1, 22), 10)], 'Везни')

    def test_scorpio(self):
        self.assert_sign([((23, 31), 10), ((1, 21), 11)], 'Скорпион')

    def test_sagittarius(self):
        self.assert_sign([((22, 30), 11), ((1, 21), 12)], 'Стрелец')

    def test_capricorn(self):
        self.assert_sign([((22, 31), 12), ((1, 19), 1)], 'Козирог')

    def test_living_on_the_edge(self):
        self.assertEqual(solution.what_is_my_sign(20, 6), 'Близнаци')

    def test_sludge(self):
        self.assertEqual(solution.what_is_my_sign(21, 5), 'Близнаци')

    def test_named_arguments(self):
        self.assertEqual(solution.what_is_my_sign(month=6, day=20), 'Близнаци')


if __name__ == '__main__':
    unittest.main()
