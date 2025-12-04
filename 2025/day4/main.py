from aocd.models import Puzzle
from aocd.examples import Example
import time

directions = [[-1, 0], [-1, -1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, 1]]

def create_board(data: str):
    board = [[] for _ in range(len(data.splitlines()))]
    i = 0

    for line in data.splitlines():
        for value in line:
            board[i].append(value)
        i += 1

    return board


def solution_a(data: str):
    board = create_board(data)
    res = 0
    row = 0
    while row < len(board):
        col = 0
        while col < len(board[0]):
            neighbours = 0
            if board[row][col] == "@":
                for dir in directions:
                    row_check = row + dir[0]
                    col_check = col + dir[1]
                    if (
                        not row_check < 0 and
                        not col_check < 0 and 
                        not row_check > len(board) - 1 and
                        not col_check > len(board[0]) - 1 and
                        board[row_check][col_check] == "@"
                    ):
                        neighbours += 1
                if neighbours < 4:
                    res += 1
            col += 1
        row += 1
    return res

def solution_b(data: str):
    board = create_board(data)

    res = 0
    updated = 1
    while updated > 0:
        row = 0
        updated = 0
        clean = []
        while row < len(board):
            col = 0
            while col < len(board[0]):
                neighbours = 0
                if board[row][col] == "@":
                    for dir in directions:
                        row_check = row + dir[0]
                        col_check = col + dir[1]
                        if (
                            not row_check < 0 and
                            not col_check < 0 and 
                            not row_check > len(board) - 1 and
                            not col_check > len(board[0]) - 1 and
                            board[row_check][col_check] == "@"
                        ):
                            neighbours += 1

                    if neighbours < 4:
                        res += 1
                        updated += 1
                        clean.append((row, col))

                col += 1
            row += 1
        for r, c in clean:
            board[r][c] = "x"
        clean.clear()
    return res

puzzle = Puzzle(year=2025, day=4)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data))
assert sol_a == "13", f"Got {sol_a} wanted {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = "43"
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b} wanted {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")