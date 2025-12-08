from aocd.models import Puzzle
from aocd.examples import Example
import time
import numpy as np

def calc_euclidean_distance(c1: tuple, c2: tuple):
    x1_coords, y1_coords, z1_coords = c1
    x2_coords, y2_coords, z2_coords = c2
    p1 = np.array([x1_coords, y1_coords, z1_coords])
    p2 = np.array([x2_coords, y2_coords, z2_coords])
    return np.linalg.norm(p1 - p2)


def pop_shortest(dist_list: list):
    shortest = 99999999999999999999999
    shortest_index = 0

    for index, value in enumerate(dist_list):
        dist, _, _ = value
        if dist != 0 and dist < shortest:
            shortest = dist
            shortest_index = index

    return dist_list.pop(shortest_index)

def solution_a(data: str, loops: int):
    coord_list = []
    for line in data.splitlines():
        x, y, z = line.split(",")
        coord_list.append((int(x), int(y), int(z)))

    dist_list = []

    for index_c1, c1 in enumerate(coord_list):
        shortest = 9999999999999999999
        for index_c2, c2 in enumerate(coord_list):
            dist = calc_euclidean_distance(c1, c2)
            if dist < shortest and index_c1 != index_c2:
                shortest = dist
                shortest_index = index_c2
        dist_list.append((shortest, index_c1, shortest_index))

    print(dist_list)

    loop = 0
    light_groups: list[set] = []
    while loop < loops:
        shortest_dist, c1, c2 = pop_shortest(dist_list)
        exists = False
        added = False
        for lights in light_groups:
            if c1 in lights and c2 in lights:
                exists = True
                loop -= 1
                break
            elif c1 in lights or c2 in lights:
                added = True
                lights.add(c1)
                lights.add(c2)
                break
        if not exists and not added:
            light_groups.append(set())
            light_groups[-1].add(c1)
            light_groups[-1].add(c2)
        loop += 1

    print(light_groups)


    pass

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2025, day=8)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data, 10))
assert sol_a == example.answer_a, f"Got {sol_a}, expected {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data, 1000))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = None
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")