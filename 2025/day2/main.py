from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    data = data.replace("\n", "")
    id_pair = data.split(",")

    res = 0

    for pair in id_pair:
        start_id, end_id = pair.split("-")
        working_number = int(start_id)
        while working_number <= int(end_id):
            split_pos = int(len(str(working_number)) / 2)
            left, right = str(working_number)[:split_pos], str(working_number)[split_pos:]
            if left == right:
                res += working_number
            working_number += 1

    return res

def solution_b(data: str):
    data = data.replace("\n", "")
    id_pair = data.split(",")

    res = 0

    for pair in id_pair:
        start_id, end_id = pair.split("-")
        working_number = int(start_id)
        while working_number <= int(end_id):
            working_len = len(str(working_number))
            dividers = [x + 1 for x in range(1, int(working_len)) if not working_len % (x + 1)]

            for div in dividers:
                step = int(working_len / div)
                splits = [str(working_number)[x * step: (x + 1) * step] for x in range(div)]
                if len(set(splits)) <= 1:
                    res += working_number
                    break
            working_number += 1
    return res

puzzle = Puzzle(year=2025, day=2)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a, f"Looking for: {example.answer_a}"
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 4174379265
assert answer_b is not None
calculated_answer = str(solution_b(example.input_data))
assert calculated_answer == str(answer_b), f"Looking for: {answer_b} but got {calculated_answer}"
print(f"Solution_b: {solution_b(puzzle.input_data)}")