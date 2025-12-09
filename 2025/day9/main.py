from pathlib import Path
import time
from itertools import combinations


answer_a = "50"
answer_b = "24"

def read_file(file_str: str):
    data_lines: list[str] = []
    with open(file_str, "r") as f:
        data_lines = f.readlines()

    return data_lines


def solution_a(file_str: str):
    data_lines = read_file(file_str)
    red_squares = []
    for line in data_lines:
        x, y = line.strip().split(",")
        red_squares.append((int(x), int(y)))

    largest = 0

    for combo in combinations(red_squares, 2):
        x1, y1 = combo[0]
        x2, y2 = combo[1]

        width = abs(x1 - x2)
        height = abs(y1 - y2)

        width = width + 1 if x1 != x2 else width
        height = height + 1 if y1 != y2 else height

        size = (width) * (height)

        if width == 0:
            size = height
        elif height == 0:
            size = width

        if size > largest:
            largest = size

    return largest


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