import copy
from aocd.models import Puzzle
from aocd.examples import Example
import time
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def create_board(data: str):
    board = [[] for _ in range(len(data.splitlines()))]
    start = []
    i = 0
    for line in data.splitlines():
        for value in line:
            if value == "^":
                start.append(i)
                start.append(len(board[i]))
            board[i].append(value)
        i += 1
    return board, start


def traverse_board(board: list, start: list):
    dir = 0
    current_pos = start
    traversed = [[current_pos[0], current_pos[1]]]

    while True:

        next_0 = current_pos[0] + directions[dir][0]
        next_1 = current_pos[1] + directions[dir][1]

        if next_0 < 0 or next_1 < 0 or next_0 > len(board[0]) - 1 or next_1 > len(board) - 1:
            break

        if board[next_0][next_1] != "#":
            current_pos[0] = next_0
            current_pos[1] = next_1
            traversed.append([next_0, next_1])
        else:
            dir += 1
            if dir > len(directions) - 1:
                dir = 0

    return traversed


def calculate_result(traversed: list):
    for v in traversed:
        return len([t for t in (set(tuple(i) for i in traversed))])


def traverse_board_complex(board: list, start: list):
    dir = 0
    current_pos = start.copy()
    traversed = [[current_pos[0], current_pos[1]]]
    moves = 0

    while moves < 10000:
        next_0 = current_pos[0] + directions[dir][0]
        next_1 = current_pos[1] + directions[dir][1]

        if next_0 < 0 or next_1 < 0 or next_0 > len(board[0]) - 1 or next_1 > len(board) - 1:
            break

        if board[next_0][next_1] != "#":
            current_pos[0] = next_0
            current_pos[1] = next_1
            traversed.append([next_0, next_1])
        else:
            dir += 1
            if dir > len(directions) - 1:
                dir = 0
        moves += 1
    if moves < 10000:
        return 0
    return 1



def solution_a(data: str):
    board, start = create_board(data)
    traveled = traverse_board(board, start)
    result = calculate_result(traveled)
    return result

def solution_b(data: str):
    board, start = create_board(data)
    result = 0
    traversed_points_from_one = traverse_board(board, start.copy())
    traversed_points_from_one = [t for t in (set(tuple(i) for i in traversed_points_from_one))]
    boards = 0
    total_boards = len(traversed_points_from_one)
    for point in traversed_points_from_one:
        boards += 1
        print(f"Board {boards} of roughly {total_boards}")

        temp_board = copy.deepcopy(board)
        temp_board[point[0]][point[1]] = "#"
        result += traverse_board_complex(temp_board, start.copy())

    return result

puzzle = Puzzle(year=2024, day=6)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 6
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
tic = time.perf_counter()
print(f"Solution_b: {solution_b(puzzle.input_data)}")
toc = time.perf_counter()
print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
