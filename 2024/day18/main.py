from aocd.models import Puzzle
from aocd.examples import Example

def create_board(data, width, height, num):
    board = [["." for _ in range(width)] for _ in range(height)]

    visited = [None] * height

    for i in range(height):
        visited[i] = [False] * width

    i = 0
    y,x = 0, 0
    for row in data.splitlines():
        if i == num:
            break
        y,x = row.split(",")
        board[int(x)][int(y)] = "#"
        visited[int(x)][int(y)] = True
        i += 1
    return board, visited, x, y

def add_pos(sorted_list, weight, row, column, visited):
    i = 0
    visited[row][column] = True
    if len(sorted_list) > 0:
        while i < len(sorted_list):
            if sorted_list[i]["weight"] >= weight:
                sorted_list.insert(i, {"weight": weight, "row": row, "column": column})
                return
            i += 1
    sorted_list.append({"weight": weight, "row": row, "column": column})

def traverse(board, start, end, visited):
    sorted_list = [{"weight": 0, "row": 0, "column": 0}]
    visited[0][0] = True

    i = 0
    while i < 30:
        if len(sorted_list) == 0:
            return 0
        position = sorted_list.pop(0)
        weight = position["weight"]
        row = position["row"]
        column = position["column"]
        visited[row][column] = True

        if row == end[0] and column == end[1]:
            return weight

        if row != 0 and not visited[row - 1][column]:
            add_pos(sorted_list, weight + 1, row - 1, column, visited)
        if column != 0 and not visited[row][column - 1]:
            add_pos(sorted_list, weight + 1, row, column - 1, visited)
        if row != len(board) - 1 and not visited[row + 1][column]:
            add_pos(sorted_list, weight + 1, row + 1, column, visited)
        if column != len(board[0]) - 1 and not visited[row][column + 1]:
            add_pos(sorted_list, weight + 1, row, column + 1, visited)

        # i += 1
        # print(i)
        # print(self.sorted_list)



def solution_a(data: str, wh = 71, simulate_num = 1024):
    board, visited, x, y = create_board(data, wh, wh, simulate_num)
    start = [0, 0]
    end = [wh-1, wh-1]

    result = traverse(board, start, end, visited)

    return result

def solution_b(data: str, wh = 71, simulate_num = 1024):
    offset = 0
    x, y = 0, 0
    while True:
        board, visited, x, y = create_board(data, wh, wh, simulate_num + offset)
        start = [0, 0]
        end = [wh-1, wh-1]

        result = traverse(board, start, end, visited)
        if result == 0:
            break
        offset += 1

    result = f"{y},{x}"
    return result

puzzle = Puzzle(year=2024, day=18)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data, 7, 12)) == "22"
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = "6,1"
assert answer_b is not None
assert str(solution_b(example.input_data, 7, 12)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")