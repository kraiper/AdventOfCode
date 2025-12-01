import operator
from aocd.models import Puzzle
from aocd.examples import Example


def solution_a(data: str):
    data_list = data.split("\n")
    pos = 50
    res = 0

    for line in data_list:
        dir = operator
        if line[0] == "L":
            dir = operator.sub
            num = int(line.split("L")[1])
        elif line[0] == "R":
            dir = operator.add
            num = int(line.split("R")[1])
        i = 0
        while num != 0 and i < 10:
            pos = dir(pos, num)
            if pos < 0:
                num = abs(pos) - 1
                pos = 99
            elif pos > 99:
                num = pos - 100
                pos = 0
            else:
                num = 0
            i+=1
        if i > 9:
            break
        if pos == 0:
            res += 1
    return res





def solution_b(data: str):
    pass

puzzle = Puzzle(year=2025, day=1)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = None
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")