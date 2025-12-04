from aocd.models import Puzzle
from aocd.examples import Example
import time

def solution_a(data: str):
    pass

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2025, day=3)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data))
assert sol_a == example.answer_a, f"Got {sol_a}, expected {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = None
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {example.answer_a}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")