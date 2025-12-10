from copy import copy
from pathlib import Path
import time
import numpy
from functools import cache

answer_a = "7"
answer_b = None


def read_file(file_str: str):
    data_lines: list[str] = []
    with open(file_str, "r") as f:
        data_lines = f.readlines()

    return data_lines


@cache
def find_combination(light_str, button_array_str, wanted_str, depth):
    res = 999999999999
    if depth < 10:

        light_list = [int(x) for x in light_str.split(",")]
        button_array = []

        for button_list_str in button_array_str.split("|"):
            button_array.append([int(x) for x in button_list_str.split(",")])

        wanted = [int(x) for x in wanted_str.split(",")]

        for button in button_array:
            new_light_line = numpy.multiply(light_list, button)
            if (wanted == new_light_line).all():
                return depth + 1

            start_str = ""
            for x in new_light_line:
                start_str += str(x) + ","
            start_str = start_str[:-1]

            v = find_combination(start_str, button_array_str, wanted_str, depth + 1)
            
            if v < res:
                res = v

    return res


def solution_a(file_str: str):
    data_lines = read_file(file_str)
    res = 0
    for index, line in enumerate(data_lines):
        print(f"Loop {index} of {len(data_lines)}")
        line_data = line.strip().split(" ")
        wanted = [1 if x == "#" else -1 for x in list(line_data.pop(0)[1:-1])]
        jolt_scheme = list(line_data.pop(-1)[1:-1].split(","))
        button_list = []
        for l in line_data:
            button_array = [1 for _ in range(len(wanted))]
            for x in l[1:-1].split(","):
                button_array[int(x)] = -1
            button_str = ""
            for x in button_array:
                button_str += str(x) + ","
            button_str = button_str[:-1]
            button_list.append(button_str)

        start_str = ""
        for _ in range(len(wanted)):
            start_str += "-1,"
        start_str = start_str[:-1]

        button_str = ""
        for b in button_list:
            button_str += b + "|"
        button_str = button_str[:-1]

        wanted_str = ""
        for v in wanted:
            wanted_str += str(v) + ","
        wanted_str = wanted_str[:-1]

        res += find_combination(start_str, button_str, wanted_str, 0)

    return res


def solution_b(file_str: str):
    data_lines = read_file(file_str)




example_file = Path(__file__).parent / "example.txt"
data_file = Path(__file__).parent / "data.txt"

assert answer_a is not None
sol_a = str(solution_a(example_file))
assert sol_a == answer_a, f"Got {sol_a}, expected {answer_a}"
start = time.time()
sol_answer_a = str(solution_a(data_file))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")


assert answer_b is not None
sol_b = str(solution_b(example_file))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(data_file))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")