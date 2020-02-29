import random


class Board:
    def __init__(self, rows, cols):
        """Initialize the board and does operations in it"""
        self.rows = rows
        self.columns = cols
        self.bombs = 0
        self.bombs_array = []
        self.board = []
        self.build()

    def build(self):
        """Build the board as an array"""
        if (self.rows * self.columns) <= 10 or (self.rows * self.columns) > 480:
            print("The number is not valid, Enter one of the valid sets: 8 x 10 | 14 x 18 | 20 x 24")
            self.build()

        for i in range(self.rows):
            self.board.append([])
            for j in range(self.columns):
                self.board[i].append(int(0))

    def show_board(self):
        """Prints the board in a good layout"""
        # print the header row
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("  n  ||", end="")
        for c in range(self.columns):
            if len(str(c+1)) ==1:
                print("  {}  |".format(c + 1), end="")
            else:
                print("  {} |".format(c + 1), end="")

        print("\n=====++", end="")
        for c in range(self.columns):
            print("=====+", end="")
        print("")

        # print the rest of the rows
        for r in range(self.rows):
            if len(str(r+1)) ==1:
                print("  {}  ||".format(r+1), end="")
            else:
                print("  {} ||".format(r+1), end="")

            for c in range(self.columns):
                print("  {}  |".format(self.board[r][c]), end="")
            print("\n-----++", end="")
            for c in range(self.columns):
                print("-----+", end="")
            print()

    def generate_bombs(self):
        """generates the number of bombs in the grid and put them in random places"""
        # generate the bombs
        if (self.rows * self.columns) == 80:
            self.bombs = 10
        elif (self.rows * self.columns) == 252:
            self.bombs = 40
        elif (self.rows * self.columns) == 480:
            self.bombs = 99

        for b in range(self.bombs):
            r = random.randint(0, self.rows-1)
            c = random.randint(0, self.columns-1)

            if [r, c] not in self.bombs_array:
                self.bombs_array.append([r, c])
        print(self.bombs_array)

        # place the bombs
        for b in self.bombs_array:
            self.board[b[0]][b[1]] = "*"
        self.insert_numbers()

    def insert_numbers(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.board[r][c] == "*":
                    inc = [-1, 0, 1]
                    for i in inc:
                        for j in inc:
                            row_index = r + i
                            col_index = c + j
                            if (row_index < 0) or (row_index >= self.rows) \
                                    or (col_index < 0) or (col_index >= self.columns) or (i == 0 and j == 0):
                                continue
                            if self.board[row_index][col_index] == "*":
                                continue
                            self.board[row_index][col_index] += 1


class Player:
    def __init__(self, name):
        self.name = name
        size = self.start_game()
        self.hid_board = Board(size[0], size[1])
        self.hid_board.generate_bombs()
        self.hid_board.show_board()
        self.board = Board(size[0], size[1])

    def start_game(self):
        print("What difficulty do you prefer? <Easy: 8 x 10> <Medium: 14 x 18> <Hard: 20 x 24>")
        r=0
        c=0
        i = int(input("Enter 1 for Easy, 2 for Medium, 3 for Hard\n"))
        if i not in [1, 2, 3]:
            print("Not valid, try again")
            self.start_game()
        if i == 1:
            r, c = 8, 10
        elif i == 2:
            r, c = 14, 18
        elif i == 3:
            r, c = 20, 24
        return [r, c]


kees = Player("kees")

# hid_board = Board(r, c)
# board = Board(r, c)
# board.show_board()
# board.generate_bombs()
# board.show_board()
