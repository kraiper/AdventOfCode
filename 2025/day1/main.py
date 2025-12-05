import math
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
        while num != 0:
            pos = dir(pos, num)
            if pos < 0:
                num = abs(pos) - 1
                pos = 99
            elif pos > 99:
                num = pos - 100
                pos = 0
            else:
                num = 0
        if pos == 0:
            res += 1
    return res


def solution_b(data: str):
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

        res += math.floor(num / 100)
        rest = num % 100

        while rest != 0:
            pos = dir(pos, 1)

            if pos < 0:
                pos = 99
            elif pos > 99:
                pos = 0

            if pos == 0:
                res += 1

            rest -= 1
    return res



puzzle = Puzzle(year=2025, day=1)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 6
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")