def read_bingo_numbers(bingo_numbers_str):
    bingo_numbers_int = []
    for number in bingo_numbers_str:
        bingo_numbers_int.append(int(number))
    return bingo_numbers_int


def create_game_boards(file_con):
    game_boards = []

    while True:
        try:
            file_con.pop(0)
        except Exception:
            break
        board = [file_con.pop(0), file_con.pop(0), file_con.pop(0), file_con.pop(0), file_con.pop(0)]
        game_board = GameBoard()
        game_board.set_board(board)

        game_boards.append(game_board)

    return game_boards


class GameBoard:
    """
    [
        [
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        ],
        [
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        ]
    ]
    """

    def __init__(self):
        self.board = []

    def set_board(self, board_str):
        self.board.clear()
        i = 0
        while i < 5:
            row: list = board_str[i].split(" ")
            try:
                while True:
                    row.remove("")
            except Exception:
                pass

            self.board.append([{int(row[0]): 0},
                               {int(row[1]): 0},
                               {int(row[2]): 0},
                               {int(row[3]): 0},
                               {int(row[4]): 0}]
                              )
            i += 1

    def add_number(self, number):
        i = 0
        while i < 5:
            y = 0
            while y < 5:
                if number in self.board[i][y].keys():
                    self.board[i][y][number] = 1
                y += 1
            i += 1

    def check_bingo(self):
        i = 0
        while i < 5:
            y = 0
            in_row = 0
            in_column = 0
            while y < 5:
                if 1 in self.board[i][y].values():
                    in_row += 1
                if 1 in self.board[y][i].values():
                    in_column += 1
                y += 1
            if in_row == 5:
                return True
            elif in_column == 5:
                return True
            i += 1
        return False

    def print_board(self):
        print(self.board[0][0], self.board[0][1], self.board[0][2], self.board[0][3], self.board[0][4])
        print(self.board[1][0], self.board[1][1], self.board[1][2], self.board[1][3], self.board[1][4])
        print(self.board[2][0], self.board[2][1], self.board[2][2], self.board[2][3], self.board[2][4])
        print(self.board[3][0], self.board[3][1], self.board[3][2], self.board[3][3], self.board[3][4])
        print(self.board[4][0], self.board[4][1], self.board[4][2], self.board[4][3], self.board[4][4])

    def calculate_score(self):
        i = 0
        score = 0
        while i < 5:
            y = 0
            while y < 5:
                if 0 in self.board[i][y].values():
                    for key in self.board[i][y].keys():
                        score += key
                y += 1
            i += 1
        return score


def run_game_1():
    file = open("day4/input.txt")
    file_content = file.readlines()
    bingo_numbers_str = file_content.pop(0).split(",")

    bingo_numbers = read_bingo_numbers(bingo_numbers_str)
    game_boards = create_game_boards(file_content)

    while True:
        number = bingo_numbers.pop(0)
        for board in game_boards:
            board.add_number(number)

        for board in game_boards:
            if board.check_bingo():
                return board.calculate_score() * number


def run_game_2():
    file = open("day4/input.txt")
    file_content = file.readlines()
    bingo_numbers_str = file_content.pop(0).split(",")

    bingo_numbers = read_bingo_numbers(bingo_numbers_str)
    game_boards = create_game_boards(file_content)

    while True:
        number = bingo_numbers.pop(0)
        for board in game_boards:
            board.add_number(number)

        i = 0
        while i < len(game_boards):
            if game_boards[i].check_bingo():
                if len(game_boards) == 1:
                    return game_boards[i].calculate_score() * number
                else:
                    game_boards.pop(i)
            else:
                i += 1

result1 = run_game_1()

result2 = run_game_2()

print(result1)

print(result2)
