from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    safe = 0
    for line in data.splitlines():
        int_list = list(map(int,line.split(" ")))
        i = 0
        up = int_list[i] < int_list[i+1]
        add = True
        while i < len(int_list) -1:
            i += 1
            if abs(int_list[i-1] - int_list[i]) in [1, 2 , 3]:
                if up:
                    if int_list[i-1] >= int_list[i]:
                        add = False
                        continue
                elif not up:
                    if int_list[i-1] <= int_list[i]:
                        add = False
                        continue
            else:
                add = False
        if add:
            safe += 1
    return safe

def solution_b(data: str):
    def check_line(l):
        i = 0
        add = True
        up = l[i] < l[i+1]
        while i < len(l) -1:
            i += 1
            if abs(l[i-1] - l[i]) in [1, 2 , 3]:
                if up:
                    if l[i-1] >= l[i]:
                        add = False
                        continue
                elif not up:
                    if l[i-1] <= l[i]:
                        add = False
                        continue
            else:
                add = False
        return add

    def pop(l: list):
        i = 0
        up = l[i] < l[i+1]
        while i < len(l) -1:
            i += 1
            if abs(l[i-1] - l[i]) in [1, 2 , 3]:
                if up:
                    if l[i-1] >= l[i]:
                        del l[i-1]
                        return
                elif not up:
                    if l[i-1] <= l[i]:
                        del l[i]
                        return
            else:
                del l[i-1]
                return

    safe = 0
    for line in data.splitlines():
        int_list = list(map(int,line.split(" ")))
        if check_line(int_list):
            safe += 1
        else:
            s1 = len(int_list)
            pop(int_list)
            s2 = len(int_list)
            assert s1 != s2
            if check_line(int_list):
                safe += 1
    return safe

puzzle = Puzzle(year=2024, day=2)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 4
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")