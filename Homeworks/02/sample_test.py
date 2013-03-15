import unittest

import solution


class GroupByTest(unittest.TestCase):

    def assert_group_by(self, func, seq, result):
        self.assertEqual(solution.groupby(func, seq), result)

    def test_group_by_main_workflow(self):
        self.assert_group_by(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7],
                             {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]})

    def test_group_by_with_empty_seq(self):
        self.assert_group_by(lambda x: x % 2, [], {})

    def test_group_by_with_one_group(self):
        self.assert_group_by(lambda x: 3, [0, 1, 2, 3, 4, 5, 6, 7],
                             {3: [0, 1, 2, 3, 4, 5, 6, 7]})

    def test_group_by_with_unique_groups(self):
        self.assert_group_by(lambda x: x, [0, 1, 2, 3, 4, 5, 6, 7],
                             {0: [0], 1: [1], 2: [2], 3: [3], 4: [4],
                              5: [5], 6: [6], 7: [7]})

    def test_group_by_with_duplicate_values(self):
        self.assert_group_by(lambda x: x % 2, [0, 1, 1, 2, 3, 4, 5, 5, 6, 7],
                             {0: [0, 2, 4, 6], 1: [1, 1, 3, 5, 5, 7]})

    def test_groupby_odd_and_even(self):
        expected = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        actual = solution.groupby(lambda x: 'odd' if x % 2 else 'even',
                                  [1, 2, 3, 5, 8, 9, 10, 12])
        self.assertEqual(expected, actual)


class IterateTest(unittest.TestCase):

    def test_iterate_ordered_calls_one(self):
        powers_of_two = solution.iterate(lambda x: x * 2)
        f = next(powers_of_two)
        self.assertEqual(3, f(3))
        f = next(powers_of_two)
        self.assertEqual(6, f(3))
        f = next(powers_of_two)
        self.assertEqual(12, f(3))
        f = next(powers_of_two)
        self.assertEqual(24, f(3))

    def test_iterate_ordered_calls_two(self):
        powers_of_two = solution.iterate(lambda x: x * 2)
        f = next(powers_of_two)
        self.assertEqual(1 * 'eggs', f('eggs'))
        f = next(powers_of_two)
        self.assertEqual(2 * 'ham', f('ham'))
        f = next(powers_of_two)
        self.assertEqual(4 * 'spam', f('spam'))
        f = next(powers_of_two)
        self.assertEqual(8 * 'spameggs', f('spameggs'))

    def iterate(self, func, times, param):
        i = solution.iterate(func)
        for t in range(-1, times):
            result = next(i)(param)
        return result

    def assert_iterate(self, func, times, param, result):
        self.assertEqual(self.iterate(func, times, param), result)

    def test_iterate_identity(self):
        self.assert_iterate(lambda x: x ** 3, 0, 3, 3)

    def test_iterate_composition(self):
        for i in range(0, 10):
            self.assert_iterate(lambda x: 2 * x, i, 3, (2 ** i) * 3)

    def test_iterate_param_count(self):
        self.assert_iterate(lambda: 3, 0, 3, 3)


class ZipWithTest(unittest.TestCase):

    def assert_zip_with(self, func, iterables, result):
        self.assertEqual(list(solution.zip_with(func, *iterables)), result)

    def test_zip_with_equal_iterables_len(self):
        self.assert_zip_with(lambda x, y, z: x + y + z,
                             [['John', 'Miles'],
                             [' '] * 2,
                             ['Coltrane', 'Davis']],
                             ['John Coltrane', 'Miles Davis'])

    def test_zip_with_different_iterables_len(self):
        self.assert_zip_with(lambda x, y, z: x + y + z,
                             [['John'],
                             [' '] * 2,
                             ['Coltrane', 'Davis', 'Grohl']],
                             ['John Coltrane'])

    def test_zip_without_iterables(self):
        self.assert_zip_with(lambda: 3, [], [])

    def test_zip_with_simple(self):
        first_names = ['Charlie', 'Dizzy']
        last_names = ['Parker', 'Gillespie']
        expected = ['CharlieParker', 'DizzyGillespie']
        actual = solution.zip_with(str.__add__, first_names, last_names)
        self.assertEqual(expected, list(actual))


class CacheTest(unittest.TestCase):

    def test_cache_call_is_cached(self):
        call_count = 0

        def double(x):
            nonlocal call_count
            call_count += 1
            return 2 * x

        cached_double = solution.cache(double, 10)
        self.assertEqual(256, cached_double(128))
        self.assertEqual(256, cached_double(128))
        self.assertEqual(1, call_count)

    def test_cache_size(self):
        call_count = 0

        def inc(x):
            nonlocal call_count
            call_count += 1
            return x + 1

        cached_inc = solution.cache(inc, 2)
        self.assertEqual(2, cached_inc(1))
        self.assertEqual(2, cached_inc(1))
        self.assertEqual(1, call_count)

        self.assertEqual(5, cached_inc(4))
        self.assertEqual(5, cached_inc(4))
        self.assertEqual(2, call_count)

        self.assertEqual(2, cached_inc(1))
        self.assertEqual(2, cached_inc(1))
        self.assertEqual(2, call_count)

        self.assertEqual(1, cached_inc(0))
        self.assertEqual(1, cached_inc(0))
        self.assertEqual(3, call_count)

        self.assertEqual(2, cached_inc(1))
        self.assertEqual(2, cached_inc(1))
        self.assertEqual(4, call_count)

    def test_cache_two_arguments(self):
        call_count = 0

        def mult(x, y):
            nonlocal call_count
            call_count += 1
            return x * y

        cached_mult = solution.cache(mult, 10)
        self.assertEqual(2, cached_mult(1, 2))
        self.assertEqual(2, cached_mult(1, 2))
        self.assertEqual(1, call_count)

        self.assertEqual(6, cached_mult(3, 2))
        self.assertEqual(6, cached_mult(3, 2))
        self.assertEqual(2, call_count)

if __name__ == "__main__":
    unittest.main()
