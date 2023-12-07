from operator import le
from aocd.models import Puzzle
from aocd.examples import Example
import re



def _read_data(data: str, seeds, transform):
    lines = data.splitlines()
    depth = 0
    line_index = 0
    seeds.extend(re.findall(r"(\d+)", lines[line_index]))
    line_index += 3

    while depth < 7:
        while line_index < len(lines) and lines[line_index] != "":
            destination, source, r = lines[line_index].split(" ")
            _list = [int(source), int(destination), int(r)]
            transform[depth].append(_list)
            line_index += 1
        line_index += 2
        depth += 1

def solution_a(data: str):
    seeds = []
    transform = [[] for _ in range(7)]
    _read_data(data, seeds, transform)
    location = []
    for seed in seeds:
        depth = 0
        current = int(seed)
        while depth < 7:
            for target in transform[depth]:
                if current in range(target[0], target[0] + target[2]):
                    current = target[1] + (current - target[0])
                    break
            depth += 1
        location.append(current)
    return min(location)

def solution_b(data: str):
    seeds = []
    transform = [[] for _ in range(7)]
    _read_data(data, seeds, transform)
    location = []

    full_seed_list = []
    seed_index = 0
    while seed_index < len(seeds):
        full_seed_list.extend(range(int(seeds[seed_index]), int(seeds[seed_index]) + int(seeds[seed_index + 1])))
        seed_index += 2
    for seed in full_seed_list:
        depth = 0
        current = int(seed)
        while depth < 7:
            for target in transform[depth]:
                if current in range(target[0], target[0] + target[2]):
                    current = target[1] + (current - target[0])
                    break
            depth += 1
        location.append(current)
    print(location)
    print(len(location))
    print( min(location))
    return min(location)

puzzle = Puzzle(year=2023, day=5)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 46
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
# print(f"Solution_b: {solution_b(puzzle.input_data)}")