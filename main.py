from random import choice


class Chessboard:
    def __init__(self, x=8, y=8):
        self.x = x
        self.y = y
        self.chessboard = self.create_board()

    def create_board(self):
        return [[0 for _ in range(self.x)] for _ in range(self.y)]

    def show_board(self):
        print("\nACTUAL CHESSBOARD:")
        for row in self.chessboard:
            print(row)


class Knight:
    MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def __init__(self, pos_x=0, pos_y=0):
        self.pos_x = 0
        self.pos_y = 0
        self.step_no = 1

    def move(self, board, step):
        print(f"step {step}")
        if self.check_move(board, step):
            print("MOVE BITCH")
            board.chessboard[self.pos_x + step[0]][self.pos_y + step[1]] = self.step_no
        else:
            print("NO MOVE!!!")

    def check_move(self, board, step):
        return (0 <= self.pos_x + step[0] <= board.x - 1) and \
               (0 <= self.pos_y + step[1] <= board.y - 1) and \
            board.chessboard[self.pos_x + step[0]][self.pos_y + step[1]] == 0


chessboard = Chessboard()
knight = Knight()
knight.move(chessboard, choice(Knight.MOVES))
chessboard.show_board()
