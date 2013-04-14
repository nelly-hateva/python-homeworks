import unittest
import solution


class TicTacHomeworkTest(unittest.TestCase):
    def test_empty(self):
        b = solution.TicTacToeBoard()
        empty_board = '\n  -------------\n' +\
            '3 |   |   |   |\n' +\
            '  -------------\n' +\
            '2 |   |   |   |\n' +\
            '  -------------\n' +\
            '1 |   |   |   |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

        self.assertEqual(empty_board, b.__str__())

    def test_full(self):
        d = solution.TicTacToeBoard()
        full_board = '\n  -------------\n' +\
            '3 | O | O | X |\n' +\
            '  -------------\n' +\
            '2 | X | X | O |\n' +\
            '  -------------\n' +\
            '1 | O | X | O |\n' +\
            '  -------------\n' +\
            '    A   B   C  \n'

        d["A1"] = 'O'
        d["B1"] = 'X'
        d["A3"] = 'O'
        d["A2"] = 'X'
        d["C2"] = 'O'
        d["C3"] = 'X'
        d["B3"] = 'O'
        d["B2"] = 'X'
        d["C1"] = 'O'

        self.assertEqual(full_board, d.__str__())

    def test_input_format(self):
        o = solution.TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            o['Magadan'] = 'X'

    def test_x_wins(self):
        h = solution.TicTacToeBoard()
        h["A1"] = 'X'
        h["A2"] = 'O'
        h["B1"] = 'X'
        h["A3"] = 'O'
        h["C1"] = 'X'

        self.assertEqual('X wins!', h.game_status())

    def test_o_wins(self):
        # Vertical win
        v = solution.TicTacToeBoard()
        v["A1"] = 'O'
        v["B2"] = 'X'
        v["A2"] = 'O'
        v["B3"] = 'X'
        v["A3"] = 'O'

        self.assertEqual('O wins!', v.game_status())

    def test_draw(self):
        d = solution.TicTacToeBoard()
        d["A1"] = 'O'
        d["B1"] = 'X'
        d["A3"] = 'O'
        d["A2"] = 'X'
        d["C2"] = 'O'
        d["C3"] = 'X'
        d["B3"] = 'O'
        d["B2"] = 'X'
        d["C1"] = 'O'

        self.assertEqual('Draw!', d.game_status())

    def test_game_in_progress(self):
        p = solution.TicTacToeBoard()
        p["A1"] = 'X'
        p["A3"] = 'O'

        self.assertEqual('Game in progress.', p.game_status())

    def test_invalid_value_exception_raises(self):
        invalid_value = solution.TicTacToeBoard()
        with self.assertRaises(solution.InvalidValue):
            invalid_value["A1"] = "F"

    def test_invalid_key_exception_raises(self):
        invalid_key = solution.TicTacToeBoard()
        with self.assertRaises(solution.InvalidKey):
            invalid_key["A51"] = "X"

    def test_invalid_move_exception_raises(self):
        invalid_move = solution.TicTacToeBoard()
        with self.assertRaises(solution.InvalidMove):
            invalid_move["A1"] = "X"
            invalid_move["A1"] = "O"

    def test_not_your_turn_exception_raises(self):
        not_your_turn = solution.TicTacToeBoard()
        with self.assertRaises(solution.NotYourTurn):
            not_your_turn["A1"] = "X"
            not_your_turn["A2"] = "X"

    def test_not_your_turn_exception_raises_two(self):
        not_your_turn = solution.TicTacToeBoard()
        with self.assertRaises(solution.NotYourTurn):
            not_your_turn["A1"] = "O"
            not_your_turn["A2"] = "O"

if __name__ == '__main__':
    unittest.main()
