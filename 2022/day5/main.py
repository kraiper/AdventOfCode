from calendar import c
from aocd.models import Puzzle
from aocd.examples import Example

def _parse_stack(stack: list[str]):
    nr_of_stacks = int(stack.pop(-1)[-2])
    crate_stacks = [[] for _ in range(nr_of_stacks)]
    for crates in stack:
        offset = 0
        while offset < nr_of_stacks:
            if crates[1 + offset*4] != " ":
                crate_stacks[offset].insert(0, crates[1 + offset*4])
            offset += 1
    return crate_stacks

def _parse_move(move: str):
    moves = move.split(" ")
    amount = int(moves[1])
    from_stack = int(moves[3])
    to_stack = int(moves[5])
    return amount, from_stack, to_stack

def solution_a(data: str):
    lines = []
    for line in data.splitlines():
        lines.append(line)

    stack = []
    for s in lines:
        if len(s) > 0:
            stack.append(s)
        else:
            break  
    stack = _parse_stack(stack)
    for line in lines:
        if "move" in line:
            amount, from_stack, to_stack = _parse_move(line)
            for _ in range(amount):
                stack[to_stack-1].append(stack[from_stack-1].pop(-1))
    result = ""
    for s in stack:
        result += "".join(s[-1])
    return result

def solution_b(data: str):
    lines = []
    for line in data.splitlines():
        lines.append(line)

    stack = []
    for s in lines:
        if len(s) > 0:
            stack.append(s)
        else:
            break  
    stack = _parse_stack(stack)
    for line in lines:
        if "move" in line:
            amount, from_stack, to_stack = _parse_move(line)
            moving = []
            for _ in range(amount):
                moving.append(stack[from_stack-1].pop(-1))
            for _ in range(amount):
                stack[to_stack-1].append(moving.pop(-1))
    result = ""
    for s in stack:
        result += "".join(s[-1])
    return result

puzzle = Puzzle(year=2022, day=5)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = "MCD"
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")