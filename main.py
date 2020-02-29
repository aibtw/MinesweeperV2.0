class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.columns = cols
        self.board = []
        self.build()

    def build(self):
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.columns):
                self.board[i].append(0)

    def show_board(self):
        # print(self.board)
        print("  n  ||", end="")
        for c in range(self.columns):
            print("  {}  |".format(c + 1), end="")
        print("\n=====++", end="")
        for c in range(self.columns):
            print("=====+", end="")
        print("")



class Player:
    def __init__(self,):
        pass


board = Board(2,6)
board.show_board()