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

    def __setitem__(self, index, item):
        if index not in self.valid_keys:
            raise InvalidKey("Invalid key!")
        if item not in self.valid_values:
            raise InvalidValue("Invalid value!")
        if self.board[index] != ' ':
            raise InvalidMove("Invalid move!")
        self.board[index] = item
        self.filled_cells += 1

    def __getitem__(self, index):
        if index not in self.valid_keys:
            raise InvalidKey("Invalid key!")
        return self.board[index]

    def __str__(self):
        line = ['', '', '', '']
        for i in range(1, 4):
            line[i] = str(i) + ' | ' + self.board['A' + str(i)] +\
                ' | ' + self.board['B' + str(i)] +\
                ' | ' + self.board['C' + str(i)] + ' |\n'
        return '\n -------------\n' +\
               line[3] +\
               ' -------------\n' +\
               line[2] +\
               ' -------------\n' +\
               line[1] +\
               ' -------------\n' +\
               ' A B C \n'

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
        if self.board['A1'] == self.board['A2'] == self.board['A3'] == gamer:
            return True
        elif self.board['B1'] == self.board['B2'] == self.board['B3'] == gamer:
            return True
        elif self.board['C1'] == self.board['C2'] == self.board['C3'] == gamer:
            return True
        elif self.board['A1'] == self.board['B1'] == self.board['C1'] == gamer:
            return True
        elif self.board['A2'] == self.board['B2'] == self.board['C2'] == gamer:
            return True
        elif self.board['A3'] == self.board['B3'] == self.board['C3'] == gamer:
            return True
        elif self.board['A1'] == self.board['B2'] == self.board['C3'] == gamer:
            return True
        elif self.board['A3'] == self.board['B2'] == self.board['C1'] == gamer:
            return True
        else:
            return False


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
