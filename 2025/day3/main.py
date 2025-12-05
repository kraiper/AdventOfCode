from aocd.models import Puzzle
from aocd.examples import Example
import time

def number_search(line: str, highest: int, num_index_1: int, num_index_2: int):
    current_number = int(line[num_index_1] + line[num_index_2])
    if highest < current_number:
        highest = current_number
    if num_index_2 < len(line) - 1:
        return number_search(line, highest, num_index_1, num_index_2 + 1)
    else:
        return highest

def solution_a(data: str):
    lines = data.split("\n")
    res = 0
    for line in lines:
        line_max = 0
        for start_index in range(len(line) - 1):
            index_max = number_search(line, 0, start_index, start_index+1)
            if line_max < index_max:
                line_max = index_max
        res += line_max
    return res



def find_highest(line, start, end):
    highest = 0
    highest_index = 0
    for index in range(start, end):
        value = int(line[index])
        if value > highest:
            highest = value
            highest_index = index

    return highest, highest_index
    


def solution_b(data: str):
    lines = data.split("\n")
    res = 0
    for line in lines:
        line_res = ""
        next_start = 0
        for index in range(12):
            highest, highest_index = find_highest(line, next_start, len(line) - 11 + index)
            line_res += str(highest)
            next_start = highest_index + 1
        res += int(line_res)
    return res

puzzle = Puzzle(year=2025, day=3)
example: Example = puzzle.examples[0]


assert str(solution_a(example.input_data)) == example.answer_a
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = 3121910778619
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"{answer_b}, {sol_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")