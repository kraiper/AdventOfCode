from aocd.models import Puzzle
from aocd.examples import Example
import re

def solution_a(data: str):
    lines = data.splitlines()
    times = re.findall(r"(\d+)", lines[0])
    times = [int(time) for time in times]
    distances = re.findall(r"(\d+)", lines[1])
    distances = [int(distance) for distance in distances]

    race_index = 0
    wins = [0 for _ in range(len(times))]
    while race_index < len(times):
        time_index = 0
        while time_index < times[race_index]:
            if time_index * (times[race_index] - time_index) > distances[race_index]:
                wins[race_index] += 1
            time_index += 1
        race_index += 1

    result = 1
    for win in wins:
        result *= win
    return result

def solution_b(data: str):
    lines = data.splitlines()
    time = re.findall(r"(\d+)", lines[0].replace(" ", ""))[0]
    time = int(time)
    distance = re.findall(r"(\d+)", lines[1].replace(" ", ""))[0]
    distance = int(distance)
    start_win = 0
    end_win = time
    while start_win * (time - start_win) < distance:
        start_win += 1
    while end_win * (time - end_win) < distance:
        end_win -= 1
    return end_win - start_win + 1

puzzle = Puzzle(year=2023, day=6)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) =="288"
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 71503
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")