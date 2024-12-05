from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    rules = []
    lines = []
    for line in data.splitlines():
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            lines.append(line.split(","))

    correct_line = []
    for line in lines:
        correct = True
        for rule in rules:
            start, end = rule
            try:
                if int(line.index(start)) > int(line.index(end)):
                    correct = False
            except Exception:
                continue
            if not correct:
                break
        if correct:
            correct_line.append(line)

    result = 0
    for line in correct_line:
        result += int(line[int(len(line)/2)])
    return result

def solution_b(data: str):
    def sort_pages(line: list, rules: list):
        correct = False
        while not correct:
            correct = True
            for rule in rules:
                start, end = rule
                try:
                    if int(line.index(start)) > int(line.index(end)):
                        left = int(line.index(start))
                        right = int(line.index(end))
                        line[left] = end
                        line[right] = start
                        correct = False
                except Exception:
                    continue


    rules = []
    lines = []
    for line in data.splitlines():
        if "|" in line:
            rules.append(line.split("|"))
        elif "," in line:
            lines.append(line.split(","))

    incorrect_line = []
    for line in lines:
        correct = True
        for rule in rules:
            start, end = rule
            try:
                if int(line.index(start)) > int(line.index(end)):
                    correct = False
            except Exception:
                continue
            if not correct:
                break
        if not correct:
            incorrect_line.append(line)

    for line in incorrect_line:
        sort_pages(line, rules)

    result = 0
    for line in incorrect_line:
        result += int(line[int(len(line)/2)])
    return result

puzzle = Puzzle(year=2024, day=5)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 123
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")