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
        # print('coordinate: {}'.format(coordinate))
        return int(coordinate[1]) - 1, self.letter_lookup[coordinate[0]]

    def get_moves(self, old, board):
        moves = []
        if self.color == 'lower':
            tmp = (old[0] + 1, old[1])

            try:
                # allow pawn to move forward one space if empty
                if board[old[0] + 1][old[1]] == '_':
                    moves.append(tmp)
            except IndexError:
                pass

            try:
                # allow pawn to move forward 2 spaces on its first move
                if self.is_first_move:
                    tmp = (old[0] + 2, old[1])
                    if board[old[0] + 2][old[1]] == '_':
                        moves.append(tmp)
            except IndexError:
                pass

            try:
                # allow pawn to capture diagonally if target is
                # occupied by opponent piece
                target = board[old[0] + 1][old[1] + 1]
                if target.isalpha() and not target.islower():
                    moves.append((old[0] + 1, old[1] + 1))
            except IndexError:
                pass

            try:
                # allow pawn to capture diagonally if target is
                # occupied by opponent piece
                target = board[old[0] + 1][old[1] - 1]
                if target.isalpha() and not target.islower():
                    moves.append((old[0] + 1, old[1] - 1))
            except IndexError:
                pass

        if self.color == 'UPPER':
            tmp = (old[0] - 1, old[1])

            try:
                # allow pawn to move forward one space if empty
                if board[old[0] - 1][old[1]] == '_':
                    moves.append(tmp)
            except IndexError:
                pass

            try:
                # allow pawn to move forward 2 spaces on its first move
                if self.is_first_move:
                    tmp = (old[0] - 2, old[1])
                    if board[old[0] - 2][old[1]] == '_':
                        moves.append(tmp)
            except IndexError:
                pass

            try:
                # allow pawn to capture diagonally if target is
                # occupied by opponent piece
                target = board[old[0] - 1][old[1] + 1]
                if target.isalpha() and not target.islower():
                    moves.append((old[0] - 1, old[1] + 1))
            except IndexError:
                pass

            try:
                # allow pawn to capture diagonally if target is
                # occupied by opponent piece
                target = board[old[0] - 1][old[1] - 1]
                if target.isalpha() and not target.islower():
                    moves.append((old[0] - 1, old[1] - 1))
            except IndexError:
                pass
        # print('moves: {}'.format(moves))
        return moves

    def move(self, old, new, board):
        old = self.convert_to_coordinates(old)
        new = self.convert_to_coordinates(new)
        moves = self.get_moves(old, board)
        # print('new: {}'.format(new))
        if new in moves:
            # print('true')
            board[new[0]][new[1]] = 'p' if self.color == 'lower' else 'P'
            board[old[0]][old[1]] = '_'
            self.is_first_move = False
        else:
            raise MoveError('Invalid Move')
        return board


class Knight:

    def __init__(self, color):
        self.color = color
        self.abc = 'a b c d e f g h'.split()
        self.letter_lookup = dict(zip(self.abc, range(8)))
        self.is_first_move = True

    def convert_to_coordinates(self, coordinate):
        # print('coordinate: {}'.format(coordinate))
        return int(coordinate[1]) - 1, self.letter_lookup[coordinate[0]]

    def get_moves(self, old, board):
        moves = []

        for n in [-1, 1]:
            for num in [-2, 2]:
                # print n, num
                # print num, n

                tmp = (old[0] + n, old[1] + num)
                try:
                    target = board[old[0] + n][old[1] + num]
                    if target == '_' or (target.isupper() is not self.color.isupper()):
                        moves.append(tmp)
                except IndexError:
                    pass

                tmp = (old[0] + num, old[1] + n)
                try:
                    target = board[old[0] + num][old[1] + n]
                    if target == '_' or (target.isupper() is not self.color.isupper()):
                        moves.append(tmp)
                except IndexError:
                    pass

        return moves

    def move(self, old, new, board):
        old = self.convert_to_coordinates(old)
        new = self.convert_to_coordinates(new)
        moves = self.get_moves(old, board)
        # print('new: {}'.format(new))
        if new in moves:
            # print('true')
            board[new[0]][new[1]] = 'n' if self.color == 'lower' else 'N'
            board[old[0]][old[1]] = '_'
            self.is_first_move = False
        else:
            raise MoveError('Invalid Move')
        return board


class MoveError(Exception):
    pass


if __name__ == '__main__':
    pieces = {
        'p': Pawn,
        'n': Knight
    }
    board = Board()
    board.initialize_board()
    board.print_board()
    turn = 'UPPER'
    while True:

        if turn == 'UPPER':

            print("--- Upper's turn ---")
            old = input('select piece: ')

            old_coords = board.convert_to_coordinates(old)

            # print(old_coords)
            name = board.board[old_coords[0]][old_coords[1]]
            try:
                assert name.isupper()
            except AssertionError:
                print("Please choose your own piece")
                continue
            new = input('select new position: ')
            new_coords = board.convert_to_coordinates(new)
            current_piece = pieces[name.lower()]('UPPER')
            try:
                board.board = current_piece.move(old, new, board.board)
            except MoveError:
                print("invalid move! Please choose a legal move.")
                continue
            turn = 'lower'
            board.print_board()

        if turn == 'lower':
            print("--- Lower's turn ---")
            old = input('select piece: ')

            old_coords = board.convert_to_coordinates(old)

            # print(old_coords)
            name = board.board[old_coords[0]][old_coords[1]]
            try:
                assert name.islower()
            except AssertionError:
                print("Please choose your own piece")
                continue

            new = input('select new position: ')
            new_coords = board.convert_to_coordinates(new)
            current_piece = pieces[name.lower()]('lower')
            try:
                board.board = current_piece.move(old, new, board.board)
            except MoveError:
                print("invalid move! Please choose a legal move.")
                continue
            turn = 'UPPER'
            board.print_board()

