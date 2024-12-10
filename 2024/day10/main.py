from aocd.models import Puzzle
from aocd.examples import Example

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def create_board(data: str):
    board = [[] for _ in range(len(data.splitlines()))]
    start = []
    i = 0
    for line in data.splitlines():
        for value in line:
            if value == "0":
                start.append((i,len(board[i])))
            board[i].append(int(value))
        i += 1
    return board, start

def resolve_start(board, start):
    max_rows = len(board)
    max_columns = len(board[0])
    nine_pos = []
    while len(start) > 0:
        row, column = start.pop()
        current_value = board[row][column]
        if current_value == 9:
            nine_pos.append((row, column))
        for dir in directions:
            next_row = row + dir[0]
            next_column = column + dir[1]
            if (
                next_row >= 0 and next_row < max_rows and
                next_column >= 0 and next_column < max_columns
            ):
                next_value = board[next_row][next_column]
                if next_value == current_value + 1:
                    start.append([next_row, next_column])

    return len(list(set(nine_pos)))

def resolve_start_no_trim(board, start):
    max_rows = len(board)
    max_columns = len(board[0])
    nine_pos = []
    while len(start) > 0:
        row, column = start.pop()
        current_value = board[row][column]
        if current_value == 9:
            nine_pos.append((row, column))
        for dir in directions:
            next_row = row + dir[0]
            next_column = column + dir[1]
            if (
                next_row >= 0 and next_row < max_rows and
                next_column >= 0 and next_column < max_columns
            ):
                next_value = board[next_row][next_column]
                if next_value == current_value + 1:
                    start.append([next_row, next_column])

    return len(nine_pos)

def solution_a(data: str):
    board, start = create_board(data)
    result = 0
    for pos in start:
        result += resolve_start(board, [pos])

    return result

def solution_b(data: str):
    board, start = create_board(data)
    result = 0
    for pos in start:
        result += resolve_start_no_trim(board, [pos])

    return result

puzzle = Puzzle(year=2024, day=10)
example: Example = puzzle.examples[0]


input_test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


assert str(solution_a(input_test)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 81
assert answer_b is not None
assert str(solution_b(input_test)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")