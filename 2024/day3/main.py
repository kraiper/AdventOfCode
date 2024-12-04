from aocd.models import Puzzle
from aocd.examples import Example
import re

def solution_a(data: str):
    result = 0
    for line in data.splitlines():
        search = re.finditer("mul\((\d+),(\d+)\)", line)
        for hit in search:
            result += int(hit.group(1))*int(hit.group(2))
    return result

def solution_b(data: str):
    result = 0
    do = True

    for line in data.splitlines():
        search1 = re.finditer("mul\((\d+),(\d+)\)", line)
        search2 = re.finditer("(don?'?t?\(\))", line)
        spans = []
        span_start = 0
        for hit in search2:
            if do:
                if hit.group(0) == "don't()":
                    spans.append((span_start, hit.span()[0]))
                    do = False
            else:
                if hit.group(0) == "do()":
                    span_start = hit.span()[0]
                    do = True
        if do:
            spans.append((span_start, len(line)))

        for hit in search1:
            for s in spans:
                start, end = s
                if (
                    int(hit.span()[0]) >= start and
                    int(hit.span()[0]) <= end
                ):
                    result += int(hit.group(1))*int(hit.group(2))

    return result

puzzle = Puzzle(year=2024, day=3)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == "161"
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 48
assert answer_b is not None
assert str(solution_b("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")