import random


class Board:
    def __init__(self, rows, cols):
        """Initialize the board and does operations in it"""
        self.rows = rows
        self.columns = cols
        self.bombs = 0
        self.bombs_array = []
        self.shown_board = []
        self.hid_board = []
        self.build()

    def build(self):
        """Build the board as an array"""
        for i in range(self.rows):
            self.shown_board.append([])
            self.hid_board.append([])
            for j in range(self.columns):
                self.hid_board[i].append(int(0))
                self.shown_board[i].append("-")

    def show_board(self, board):
        """Prints the board in a good layout"""
        # print the header row
        # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
                print("  {}  |".format(board[r][c]), end="")
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
        # print(self.bombs_array)

        # place the bombs
        for b in self.bombs_array:
            self.hid_board[b[0]][b[1]] = "*"
        self.insert_numbers()

    def insert_numbers(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.hid_board[r][c] == "*":
                    inc = [-1, 0, 1]
                    for i in inc:
                        for j in inc:
                            row_index = r + i
                            col_index = c + j
                            if (row_index < 0) or (row_index >= self.rows) \
                                    or (col_index < 0) or (col_index >= self.columns) or (i == 0 and j == 0):
                                continue
                            if self.hid_board[row_index][col_index] == "*":
                                continue
                            self.hid_board[row_index][col_index] += 1

    def check_win(self):
        for r in self.rows:
            for c in self.columns:
                if self.shown_board[r][c] == self.hid_board[r][c]:
                    continue
                else:
                    if self.hid_board[r][c] == "*":
                        continue
                    else:
                        return False
        return True


class Player:
    def __init__(self, name):
        self.name = name
        size = self.start_game()
        self.boards = Board(size[0], size[1])
        self.boards.generate_bombs()
        self.boards.show_board(self.boards.shown_board)
        self.choice()

    def start_game(self):
        print("What difficulty do you prefer? <Easy: 8 x 10> <Medium: 14 x 18> <Hard: 20 x 24>")
        r = 0
        c = 0
        i = int(input("Enter 1 for Easy, 2 for Medium, 3 for Hard\n"))
        if i not in [1, 2, 3]:
            print("Not valid, try again")
            self.__init__(self.name)
        if i == 1:
            r, c = 8, 10
        elif i == 2:
            r, c = 14, 18
        elif i == 3:
            r, c = 20, 24
        return [r, c]

    def make_move(self):
        r = int(input("Make a move: \nEnter the row number\n"))
        if r-1 not in range(self.boards.rows):
            if r == 0:
                exit()
            else:
                print("Not valid, try again")
                self.make_move()
        c = int(input("Enter the column number \n"))
        if c-1 not in range(self.boards.columns):
            if c == 0:
                exit()
            print("Not valid, try again")
            self.make_move()

        self.boards.shown_board[r-1][c-1] = self.boards.hid_board[r-1][c-1]
        self.boards.show_board(self.boards.shown_board)

        if self.boards.shown_board[r-1][c-1] == "*":
            print(" ----- You Lose -----")
            exit()
        if self.boards.check_win == True:
            print(" ----- You win ------ ")
            exit()

        self.choice()

    def choice(self):
        ch = input("Enter f to put flag or m to make move\n").lower()
        if ch == "m":
            self.make_move()
        elif ch == "f":
            self.put_flag()
        else:
            print("not valid, try again")
            self.choice()

    def put_flag(self):
        r = int(input("Put a flag: \nEnter the row number\n"))
        if r-1 not in range(self.boards.rows):
            if r == 0:
                exit()
            else:
                print("Not valid, try again")
                self.put_flag()
        c = int(input("Enter the column number \n"))
        if c-1 not in range(self.boards.columns):
            if c == 0:
                exit()
            print("Not valid, try again")
            self.put_flag()

        self.boards.shown_board[r-1][c-1] = "F"
        self.boards.show_board(self.boards.shown_board)
        if self.boards.check_win == True:
            print(" ----- You win ------ ")
            exit()
        self.choice()


kees = Player("kees")
