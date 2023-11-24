from operator import add

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


# class GameBoard:
#     def __init__(self):
#         self.board = []
#
#     def set_board(self, board_str: [str]):
#         self.board = [None] * len(board_str)
#         i = 0
#         while i < len(board_str):
#             self.board[i] = []
#             i += 1
#         i = 0
#         while i < len(board_str):
#             row: list = list(board_str[i].rstrip(" \n "))
#             y = 0
#             while y < len(row):
#                 self.board[i].append(int(row[y]))
#                 y += 1
#             i += 1

def print_board(board):
    for a in board:
        print(a)


def p1():
    lines = read_lines("day13/input.txt")

    hx = 0
    hy = 0
    for line in lines:
        if "fold" not in line:
            x, y = line.split(",")
            if hx < int(x):
                hx = int(x)
            if hy < int(y):
                hy = int(y)
    board = [0] * (hy + 1)
    i = 0
    while i < (hy + 1):
        board[i] = [0] * (hx + 1)
        i += 1

    for line in lines:
        if "fold" not in line:
            x, y = line.split(",")
            board[int(y)][int(x)] = 1

    axis = ""
    offset = 0

    for line in lines:
        if "fold" in line:
            s1 = line.split(" ")
            axis, offset = s1[2].split("=")
            offset = int(offset)

            if axis == "x":
                i = 0
                while i < len(board):
                    move_up = offset + 1
                    move_down = offset - 1
                    while move_up < len(board[i]) and move_down > -1:
                        board[i][move_down] += board[i][move_up]
                        move_up += 1
                        move_down -= 1
                    i += 1
                i = 0
                while i < len(board):
                    while offset < len(board[i]):
                        board[i].pop(offset)
                    i += 1

            if axis == "y":
                move_up = offset + 1
                move_down = offset - 1

                while move_up < hy + 1 and move_down > -1:
                    board[move_down] = list(map(add, board[move_down], board[move_up]))
                    move_up += 1
                    move_down -= 1
                while offset < len(board):
                    board.pop(offset)

            # break

    count = 0
    for y in board:
        for x in y:
            if x > 0:
                count += 1
    print(count)
    # print_board(board)


def p2():
    lines = read_lines("day13/input.txt")

    hx = 0
    hy = 0
    for line in lines:
        if "fold" not in line:
            x, y = line.split(",")
            if hx < int(x):
                hx = int(x)
            if hy < int(y):
                hy = int(y)
    board = [0] * (hy + 1)
    i = 0
    while i < (hy + 1):
        board[i] = [0] * (hx + 1)
        i += 1

    for line in lines:
        if "fold" not in line:
            x, y = line.split(",")
            board[int(y)][int(x)] = 1

    axis = ""
    offset = 0

    for line in lines:
        if "fold" in line:
            s1 = line.split(" ")
            axis, offset = s1[2].split("=")
            offset = int(offset)

            if axis == "x":
                i = 0
                while i < len(board):
                    move_up = offset + 1
                    move_down = offset - 1
                    while move_up < len(board[i]) and move_down > -1:
                        board[i][move_down] += board[i][move_up]
                        move_up += 1
                        move_down -= 1
                    i += 1
                i = 0
                while i < len(board):
                    while offset < len(board[i]):
                        board[i].pop(offset)
                    i += 1

            if axis == "y":
                move_up = offset + 1
                move_down = offset - 1

                while move_up < hy + 1 and move_down > -1:
                    board[move_down] = list(map(add, board[move_down], board[move_up]))
                    move_up += 1
                    move_down -= 1
                while offset < len(board):
                    board.pop(offset)

            # break
    # print_board(board)

    i = 0
    while i < len(board):
        y = 0
        while y < len(board[0]):
            if board[i][y] > 0:
                board[i][y] = "#"
            else:
                board[i][y] = " "
            y += 1
        i += 1
    # print_board(board)
    for s in board:
        print(listToString(s))

# p1()
p2()