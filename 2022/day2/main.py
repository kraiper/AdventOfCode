from aocd.models import Puzzle
from aocd.examples import Example

choice_value = {"A": 1, "B": 2, "C": 3,
                "X": 0, "Y": 3, "Z": 6}

def solution_a(data: str):
    result_score = {"A X": 4, "A Y": 8, "A Z": 3,
                "B X": 1, "B Y": 5, "B Z": 9,
                "C X": 7, "C Y": 2, "C Z": 6}
    score = 0
    for value in data.splitlines():
        score += result_score[value]
    return score

def solution_b(data: str):
    score = 0
    for value in data.splitlines():
        shape, result = value.split(" ")
        my_shape = int(int(choice_value[shape]) + (float(choice_value[result])/3-1))
        if my_shape > 3:
            my_shape = 1
        elif my_shape < 1:
            my_shape = 3
        score += choice_value[result] + my_shape
    return score

puzzle = Puzzle(year=2022, day=2)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = "12"
assert answer_b is not None
assert str(solution_b(example.input_data)) == answer_b
print(f"Solution_b: {solution_b(puzzle.input_data)}")