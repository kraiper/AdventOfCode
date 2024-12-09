from aocd.models import Puzzle
from aocd.examples import Example

def solution_a(data: str):
    array = [[] for _ in range(len(data.splitlines()))] # row, column
    row = 0
    nodes = {}
    for line in data.splitlines():
        for x in line:
            array[row].append(x)
        row += 1

    row = 0
    while row < len(array):
        column = 0
        while column < len(array[0]):
            value = array[row][column]
            if array[row][column] != ".":
                if value not in nodes:
                    nodes[value] = [(row, column)]
                else:
                    nodes[value].append((row, column))
            column += 1
        row += 1

    result_points = []
    for _, points in nodes.items():
        for p_1 in points:
            for p_2 in points:
                if p_1 != p_2:
                    n_1, n_2 = p_1
                    m_1, m_2 = p_2
                    r_1 = n_1 - m_1
                    r_2 = n_2 - m_2
                    if n_1 + r_1 >= 0 and n_1 + r_1 < len(array) and n_2 + r_2 >= 0 and n_2 + r_2 < len(array[0]):
                        result_points.append((n_1 + r_1, n_2 + r_2))
                        array[n_1 + r_1][n_2 + r_2]  = "#"

    result_points = [t for t in (set(tuple(i) for i in result_points))]
    return len(result_points)

def solution_b(data: str):
    array = [[] for _ in range(len(data.splitlines()))] # row, column
    row = 0
    nodes = {}
    for line in data.splitlines():
        for x in line:
            array[row].append(x)
        row += 1

    row = 0
    while row < len(array):
        column = 0
        while column < len(array[0]):
            value = array[row][column]
            if array[row][column] != ".":
                if value not in nodes:
                    nodes[value] = [(row, column)]
                else:
                    nodes[value].append((row, column))
            column += 1
        row += 1

    result_points = []
    for _, points in nodes.items():
        for p_1 in points:
            for p_2 in points:
                if p_1 != p_2:
                    n_1, n_2 = p_1
                    m_1, m_2 = p_2
                    r_1 = n_1 - m_1
                    r_2 = n_2 - m_2
                    step_1 = r_1
                    step_2 = r_2
                    result_points.append((n_1, n_2))
                    stop = False
                    while not stop:
                        if n_1 + r_1 >= 0 and n_1 + r_1 < len(array) and n_2 + r_2 >= 0 and n_2 + r_2 < len(array[0]):
                            result_points.append((n_1 + r_1, n_2 + r_2))
                            array[n_1 + r_1][n_2 + r_2]  = "#"
                            r_1 += step_1
                            r_2 += step_2
                        else:
                            stop = True

    result_points = [t for t in (set(tuple(i) for i in result_points))]
    print(len(result_points))
    return len(result_points)

puzzle = Puzzle(year=2024, day=8)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 34
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")