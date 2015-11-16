class Board:

    positions = {
        'r': [(0, 0), (0, 7)],
        'p': [(1, i) for i in range(8)],
        'n': [(0, 1), (0, 6)],
        'b': [(0, 2), (0, 5)],
        'k': [(0, 4)],
        'q': [(0, 3)],
        'R': [(7, 0), (7, 7)],
        'P': [(6, i) for i in range(8)],
        'N': [(7, 1), (7, 6)],
        'B': [(7, 2), (7, 5)],
        'K': [(7, 4)],
        'Q': [(7, 3)]
    }

    def __init__(self):
        self.abc = 'a b c d e f g h'.split()
        self.board = [['_' for i in range(8)] for num in range(8)]
        self.letter_lookup = dict(zip(self.abc, range(8)))

    def set_position(self, coordinates, piece):
        r, c = coordinates
        self.board[r][c] = piece

    @property
    def get_positions(self):
        return self.board

    def initialize_board(self):
        for name, coordList in self.positions.items():
            for coord in coordList:
                self.set_position(coord, name)

    def print_board(self):

        row_format = str('|'.join(["{%s:^5}" % str(i) for i in range(8)]))
        letter_line_format = str(''.join(["{%s:^6}" % str(i) for i in range(8)]))
        letters = '      ' + letter_line_format.format(*self.abc)
        horizontal_line = '      ' + '------' * 7 + '-----'
        print(horizontal_line)
        for n, row in enumerate(self.get_positions, 1):
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


if __name__ == '__main__':
    board = Board()
    # print(board.board)
    print(board.letter_lookup)
    board.initialize_board()
    # print(board.board)
    board.print_board()
