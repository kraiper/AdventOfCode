from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    list1 = []
    list2 = []
    for line in data.splitlines():
        left, right = line.split("   ")
        list1.append(int(left))
        list2.append(int(right))

    list1.sort()
    list2.sort()

    i = 0
    result = 0
    while i < len(list1):
        result += abs(list1[i] - list2[i])
        i+=1


    return result

def solution_b(data: str):
    list1 = []
    list2 = []
    for line in data.splitlines():
        left, right = line.split("   ")
        list1.append(int(left))
        list2.append(int(right))

    i = 0
    result = 0
    while i < len(list1):
        result += list1[i] * list2.count(list1[i])
        i+=1

    return result

puzzle = Puzzle(year=2024, day=1)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 31
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")