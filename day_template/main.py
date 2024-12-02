from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    pass

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2024, day=)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = None
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")