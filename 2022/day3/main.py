from operator import index
from unittest import result
from aocd.models import Puzzle
from aocd.examples import Example

PRIORITY = {chr(i + 97): i + 1 for i in range(26)}
PRIORITY.update({chr(i + 65): i + 27 for i in range(26)})


def solution_a(data: str):
    shared = []
    for line in data.splitlines():
        middle = len(line) // 2
        r1, r2 = line[:middle], line[middle:]
        for item in r1:
            if item in r2:
                shared.append(item)
                break
    return sum(PRIORITY[item] for item in shared)

def solution_b(data: str):
    index = 0
    lines = data.splitlines()
    badges = []
    while index < len(lines):
        for item in lines[index]:
            if item in lines[index + 1] and item in lines[index + 2]:
                badges.append(item)
                break
        index += 3
    return sum(PRIORITY[item] for item in badges)

puzzle = Puzzle(year=2022, day=3)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 70
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")