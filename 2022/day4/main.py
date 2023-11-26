from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    overlaps = 0
    for line in data.splitlines():
        e1, e2 = line.split(",")
        v1, v2 = e1.split("-")
        elf_1_set = set(range(int(v1), int(v2)+1))
        if v1 == v2:
            elf_1_set = set([int(v1)])
        v1, v2 = e2.split("-")
        elf_2_set = set(range(int(v1), int(v2)+1))
        if v1 == v2:
            elf_2_set = set([int(v1)])
        if elf_1_set.issubset(elf_2_set):
            overlaps += 1
        elif elf_2_set.issubset(elf_1_set):
            overlaps += 1
    return overlaps

def solution_b(data: str):
    overlaps = 0
    for line in data.splitlines():
        e1, e2 = line.split(",")
        v1, v2 = e1.split("-")
        elf_1_set = set(range(int(v1), int(v2)+1))
        if v1 == v2:
            elf_1_set = set([int(v1)])
        v1, v2 = e2.split("-")
        elf_2_set = set(range(int(v1), int(v2)+1))
        if v1 == v2:
            elf_2_set = set([int(v1)])
        if len(elf_1_set.intersection(elf_2_set)):
            overlaps += 1
    return overlaps

puzzle = Puzzle(year=2022, day=4)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 4
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")