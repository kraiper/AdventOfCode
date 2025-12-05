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

def solution_b(data: str):
    fresh_ranges = []
    for line in data.splitlines():
        if "-" in line:
            start, stop = line.split("-")
            start = int(start)
            stop = int(stop)
            add = True
            pops = []
            for ran in fresh_ranges:
                o_start, o_stop = ran
                ### new range within old range
                if start >= o_start and stop <= o_stop:
                    add = False
                    break

                ### 
                if start >= o_start and start <= o_stop:
                    start = o_stop + 1
                if stop >= o_start and stop <= o_stop:
                    stop = o_start - 1

            if add:
                fresh_ranges.append((start, stop))

    res = 0
    for x in fresh_ranges:
        start, stop = x
        # for v in range(start, stop + 1):
        #     print(v)

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
assert int(sol_b) > 330256053047770
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")