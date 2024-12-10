from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    disk_list = []
    index = 0
    for line in data.splitlines():
        file = True
        for val in line:
            if file:
                for _ in range(int(val)):
                    disk_list.append(str(index))
                index += 1
                file = False
            else:
                for _ in range(int(val)):
                    disk_list.append(".")
                file = True

    start_index = 0
    end_index = len(disk_list) - 1
    result_list = disk_list.copy()

    while start_index < end_index:
        if disk_list[start_index] != ".":
            start_index += 1
        elif disk_list[end_index] == ".":
            end_index -= 1
        else:
            result_list[start_index] = result_list[end_index]
            result_list[end_index] = "."
            start_index += 1
            end_index -= 1

    result = 0
    index = 0
    for val in result_list:
        if val != ".":
            result += int(val) * index
        index += 1
    return result

def create_scan(result_list):
    scan_files = []
    scan_empty = []
    start_index = 0
    current_index = 0
    length = 0
    current_val = result_list[0]
    for val in result_list:
        if val != current_val:
            if current_val != ".":
                scan_files.append([start_index, length])
                start_index = current_index
                length = 0
            else:
                scan_empty.append([start_index, length])
                start_index = current_index
                length = 0
            current_val = val
        length += 1
        current_index += 1
    if current_val != ".":
        scan_files.append([start_index, length])
    else:
        scan_empty.append([start_index, length])
    return scan_files, scan_empty

def solution_b(data: str):
    disk_list = []
    index = 0
    for line in data.splitlines():
        file = True
        for val in line:
            if file:
                for _ in range(int(val)):
                    disk_list.append(str(index))
                index += 1
                file = False
            else:
                for _ in range(int(val)):
                    disk_list.append(".")
                file = True

    result_list = disk_list.copy()
    scan_files, scan_empty = create_scan(result_list)
    scan_files.reverse()
    for move_pair in scan_files:
        move_index, move_length = move_pair
        for pair in scan_empty:
            empty_index, empty_length = pair
            if empty_index < move_index and empty_length >= move_length:
                for offset in range(move_length):
                    result_list[empty_index + offset] = result_list[move_index + offset]
                    result_list[move_index + offset] = "."
                break
        _, scan_empty = create_scan(result_list)

    result = 0
    index = 0
    for val in result_list:
        if val != ".":
            result += int(val) * index
        index += 1
    return result

puzzle = Puzzle(year=2024, day=9)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 2858
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")