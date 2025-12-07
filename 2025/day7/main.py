from aocd.models import Puzzle
from aocd.examples import Example
import time

def create_board(data: str):
    board = [[] for _ in range(len(data.splitlines()))]
    i = 0

    for line in data.splitlines():
        for value in line:
            board[i].append(value)
        i += 1

    return board

def solution_a(data: str):
    res = 0
    board = create_board(data)

    for r_index, row in enumerate(board):
        if r_index == 0:
            continue

        for c_index, v in enumerate(row):
            if board[r_index - 1][c_index] == "|" or board[r_index - 1][c_index] == "S":
                if v == "^":
                    res += 1
                    board[r_index][c_index - 1] = "|"
                    board[r_index][c_index + 1] = "|"
                else:
                    board[r_index][c_index] = "|"
    return res


def print_board(board):
    for a in board:
        line = ""
        for v in a:
            line += str(v)
        print(line)


def solution_b(data: str):
    res = 0
    board = create_board(data)
    for index, v in enumerate(board[0]):
        if v == "S":
            board[0][index] = 1

    for r_index, row in enumerate(board):

        for c_index, v in enumerate(row):
            if type(board[r_index - 1][c_index]) == int:
                if v == "^":
                    if type(board[r_index][c_index - 1]) == int:
                        board[r_index][c_index - 1] = board[r_index][c_index - 1] + board[r_index - 1][c_index]
                    else:
                        board[r_index][c_index - 1] = board[r_index - 1][c_index]

                    if type(board[r_index][c_index + 1]) == int:
                        board[r_index][c_index + 1] = board[r_index][c_index + 1] + board[r_index - 1][c_index]
                    else:
                        board[r_index][c_index + 1] = board[r_index - 1][c_index]
                else:
                    if type(board[r_index][c_index]) == int:
                        board[r_index][c_index] = board[r_index - 1][c_index] + board[r_index][c_index]
                    else:
                        board[r_index][c_index] = board[r_index - 1][c_index]

    for v in board[-1]:
        if type(v) == int:
            res += v

    return res


puzzle = Puzzle(year=2025, day=7)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data))
assert sol_a == example.answer_a, f"Got {sol_a}, expected {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = 40
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")