from functools import cache
import json
from pathlib import Path
import time

answer_a = "5"
answer_b = "2"


def read_file(file_str: str):
    data_lines: list[str] = []
    with open(file_str, "r") as f:
        data_lines = f.readlines()

    return data_lines

def solution_a(file_str: str):
    data_lines = read_file(file_str)
    path_dict = {}
    res = 0
    for line in data_lines:
        key, output = line.strip().split(":")
        if key not in path_dict:
            path_dict[key] = output.strip().split(" ")
        else:
            raise Exception("Duplication")

    next_step = [x for x in path_dict["you"]]
    while next_step:
        val = next_step.pop()
        if val == "out":
            res += 1
        else:
            next_step.extend([x for x in path_dict[val]])

    return res


@cache
def find_paths(val: str, dac: bool, fft: bool, path_json: str) -> int:
    res = 0
    if val == "dac":
        dac = True
    if val == "fft":
        fft = True
    if val == "out":
        if dac and fft:
            return 1
        return 0
    path_dict = json.loads(path_json)
    for v in path_dict[val]:
        res += find_paths(v, dac, fft, path_json)
 
    return res


def solution_b(file_str: str):
    data_lines = read_file(file_str)
    path_dict = {}
    res = 0
    for line in data_lines:
        key, output = line.strip().split(":")
        if key not in path_dict:
            path_dict[key] = output.strip().split(" ")
        else:
            raise Exception("Duplication")

    res = find_paths("svr", False, False, json.dumps(path_dict))

    return res



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
sol_b = str(solution_b(Path(__file__).parent / "example2.txt"))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(data_file))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")