import math
from operator import mul
from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    possible_game = []
    for line in data.splitlines():
        game_index, cubes = line.split(":")
        game_index = int(game_index.split(" ")[1])
        rounds = cubes.split(";")

        max_cubes = {}
        max_grap_size = 0
        for round in rounds:
            grabs = round.split(",")
            grab_size = 0
            for grab in grabs:
                grab = grab.strip().split(" ")
                grab_size += int(grab[0])
                if grab[1] not in max_cubes:
                    max_cubes[grab[1]] = int(grab[0])
                else:
                    if max_cubes[grab[1]] < int(grab[0]):
                        max_cubes[grab[1]] = int(grab[0])
            if max_grap_size < grab_size:
                max_grap_size = grab_size
            

        if max_cubes["red"] < 13 and max_cubes["green"] < 14 and max_cubes["blue"] < 15 and max_grap_size < 40:
            possible_game.append(game_index)
    return sum(possible_game)

def solution_b(data: str):
    result = 0
    for line in data.splitlines():
        game_index, cubes = line.split(":")
        game_index = int(game_index.split(" ")[1])
        rounds = cubes.split(";")

        max_cubes = {}
        max_grap_size = 0
        for round in rounds:
            grabs = round.split(",")
            grab_size = 0
            for grab in grabs:
                grab = grab.strip().split(" ")
                grab_size += int(grab[0])
                if grab[1] not in max_cubes:
                    max_cubes[grab[1]] = int(grab[0])
                else:
                    if max_cubes[grab[1]] < int(grab[0]):
                        max_cubes[grab[1]] = int(grab[0])
            if max_grap_size < grab_size:
                max_grap_size = grab_size
        power_of_game = 1
        for color, amount in max_cubes.items():
            power_of_game *= int(amount)
        result += power_of_game
    return result

puzzle = Puzzle(year=2023, day=2)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 2286
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")