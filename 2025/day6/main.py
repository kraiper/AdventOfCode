import re
from aocd.models import Puzzle
from aocd.examples import Example
import time

def solution_a(data: str):
    data_list = []
    res = 0
    for line in data.splitlines():
        data_list.append([val for val in line.split(" ") if val])
    math_list = data_list.pop(-1)
    for index, operator in enumerate(math_list):
        calc_str = ""
        for v in data_list:
            calc_str += v[index] + operator
        calc_str = calc_str[:-1]
        res += eval(calc_str) 
    return res


def solution_b(data: str):
    data_list = data.splitlines()
    res = 0
    
    math_list = [val for val in data_list.pop(-1)]
    math_list = [m for m in math_list if m != " "]
    
    for line in data_list:
        line_list = list(line)
        line_list.reverse()

    index = 0
    new_lines = []
    while index < len(data_list[0]):
        number_str = ""
        for line in data_list:
            number_str += line[index]
        new_lines.append(number_str.strip(" "))
        index += 1

    calcs = []
    t_line = []
    while new_lines:
        val = new_lines.pop(0)
        if val != "":
            t_line.append(val)
        else:
            calcs.append(t_line.copy())
            t_line.clear()
    calcs.append(t_line.copy())
    
    for index, operator in enumerate(math_list):
        calc_str = ""
        for v in calcs[index]:
            calc_str += v + operator
        res += eval(calc_str[:-1])
    return res


puzzle = Puzzle(year=2025, day=6)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data))
assert sol_a == example.answer_a, f"Got {sol_a}, expected {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = 3263827
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {example.answer_a}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
assert int(sol_answer_b) > 8440565836606
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")