from aocd.models import Puzzle
from aocd.examples import Example

def result_for_line(line):
    s = line.split(": ")
    answer = int(s[0])
    answer_list = [int(n) for n in s[1].split(" ")]

    result_list = []
    for value in answer_list:
        if not result_list:
            result_list.append(value)
        else:
            temp_list = []
            for working_number in result_list:
                temp_list.append(working_number + value)
                temp_list.append(working_number * value)
            result_list = temp_list

    for value in result_list:
        if answer == value:
            return value
    return 0

def result_for_line_2(line):
    s = line.split(": ")
    answer = int(s[0])
    answer_list = [int(n) for n in s[1].split(" ")]

    result_list = []
    for value in answer_list:
        if not result_list:
            result_list.append(value)
        else:
            temp_list = []
            for working_number in result_list:
                temp_list.append(working_number + value)
                temp_list.append(working_number * value)
                temp_list.append(int(str(working_number) + str(value)))
            result_list = temp_list

    for value in result_list:
        if answer == value:
            return value
    return 0

def solution_a(data: str):
    result = 0
    l = 0
    max = len(data.splitlines())
    for line in data.splitlines():
        l += 1
        print(f"Working on {l} of {max}")
        result += result_for_line(line)
    return result

def solution_b(data: str):
    result = 0
    l = 0
    max = len(data.splitlines())
    for line in data.splitlines():
        l += 1
        print(f"Working on {l} of {max}")
        result += result_for_line_2(line)
    return result

puzzle = Puzzle(year=2024, day=7)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 11387
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")