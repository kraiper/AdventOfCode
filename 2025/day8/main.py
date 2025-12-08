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
        dist, _, _ = value[0]
        if dist != 0 and dist < shortest:
            shortest = dist
            shortest_index = index

    return dist_list[shortest_index].pop(0)

def solution_a(data: str, loops: int):
    coord_list = []
    for line in data.splitlines():
        x, y, z = line.split(",")
        coord_list.append((int(x), int(y), int(z)))

    dist_list = []

    for index_c1, c1 in enumerate(coord_list):
        index_dists = []
        for index_c2, c2 in enumerate(coord_list):
            dist = calc_euclidean_distance(c1, c2)
            if index_c1 != index_c2:
                index_dists.append((float(dist), index_c1, index_c2))
        index_dists.sort()
        dist_list.append(index_dists)

    loop = 0
    light_groups: list[set] = []
    while loop < loops - 1:
        next = False
        shortest_dist, c1, c2 = pop_shortest(dist_list)
        exists = False
        added = False
        for lights in light_groups:
            if c1 in lights and c2 in lights:
                exists = True
                break
            elif c1 in lights or c2 in lights:
                added = True
                lights.add(c1)
                lights.add(c2)
                next = True
        if not exists and not added:
            light_groups.append(set())
            light_groups[-1].add(c1)
            light_groups[-1].add(c2)
            next = True

        if next:
            loop += 1

        si1 = 0

        while si1 < len(light_groups):
            si2 = si1 + 1
            while si2 < len(light_groups):
                if light_groups[si1] & light_groups[si2]:
                    light_groups[si1].update(light_groups[si2])
                    light_groups.pop(si2)
                else:
                    si2 += 1
            si1 += 1

    print(light_groups)

    size = [len(s) for s in light_groups]
    size.sort(reverse=True)
    return size[0] * size[1] * size[2]

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2025, day=8)
example: Example = puzzle.examples[0]

sol_a = str(solution_a(example.input_data, 10))
assert sol_a == example.answer_a, f"Got {sol_a}, expected {example.answer_a}"
start = time.time()
sol_answer_a = str(solution_a(puzzle.input_data, 1000))
end = time.time()
assert int(sol_answer_a) > 4050
assert int(sol_answer_a) < 194300
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = None
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")