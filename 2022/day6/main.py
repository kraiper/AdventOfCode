from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    offset = 0
    while offset < len(data) - 4:
        if len(set(data[offset:offset+4])) == 4:
            return offset + 4
        offset += 1

def solution_b(data: str):
    offset = 0
    while offset < len(data) - 14:
        if len(set(data[offset:offset+14])) == 14:
            return offset + 14
        offset += 1

puzzle = Puzzle(year=2022, day=6)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 19
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")