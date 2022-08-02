import numpy as np

class Grid():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = np.full((rows, columns), '-')
        i = 0

    def print_grid(self):
        for i in range(0, int(self.grid.size/self.columns)):
            j = 0
            print()
            for j in range(0, int(self.grid.size/self.rows)):
                print(self.grid[i][j], end=' ')
        print()

class Piece():
    def __init__(self, shape, width, height):
        self.shape = shape
        self.width = width
        self.height = height
        if len(shape) < 2:
            shape *=4
        elif len(shape) < 3:
            shape *= 2
        self.actual_state = shape[0]
        board = Grid(height, width)
        board.print_grid()

    def print_state(self):
        board = Grid(self.height, self.width)
        for i in self.actual_state:
            board.grid[int(i/self.width)][int(i%self.width)] = '0'
        board.print_grid()

    def rotate(self):
        for i in range(0, len(self.shape)):
            if self.shape[i] == self.actual_state:
                if i < 3:
                    self.actual_state = self.shape[i + 1]
                elif i == 3:
                    self.actual_state = self.shape[0]
                break


    def move_down(self):
        for i in range(0, len(self.shape)):
            for j in range(0, len(self.shape[i])):
                self.shape[i][j] += 10

    def move_right(self):
        for i in range(0, len(self.shape)):
            for j in range(0, len(self.shape[i])):
                self.shape[i][j] += 1

    def move_left(self):
        for i in range(0, len(self.shape)):
            for j in range(0, len(self.shape[i])):
                self.shape[i][j] -= 1

def main():
    user_piece = input()
    user_grid_w, user_grid_h = input().split(' ')

    if user_piece == 'O':
        cord = [[4, 14, 15, 5],[4, 14, 15, 5],[4, 14, 15, 5],[4, 14, 15, 5]]
    elif user_piece == 'I':
        cord = [[4, 14, 24, 34], [3, 4, 5, 6], [4, 14, 24, 34], [3, 4, 5, 6]]
    elif user_piece == 'S':
        cord = [[5, 4, 14, 13], [4, 14, 15, 25], [5, 4, 14, 13], [4, 14, 15, 25]]
    elif user_piece == 'Z':
        cord = [[4, 5, 15, 16], [5, 15, 14, 24], [4, 5, 15, 16], [5, 15, 14, 24]]
    elif user_piece == 'L':
        cord = [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]]
    elif user_piece == 'J':
        cord = [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]]
    elif user_piece == 'T':
        cord = [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]

    piece = Piece(cord, int(user_grid_w), int(user_grid_h))
    piece.print_state()

    while True:
        user_move = input()
        if user_move == 'down':
            piece.move_down()
            piece.print_state()
        elif user_move == 'right':
            piece.move_down()
            piece.move_right()
            piece.print_state()
        elif user_move == 'left':
            piece.move_down()
            piece.move_left()
            piece.print_state()
        elif user_move == 'rotate':
            piece.move_down()
            piece.rotate()
            piece.print_state()
        elif user_move == 'exit':
            break


if __name__ == '__main__':
    main()
