class TicTacToeBoard:

    def __init__(self):
        self.board = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                      'B1': ' ', 'B2': ' ', 'B3': ' ',
                      'C1': ' ', 'C2': ' ', 'C3': ' '}
        self.valid_keys = ('A1', 'A2', 'A3',
                           'B1', 'B2', 'B3',
                           'C1', 'C2', 'C3')
        self.valid_values = ('X', 'O')
        self.filled_cells = 0
        self.turn = 'unknown'

    def __setitem__(self, index, item):
        if index not in self.valid_keys:
            raise InvalidKey('Invalid key!')
        if item not in self.valid_values:
            raise InvalidValue('Invalid value!')
        if self.board[index] != ' ':
            raise InvalidMove('Invalid move!')
        if self.turn == 'unknown':
            self.turn = item
        elif self.turn == item:
            raise NotYourTurn("It's not your turn!")
        self.board[index] = item
        self.turn = item
        self.filled_cells += 1

    def __getitem__(self, index):
        if index not in self.valid_keys:
            raise InvalidKey('Invalid key!')
        return self.board[index]

    def __str__(self):
        line = ['', '', '']
        for i in range(1, 4):
            line[i - 1] = \
                "{} | {} | {} | {} |\n".format(str(i),
                                               self.board['A' + str(i)],
                                               self.board['B' + str(i)],
                                               self.board['C' + str(i)])
        dashes = '  -------------\n'
        return "\n{d}{}{d}{}{d}{}{d}    A   B   C  \n".format(*line[::-1],
                                                              d=dashes)

    def game_status(self):
        if self.wins('X'):
            return 'X wins!'
        elif self.wins('O'):
            return 'O wins!'
        elif self.filled_cells == 9:
            return 'Draw!'
        else:
            return 'Game in progress.'

    def wins(self, gamer):
        winning_triples = (('A1', 'A2', 'A3'), ('B1', 'B2', 'B3'),
                           ('C1', 'C2', 'C3'), ('A1', 'B1', 'C1'),
                           ('A2', 'B2', 'C2'), ('A3', 'B3', 'C3'),
                           ('A1', 'B2', 'C3'), ('A3', 'B2', 'C1'))
        for triple in iter(winning_triples):
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
