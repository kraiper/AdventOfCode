from functools import cache
from aocd.models import Puzzle
from aocd.examples import Example

def split_str(data):
    return str(int(data[0:int(len(data)/2)])), str(int(data[int(len(data)/2):]))

@cache
def calculate_itteration(node_tuple, max_depth):
    value, depth = node_tuple
    if depth == max_depth:
        return 1
    if value == "0":
        return calculate_itteration(("1", depth + 1), max_depth)
    elif len(value) % 2 == 0:
        first, second = split_str(value)
        return calculate_itteration((first, depth + 1), max_depth) + calculate_itteration((second, depth + 1), max_depth)
    else:
        return calculate_itteration((str(int(value) * 2024), depth + 1), max_depth)

def solution_a(data: str):
    full_list = [(val, 0) for val in data.splitlines()[0].split(" ")]
    result = 0
    max_depth = 25
    while len(full_list) != 0:
        current = full_list.pop()
        result += calculate_itteration(current, max_depth)
    return result

def solution_b(data: str):
    full_list = [(val, 0) for val in data.splitlines()[0].split(" ")]
    result = 0
    max_depth = 75
    while len(full_list) != 0:
        current = full_list.pop()
        result += calculate_itteration(current, max_depth)
    return result


puzzle = Puzzle(year=2024, day=11)
example: Example = puzzle.examples[0]
input_data = """125 17"""
assert str(solution_a(input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

print(f"Solution_b: {solution_b(puzzle.input_data)}")