from pathlib import Path
import time

answer_a = None
answer_b = None


def read_file(file_str: str):
    data_lines: list[str] = []
    with open(file_str, "r") as f:
        data_lines = f.readlines()

    return data_lines

def solution_a(file_str: str):
    data_lines = read_file(file_str)
    res = 0
    for line in data_lines:
        line = line.strip()
        if "x" in line:
            board_str, shapes_str = line.split(":")
            x, y = [int(x) for x in board_str.strip().split("x")]
            shapes = [int(x) for x in shapes_str.strip().split(" ")]
            if x * y >= sum(shapes) * 9:
                res += 1
    return res

def solution_b(file_str: str):
    data_lines = read_file(file_str)
    




example_file = Path(__file__).parent / "example.txt"
data_file = Path(__file__).parent / "data.txt"

# assert answer_a is not None
# sol_a = str(solution_a(example_file))
# assert sol_a == answer_a, f"Got {sol_a}, expected {answer_a}"
start = time.time()
sol_answer_a = str(solution_a(data_file))
end = time.time()
print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")


# assert answer_b is not None
# sol_b = str(solution_b(example_file))
# assert sol_b == str(answer_b), f"Got {sol_b}, expected {answer_b}"
# start = time.time()
# sol_answer_b = str(solution_b(data_file))
# end = time.time()
# print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")