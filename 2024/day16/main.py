from copy import deepcopy
from operator import add
from time import sleep
from aocd.models import Puzzle
from aocd.examples import Example

def create_board(data: str):
    board = [[] for _ in range(len(data.splitlines()))]
    visited = [[] for _ in range(len(data.splitlines()))]
    start = []
    end = []
    i = 0
    for line in data.splitlines():
        for value in line:
            if value == "S":
                start.append(i)
                start.append(len(board[i]))
            if value == "E":
                end.append(i)
                end.append(len(board[i]))
            if value == "#":
                visited[i].append(-2000)
            else:
                visited[i].append(False)
            if value == ".":
                board[i].append(" ")
            else:
                board[i].append(value)
        # print(line)
        i += 1
    return board, visited, start, end

def print_board(board, visited, active_row, active_column):
    printed_board = deepcopy(board)

    for row in range(len(printed_board)):
        p_row = ""
        for column in range(len(printed_board[row])):
            if visited[row][column] and printed_board[row][column] != "#":
                if row == active_row and column == active_column:
                    printed_board[row][column] = "X"
                else:
                    printed_board[row][column] = "O"
            p_row += printed_board[row][column]
        print(p_row)

def print_travel(board, travel):
    printed_board = deepcopy(board)

    for value in travel:
        row, column = value
        printed_board[row][column] = "."

    for row in range(len(printed_board)):
        p_row = ""
        for column in range(len(printed_board[row])):
            p_row += printed_board[row][column]
        print(p_row)

def add_pos(sorted_list, weight, row, column, direction, travel, visited):
    i = 0
    if len(sorted_list) > 0:
        while i < len(sorted_list):
            if sorted_list[i]["weight"] >= weight:
                sorted_list.insert(i, {
                    "weight": weight,
                    "row": row,
                    "column": column,
                    "direction": direction,
                    "travel": deepcopy(travel),
                    "visited": (visited)
                    })
                return
            i += 1
    sorted_list.append({"weight": weight, "row": row, "column": column, "direction": direction, "travel": deepcopy(travel), "visited": (visited)})

def traverse_a(board, start, end, visited):
    direction = 4
    visited[start[0]][start[1]] = 0
    sorted_list = [{"weight": 0, "row": start[0], "column": start[1], "direction": direction, "travel": [(start[0], start[1])], "visited": visited}]
    results = []
    i = 0
    while True: # i < 30:
        # print(len(sorted_list))
        if len(sorted_list) == 0:
            break
        position = sorted_list.pop(0)
        weight = position["weight"]
        row = position["row"]
        column = position["column"]
        direction = position["direction"]
        travel = (position["travel"])
        travel.append((row, column))
        visited = position["visited"]

        # print_board(board, visited, row, column)
        # print_travel(board, travel)

        # sleep(1)
        if weight > 102508:
            continue

        # if i > 10000:
        #     # print_board(board, visited, row, column)

        #     print_travel(board, travel)

        #     print(weight)
        #     print(len(sorted_list))
        #     i = 0
        # i += 1


        if row == end[0] and column == end[1]:
            print_travel(board, travel)
            print(weight)
            print(len(travel))
            results.append((weight, deepcopy(travel)))
        else:
            if not visited[row][column] or visited[row][column] >= weight:
                visited[row][column] = weight

            if row != 0 and (not visited[row - 1][column] or visited[row - 1][column] + 1000 >= weight):
                add_weight = 1 if direction == 1 else 1001
                add_pos(sorted_list, weight + add_weight, row - 1, column, 1, travel, visited)

            if column != 0 and (not visited[row][column - 1] or visited[row][column - 1] + 1000 >= weight):
                add_weight = 1 if direction == 2 else 1001
                add_pos(sorted_list, weight + add_weight, row, column - 1, 2, travel, visited)

            if row != len(board) - 1 and (not visited[row + 1][column] or visited[row + 1][column] + 1000 >= weight):
                add_weight = 1 if direction == 3 else 1001
                add_pos(sorted_list, weight + add_weight, row + 1, column, 3, travel, visited)

            if column != len(board[0]) - 1 and (not visited[row][column + 1] or visited[row][column + 1] + 1000 >= weight):
                add_weight = 1 if direction == 4 else 1001
                add_pos(sorted_list, weight + add_weight, row, column + 1, 4, travel, visited)

    return results

def solution_a(data: str):
    board, visited, start, end = create_board(data)
    results = traverse_a(board, start, end, visited)
    result, _ = results[0]
    result_list = []
    for res in results:
        weight, travel = res
        if weight < result:
            result = weight
    for res in results:
        weight, travel = res
        if weight == result:
            result_list.extend(travel)
    print(len(list(dict.fromkeys(result_list))))
    print(result)
    return result

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2024, day=16)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == "7036"
answer_a = solution_a(puzzle.input_data)
print(f"Solution_a: {answer_a}")

# answer_b = None
# assert answer_b is not None
# assert str(solution_b(example.input_data)) == str(answer_b)
# print(f"Solution_b: {solution_b(puzzle.input_data)}")