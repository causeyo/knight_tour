from random import choice
import sys
sys.setrecursionlimit(100)


class Chessboard:

    def __init__(self, size=8):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]

    def show_board(self):
        print("\nACTUAL CHESSBOARD:")
        for row in self.board:
            print(row)

    def move(self, x, y, step_no):
        self.board[x][y] = step_no

    def check_move(self, x, y):
        return (0 <= x < self.size) and \
               (0 <= y < self.size) and \
            self.board[x][y] == 0

    def tour_recursion(self, pos_x, pos_y, moves, step_no):
            if step_no > self.size**2:
                return True
            for n in moves:
                new_x = pos_x + n[1]
                new_y = pos_y + n[0]
                if self.check_move(new_x, new_y):
                    self.move(new_x, new_y, step_no)
                    if self.tour_recursion(new_x, new_y, moves, step_no+1):
                        return True
                    self.board[new_x][new_y] = 0
            return False

    def tour(self):
        # moves = [ (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        self.board[0][0] = 1
        step_no = 2

        if not self.tour_recursion(0, 0, moves, step_no):
            print("FAIL")
        else:
            print("SUCCESS")
            self.show_board()



chessboard = Chessboard(8)
chessboard.tour()


# knight = Knight()
# # for m in knight.MOVES:
# #     print(m, knight.check_move(chessboard, m))
# # knight.move(chessboard, (2,1), 1)
# # chessboard.show_board()
# #
# chessboard.chessboard[0][0] = 1
# if not knight.tour(chessboard, step_no=2):
#     print("FAIL")
# else:
#     print("SUCCESS")
