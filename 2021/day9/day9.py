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
        self.visited = []

    def set_board(self, board_str: [str]):
        self.board = [None] * len(board_str)
        i = 0
        while i < len(board_str):
            self.board[i] = []
            i += 1
        i = 0
        while i < len(board_str):
            row: list = list(board_str[i].rstrip(" \n "))
            y = 0
            while y < len(row):
                self.board[i].append(int(row[y]))
                y += 1
            i += 1

        self.visited = [None] * len(self.board)
        i = 0
        while i < len(self.board):
            self.visited[i] = [-1] * len(self.board[i])
            i += 1

    def find_low_points(self):
        result = 0
        i = 0
        while i < len(self.board):
            y = 0
            while y < len(self.board[i]):
                if i == 0 and y == 0:
                    if self.board[i][y] < self.board[i + 1][y] and self.board[i][y] < self.board[i][y + 1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == 0 and y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i + 1][y] and self.board[i][y] < self.board[i][y - 1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == len(self.board) - 1 and y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y - 1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == len(self.board) - 1 and y == 0:
                    if self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y + 1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == 0:
                    if self.board[i][y] < self.board[i + 1][y] and self.board[i][y] < self.board[i][y + 1] and \
                            self.board[i][y] < self.board[i][y - 1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if i == len(self.board) - 1:
                    if self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y + 1] and \
                            self.board[i][y] < self.board[i][y - 1]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if y == 0:
                    if self.board[i][y] < self.board[i][y + 1] and self.board[i][y] < self.board[i + 1][y] and \
                            self.board[i][y] < self.board[i - 1][y]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i][y - 1] and self.board[i][y] < self.board[i + 1][y] and \
                            self.board[i][y] < self.board[i - 1][y]:
                        result += 1 + self.board[i][y]
                    y += 1
                    continue
                if self.board[i][y] < self.board[i][y - 1] and self.board[i][y] < self.board[i + 1][y] and \
                        self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y + 1]:
                    result += 1 + self.board[i][y]
                y += 1
            i += 1
        print(result)

    def find_basins(self):
        next_move = []
        basin = 0

        i = 0
        while i < len(self.board):
            y = 0
            while y < len(self.board[i]):
                if i == 0 and y == 0:
                    if self.board[i][y] < self.board[i + 1][y] and self.board[i][y] < self.board[i][y + 1]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if i == 0 and y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i + 1][y] and self.board[i][y] < self.board[i][y - 1]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if i == len(self.board) - 1 and y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y - 1]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if i == len(self.board) - 1 and y == 0:
                    if self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y + 1]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if i == 0:
                    if self.board[i][y] < self.board[i + 1][y] and self.board[i][y] < self.board[i][y + 1] and \
                            self.board[i][y] < self.board[i][y - 1]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if i == len(self.board) - 1:
                    if self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y + 1] and \
                            self.board[i][y] < self.board[i][y - 1]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if y == 0:
                    if self.board[i][y] < self.board[i][y + 1] and self.board[i][y] < self.board[i + 1][y] and \
                            self.board[i][y] < self.board[i - 1][y]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if y == len(self.board[i]) - 1:
                    if self.board[i][y] < self.board[i][y - 1] and self.board[i][y] < self.board[i + 1][y] and \
                            self.board[i][y] < self.board[i - 1][y]:
                        next_move.append({"x": i, "y": y, "basin": basin})
                        basin += 1
                    y += 1
                    continue
                if self.board[i][y] < self.board[i][y - 1] and self.board[i][y] < self.board[i + 1][y] and \
                        self.board[i][y] < self.board[i - 1][y] and self.board[i][y] < self.board[i][y + 1]:
                    next_move.append({"x": i, "y": y, "basin": basin})
                    basin += 1
                y += 1
            i += 1

        max_x = len(self.board)
        max_y = len(self.board[0])
        while len(next_move) > 0:
            move = next_move.pop()
            if move["x"] < 0 or move["x"] == max_x:
                continue
            if move["y"] < 0 or move["y"] == max_y:
                continue
            if self.board[move["x"]][move["y"]] == 9:
                continue

            if self.visited[move["x"]][move["y"]] == -1:
                self.visited[move["x"]][move["y"]] = move["basin"]
                next_move.append({"x": move["x"] - 1, "y": move["y"], "basin": move["basin"]})
                next_move.append({"x": move["x"] + 1, "y": move["y"], "basin": move["basin"]})
                next_move.append({"x": move["x"], "y": move["y"] - 1, "basin": move["basin"]})
                next_move.append({"x": move["x"], "y": move["y"] + 1, "basin": move["basin"]})

    def count_basin_size(self):
        size_dict = {}
        i = 0
        while i < 10000:
            size_dict[i] = 0
            i += 1

        i = 0
        while i < len(self.visited):
            y = 0
            while y < len(self.visited[i]):
                if self.visited[i][y] != -1:
                    size_dict[self.visited[i][y]] += 1
                y += 1
            i += 1

        return size_dict

    def print_board(self):
        for a in self.board:
            print(a)

    def print_visited(self):
        for a in self.visited:
            print(a)


def p1():
    file = open("day9/input.txt")
    file_content = file.readlines()

    board = GameBoard()
    board.set_board(file_content)
    board.find_low_points()


def p2():
    file = open("day9/input.txt")
    file_content = file.readlines()

    point_list = []

    board = GameBoard()
    board.set_board(file_content)
    board.find_basins()
    # board.print_visited()
    points = board.count_basin_size()
    smalest = 0
    for key in points:
        if points[key] > 0:
            point_list.append(points[key])

    while len(point_list) > 3:
        i = 1
        smalest_index = 0
        while i < len(point_list):
            if point_list[i] < point_list[smalest_index]:
                smalest_index = i
            i += 1
        point_list.pop(smalest_index)

    print(point_list[0] * point_list[1] * point_list[2])

# p1()
p2()
