class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = [['O' for _ in range(j)] for _ in range(i)]

    def play(self, column, color):
        if color not in ['R', 'J']:
            raise ValueError("Invalid color")
        if not (0 <= column < self.j):
            raise ValueError("Invalid column")

        for i in range(self.i - 1, -1, -1):
            if self.board[i][column] == 'O':
                self.board[i][column] = color
                break
        else:
            raise ValueError("Column is full")

    def print_board(self):
        return "\n".join([" ".join(row) for row in self.board])


board = Board(5, 9)
board.play(1, "R")
board.play(2, "J")
board.play(1, "R")
board.play(2, "J")
board.play(1, "R")
board.play(2, "J")
board.play(1, "R")

print(board.print_board())
