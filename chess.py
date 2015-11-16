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
        self.is_first_move = True

    def convert_to_coordinates(self, coordinate):
        return int(coordinate[1]) - 1, self.letter_lookup[coordinate[0]]

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

    def __init__(self, color):
        self.color = color
        self.abc = 'a b c d e f g h'.split()
        self.letter_lookup = dict(zip(self.abc, range(8)))
        self.is_first_move = True

    def convert_to_coordinates(self, coordinate):
        print('coordinate: {}'.format(coordinate))
        return int(coordinate[1]) - 1, self.letter_lookup[coordinate[0]]

    def get_moves(self, old, board):
        moves = []
        if self.color == 'lower':
            tmp = (old[0] + 1, old[1])
            try:

                if board[old[0] + 1][old[1]] == '_':
                    moves.append(tmp)

            except IndexError:
                pass

            try:

                if self.is_first_move:
                    tmp = (old[0] + 2, old[1])
                    if board[old[0] + 2][old[1]] == '_':
                        moves.append(tmp)

            except IndexError:
                pass

            try:

                if board[old[0] + 1][old[1] + 1] is not '_':
                    moves.append((old[0] + 1, old[1] + 1))

            except IndexError:
                pass

            try:

                if board[old[0] + 1][old[1] - 1] is not '_':
                    moves.append((old[0] + 1, old[1] - 1))

            except IndexError:
                pass
        print('moves: {}'.format(moves))
        return moves

    def move(self, old, new, board):
        old = self.convert_to_coordinates(old)
        new = self.convert_to_coordinates(new)
        moves = self.get_moves(old, board)
        print('new: {}'.format(new))
        if new in moves:
            print('true')
            board[new[0]][new[1]] = 'p' if self.color == 'lower' else 'P'
            board[old[0]][old[1]] = '_'
            self.is_first_move = False
        else:
            print('false')
        return board


if __name__ == '__main__':
    board = Board()
    board.initialize_board()
    board.print_board()
    while True:
        old = input('select piece: ')
        new = input('select new position: ')
        old_coords = board.convert_to_coordinates(old)
        new_coords = board.convert_to_coordinates(new)
        print(old_coords)
        name = board.board[old_coords[0]][old_coords[1]]
        if name == 'p':

            p = Pawn('lower')
            board.board = p.move(old, new, board.board)
            board.print_board()
        else:
            print(name)
