class Board:

    piece_lookup = {
        'r': 'rook'
    }

    positions = {
        'r': ['a1', 'h1'],
        'p': [char + '2' for char in 'a b c d e f g h'.split()],
        'n': ['b1', 'g1'],
        'b': ['c1', 'f1'],
        'k': ['e1'],
        'q': ['d1'],
        'R': ['a8', 'h8'],
        'P': [char + '7' for char in 'a b c d e f g h'.split()],
        'N': ['b8', 'g8'],
        'B': ['c8', 'f8'],
        'K': ['e8'],
        'Q': ['d8']
    }

    def __init__(self):
        self.abc = 'a b c d e f g h'.split()
        self.board = {char + str(num): '_' for char in self.abc
                                           for num in range(1, 9)}

    def initialize_board(self):
        for name, coordList in self.positions.items():
            for coord in coordList:
                self.board[coord] = name

    def print_board(self):
        sorted_keys = [[char + str(i) for char in self.abc] for i in range(1, 9)]
        row_values = [[self.board[k] for k in row] for row in sorted_keys]
        row_format = str('|'.join(["{%s:^5}" % str(i) for i in range(8)]))
        letter_line_format = str(''.join(["{%s:^6}" % str(i) for i in range(8)]))
        letters = '      ' + letter_line_format.format(*self.abc)
        horizontal_line = '      ' + '------' * 7 + '-----'
        print(horizontal_line)
        for n, row in enumerate(row_values, 1):
            print('{}    |'.format(n) + row_format.format(*row) + '|\n' + horizontal_line)
        print('\n' + letters)

class Pawn:

    def __init__(self, old_coordinate, new_coordinate, board):
        self.old_coordinate = old_coordinate
        self.new_coordinate = new_coordinate
        self.board = board

    def get_moves(self):
        moves = []
        # self.old_coordinate

    def move(self):
        valid = []




board = Board()
board.initialize_board()
# print(board.board)
board.print_board()
