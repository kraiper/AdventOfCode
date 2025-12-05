from aocd.models import Puzzle
from aocd.examples import Example
import time

def solution_a(data: str):
    fresh_ranges = []
    res = 0
    for line in data.splitlines():
        if "-" in line:
            start, stop = line.split("-")
            start = int(start)
            stop = int(stop)
            fresh_ranges.append((start, stop))
        elif line != "":
            index = int(line)
            for range in fresh_ranges:
                start, stop = range
                if index >= start and index <= stop:
                    res += 1
                    break
    return res

def find_lowest_index(ranges):
    lowest = -1
    lowest_index = -1
    for index, r in enumerate(ranges):
        start, stop = r
        if index == 0:
            lowest = start
            lowest_index = index
        if lowest > start:
            lowest = start
            lowest_index = index
    return lowest_index

def find_overlaps(ranges, start, stop):
    index = 0
    while index < len(ranges):
        r_start, r_stop = ranges[index]
        if r_start <= stop:
            if r_stop > stop:
                stop = r_stop
            ranges.pop(index)
            index = 0
        else:
            index += 1
    return (start, stop)


def run_loop(ranges):
    handled_intervalls = []
    while ranges:
        lowest_index = find_lowest_index(ranges)
        start, stop = ranges.pop(lowest_index)
        handled_intervalls.append(find_overlaps(ranges, start, stop))

    return handled_intervalls

def solution_b(data: str):
    res = 0
    raw_ranges = []
    for line in data.splitlines():
        if "-" in line:
            start, stop = line.split("-")
            start = int(start)
            stop = int(stop)
            raw_ranges.append((start, stop))

    handled_intervalls = []
    ranges = raw_ranges.copy()
    handled_intervalls = run_loop(ranges)

    for intervall in handled_intervalls:
        start, stop = intervall
        res += stop - start + 1
    return res

puzzle = Puzzle(year=2025, day=5)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data))
assert sol_a == example.answer_a, f"Got {sol_a}, expected {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = "14"
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
assert int(sol_answer_b) > 332023203631941, f"{sol_answer_b}"
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")