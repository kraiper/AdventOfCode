from typing import Dict
from aocd.models import Puzzle
from aocd.examples import Example

directories = {}

def create_dir_structure(data: Dict, commands):
    command: str = commands.pop(0)
    if "cd" in command:
        if ".." in command:
            return
        elif "/" in command:
            create_dir_structure(directories, commands)
        else:
            create_dir_structure(data[command.split(" ")[-1]], commands)
    if "ls" in command:
        while len(commands) > 0 and "$" not in commands[0]:
            command = commands.pop(0)
            if "dir" in command:
                data[command.split(" ")[-1]] = {}
            else:
                data[command.split(" ")[-1]] = int(command.split(" ")[0])
    if len(commands) > 0:
        create_dir_structure(data, commands)

def solution_a(data: str):
    commands = data.splitlines()
    create_dir_structure(directories, commands)
    print(directories)
    pass

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2022, day=7)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = None
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")