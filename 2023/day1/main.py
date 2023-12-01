from curses.ascii import isdigit
import re
from aocd.models import Puzzle
from aocd.examples import Example

NUMBERS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def solution_a(data: str):
    # find the first and last number in the list
    total_number = 0
    for line in data.splitlines():
        first_number = -1
        last_number = -1
        for value in line:
            if isdigit(value):
                if first_number == -1:
                    first_number = value
                last_number = value
        total_number += int(first_number + last_number)
    return total_number

def solution_b(data: str):
    total_number = 0
    my_result = []
    for line in data.splitlines():
        valid_inputs = []
        valid_mapping = {}
        i = 0
        while i < len(line):
            if isdigit(line[i]):
                valid_inputs.append(i)
                valid_mapping[i] = int(line[i])
            i += 1
        for number in NUMBERS:
            number_index = [m.start() for m in re.finditer(number, line)]
            for ni in number_index:
                valid_inputs.append(ni)
                valid_mapping[ni] = int(NUMBERS[number])
        valid_inputs.sort()
        total_number += int(str(valid_mapping[valid_inputs[0]]) + str(valid_mapping[valid_inputs[-1]]))
        my_result.append(int(str(valid_mapping[valid_inputs[0]]) + str(valid_mapping[valid_inputs[-1]])))

    return total_number


puzzle = Puzzle(year=2023, day=1)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 281
assert answer_b is not None

data_b = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

assert str(solution_b(data_b)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")