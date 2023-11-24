import heapq
from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    max_value = 0
    current_value = 0
    for value in data.splitlines():
        if value:
            current_value += int(value)
            if current_value > max_value:
                max_value = current_value
        else:
            current_value = 0
    return max_value

def solution_b(data: str):
    max_values = [0]
    current_value = 0
    for value in data.splitlines():
        if value:
            current_value += int(value)
            max_values[-1] = current_value
        else:
            max_values.append(0)
            current_value = 0
    highest_values = heapq.nlargest(3, max_values)
    return sum(highest_values)

puzzle = Puzzle(year=2022, day=1)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = "45000"
assert str(solution_b(example.input_data)) == answer_b
print(f"Solution_b: {solution_b(puzzle.input_data)}")