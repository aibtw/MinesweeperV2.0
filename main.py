class Board:
    def __init__(self, rows, cols):
        """Initialize the board and does operations in it"""
        self.rows = rows
        self.columns = cols
        self.board = []
        self.build()

    def build(self):
        """Build the board as an array"""
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.columns):
                self.board[i].append(0)

    def show_board(self):
        """Prints the board in a good layout"""
        # print the header row
        print("  n  ||", end="")
        for c in range(self.columns):
            print("  {}  |".format(c + 1), end="")
        print("\n=====++", end="")
        for c in range(self.columns):
            print("=====+", end="")
        print("")

        # print the rest of the rows
        for r in range(self.rows):
            print("  {}  ||".format(r+1), end="")
            for c in range(self.columns):
                print("  {}  |".format(self.board[r][c]), end="")
            print("\n-----++", end="")
            for c in range(self.columns):
                print("-----+", end="")
            print()


class Player:
    def __init__(self,):
        pass


board = Board(6,6)
board.show_board()
