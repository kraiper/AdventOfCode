def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += str(ele)

        # return string
    return str1


def read_lines(file_name):
    file = open(file_name)
    file_content = file.readlines()
    i = 0
    while i < len(file_content):
        file_content[i] = file_content[i].rstrip("\n")
        i += 1
    return file_content


class GameBoard:

    def __init__(self, lines, size=1):
        self.sorted_list = []
        self.board = [None] * (len(lines))
        self.visited = [None] * (len(lines) * size)
        i = 0
        while i < len(lines):
            l_list = list(lines[i])
            self.board[i] = []
            for value in l_list:
                self.board[i].append(int(value))
            i += 1
        i = 0

        while i < len(lines) * size:
            self.visited[i] = [False] * (len(self.board[0]) * size)
            i += 1

    def extend(self):
        size = 5
        # original = [None] * (len(self.board) * 5)
        size_x = len(self.board)
        size_y = len(self.board[0])
        offset = 1

        while offset < size:
            x = 0
            while x < size_x:
                y = (offset - 1) * size_y
                while y < size_y * offset:
                    add_num = self.board[x][y] + 1
                    if add_num > 9:
                        add_num = 1
                    self.board[x].append(add_num)
                    y += 1
                x += 1
            offset += 1

        offset = 1

        x = 0
        while x < size_x * (size - 1):
            y = (offset - 1) * size_y
            self.board.append([])
            while y < len(self.board[0]):
                add_num = self.board[x][y] + 1
                if add_num > 9:
                    add_num = 1
                self.board[x + size_x].append(add_num)
                y += 1
            x += 1

    def print(self):
        for row in self.board:
            print(row)

    def add_risk_pos(self, risk, x, y):
        i = 0
        if len(self.sorted_list) > 0:
            while i < len(self.sorted_list):
                if self.sorted_list[i]["risk"] >= risk:
                    self.sorted_list.insert(i, {"risk": risk, "x": x, "y": y})
                    return
                i += 1
        self.sorted_list.append({"risk": risk, "x": x, "y": y})

    def traverse_board(self):

        self.sorted_list.append({"risk": 0, "x": 0, "y": 0})
        endx = len(self.board) - 1
        endy = len(self.board[0]) - 1
        self.visited[0][0] = True

        i = 0
        while i < 10:
            position = self.sorted_list.pop(0)
            risk = position["risk"]
            x = position["x"]
            y = position["y"]
            self.visited[x][y] = True
            # print(position)
            # print(risk, x, y)
            if x == endx and y == endy:
                return risk
            if x != 0 and not self.visited[x - 1][y]:
                self.add_risk_pos(risk + self.board[x - 1][y], x - 1, y)
                self.visited[x - 1][y] = True
            if y != 0 and not self.visited[x][y - 1]:
                self.add_risk_pos(risk + self.board[x][y - 1], x, y - 1)
                self.visited[x][y - 1] = True
            if x != len(self.board) - 1 and not self.visited[x + 1][y]:
                self.add_risk_pos(risk + self.board[x + 1][y], x + 1, y)
                self.visited[x + 1][y] = True
            if y != len(self.board[0]) - 1 and not self.visited[x][y + 1]:
                self.add_risk_pos(risk + self.board[x][y + 1], x, y + 1)
                self.visited[x][y + 1] = True

            # i += 1
            # print(self.sorted_list)


def p1():
    lines = read_lines("day15/input.txt")
    board = GameBoard(lines)
    # board.print()
    result = board.traverse_board()
    print(result)


def p2():
    lines = read_lines("day15/input.txt")
    board = GameBoard(lines, 5)
    board.extend()
    # board.print()
    result = board.traverse_board()
    print(result)


# p1()
p2()
