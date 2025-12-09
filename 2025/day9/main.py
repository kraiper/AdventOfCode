from aocd.models import Puzzle
from aocd.examples import Example
import time
from itertools import combinations

def solution_a(data: str):
    red_squares = []
    with open("2025/day9/data.txt", "r") as f:
        for line in f.readlines():
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

    print(largest)
    return largest


def solution_b(data: str):
    pass

puzzle = Puzzle(year=2025, day=9)
example: Example = puzzle.examples[0]


sol_a = str(solution_a(example.input_data))
assert sol_a == "50", f"Got {sol_a}, expected 50"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
assert int(sol_answer_a) > 4748985168
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

# answer_b = None
# assert answer_b is not None
# sol_b = str(solution_b(example.input_data))
# assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
# start = time.time()
# sol_answer_b = str(solution_b(puzzle.input_data))
# end = time.time()
# print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")