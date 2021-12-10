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

    def set_board(self, board_str: [str]):
        self.board = [None] * len(board_str)
        i = 0
        while i < len(board_str):
            self.board[i] = []
            i += 1
        i = 0
        while i < len(board_str):
            row: list = list(board_str[i].rstrip(" \n "))
            print(row)
            y = 0
            while y < len(row):
                self.board[i].append(int(row[y]))
                y += 1
            i += 1

    def find_low_points(self):
        result = 0
        i = 0
        while i < len(self.board):
            y = 0
            while y < len(self.board[i]):
                if i == 0 and y == 0:
                    if self.board[i][y] < self.board[i+1][y] and self.board[i][y] < self.board[i][y+1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == 0 and y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i+1][y] and self.board[i][y] < self.board[i][y-1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == len(self.board) - 1 and y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i-1][y] and self.board[i][y] < self.board[i][y-1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == len(self.board) - 1 and y == 0:
                    if self.board[i][y] < self.board[i-1][y] and self.board[i][y] < self.board[i][y+1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == 0:
                    if self.board[i][y] < self.board[i+1][y] and self.board[i][y] < self.board[i][y+1] and self.board[i][y] < self.board[i][y-1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == len(self.board) - 1:
                    if self.board[i][y] < self.board[i-1][y] and self.board[i][y] < self.board[i][y+1] and self.board[i][y] < self.board[i][y-1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if y == 0:
                    if self.board[i][y] < self.board[i][y+1] and self.board[i][y] < self.board[i+1][y] and self.board[i][y] < self.board[i-1][y]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i][y-1] and self.board[i][y] < self.board[i+1][y] and self.board[i][y] < self.board[i-1][y]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if self.board[i][y] < self.board[i][y-1] and self.board[i][y] < self.board[i+1][y] and self.board[i][y] < self.board[i-1][y] and self.board[i][y] < self.board[i][y+1]:
                    result += 1 + self.board[i][y]
                y += 1
            i += 1
        print(result)

    def print_board(self):
        for a in self.board:
            print(a)

def p1():
    file = open("day9/input.txt")
    file_content = file.readlines()

    board = GameBoard()
    board.set_board(file_content)
    board.find_low_points()


p1()



