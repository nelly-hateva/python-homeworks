from itertools import product


class TicTacToeBoard:
    COLUMNS = ('1', '2', '3')
    ROWS = ('A', 'B', 'C')
    WINNING_TRIPLES = (('A1', 'A2', 'A3'),
                       ('B1', 'B2', 'B3'),
                       ('C1', 'C2', 'C3'),
                       ('A1', 'B1', 'C1'),
                       ('A2', 'B2', 'C2'),
                       ('A3', 'B3', 'C3'),
                       ('A1', 'B2', 'C3'),
                       ('A3', 'B2', 'C1'))
    VALUES = ('X', 'O')
    GAME_IN_PROGRESS = 'Game in progress.'
    DRAW = 'Draw!'
    X_WINS = 'X wins!'
    O_WINS = 'O wins!'
    EMPTY = ' '
    BOARD_REPRESENTATION = '\n  -------------\n' +\
                           '3 | {A3} | {B3} | {C3} |\n' +\
                           '  -------------\n' +\
                           '2 | {A2} | {B2} | {C2} |\n' +\
                           '  -------------\n' +\
                           '1 | {A1} | {B1} | {C1} |\n' +\
                           '  -------------\n' +\
                           '    A   B   C  \n'

    def __init__(self):
        self.KEYS = [''.join(coordinates)
                     for coordinates in product(self.ROWS, self.COLUMNS)]
        self.board = dict.fromkeys(self.KEYS, self.EMPTY)
        self.filled_cells = 0
        self.last_player = None
        self.status = self.GAME_IN_PROGRESS

    def __setitem__(self, key, value):
        if key not in self.KEYS:
            raise InvalidKey()
        if value not in self.VALUES:
            raise InvalidValue()
        if self.board[key] != self.EMPTY:
            raise InvalidMove()
        if self.last_player is None:
            self.last_player = value
        elif self.last_player == value:
            raise NotYourTurn()
        self.board[key] = value
        self.last_player = value
        self.filled_cells += 1

    def __getitem__(self, key):
        if key not in self.KEYS:
            raise InvalidKey()
        return self.board[key]

    def __str__(self):
        return self.BOARD_REPRESENTATION.format(**self.board)

    def game_status(self):
        if self.winner('X'):
            return self.X_WINS
        elif self.winner('O'):
            return self.O_WINS
        elif self.filled_cells == 9:
            return self.DRAW
        else:
            return self.GAME_IN_PROGRESS

    def winner(self, gamer):
        for triple in iter(self.WINNING_TRIPLES):
            first, second, third = triple
            if self.board[first] == self.board[second] == \
               self.board[third] == gamer:
                return True
        return False


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
