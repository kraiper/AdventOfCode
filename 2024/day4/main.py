from aocd.models import Puzzle
from aocd.examples import Example

offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),  (1, -1), (1, 0), (1, 1)]


def check_array_XMAS(xmas_array, row, column):
    result = 0
    for offset in offsets:
        o_row, o_column = offset
        test_str = ""
        try:
            if (
                row + (o_row * 3) >= 0 and row + (o_row * 3) < len(xmas_array) and
                column + (o_column * 3) >= 0 and column + (o_column * 3) < len(xmas_array[0])
                ):
                test_str = (
                    f"{xmas_array[row + (o_row * 0)][column + (o_column * 0)]}"
                    f"{xmas_array[row + (o_row * 1)][column + (o_column * 1)]}"
                    f"{xmas_array[row + (o_row * 2)][column + (o_column * 2)]}"
                    f"{xmas_array[row + (o_row * 3)][column + (o_column * 3)]}"
                )
                if test_str == "XMAS":
                    result += 1
        except:
            test_str = ""
            continue
    return result

def check_array_MAS(xmas_array, row, column):
    result = 0
    try:
        if (
            row - 1 >= 0 and row + 1 < len(xmas_array) and
            column - 1 >= 0 and column + 1 < len(xmas_array[0])
            ):
            test_str_1 = (
                f"{xmas_array[row - 1][column - 1]}"
                f"{xmas_array[row][column]}"
                f"{xmas_array[row + 1][column + 1]}"
            )
            test_str_2 = (
                f"{xmas_array[row - 1][column + 1]}"
                f"{xmas_array[row][column]}"
                f"{xmas_array[row + 1][column - 1]}"
            )
            if (test_str_1 == "MAS" or test_str_1 == "SAM") and (test_str_2 == "MAS" or test_str_2 == "SAM"):
                result += 1
    except:
        pass
    return result

def solution_a(data: str):
    xmas_array = [[] for _ in range(len(data.splitlines()))] # row, column
    row = 0
    for line in data.splitlines():
        for x in line:
            xmas_array[row].append(x)
        row += 1
    result = 0
    row = 0
    while row < len(xmas_array):
        column = 0
        while column < len(xmas_array[0]):
            if xmas_array[row][column] == "X":
                result += check_array_XMAS(xmas_array, row, column)
            column += 1
        row += 1
    return result

def solution_b(data: str):
    xmas_array = [[] f2029or _ in range(len(data.splitlines()))] # row, column
    row = 0
    for line in data.splitlines():
        for x in line:
            xmas_array[row].append(x)
        row += 1
    result = 0
    row = 0
    while row < len(xmas_array):
        column = 0
        while column < len(xmas_array[0]):
            if xmas_array[row][column] == "A":
                result += check_array_MAS(xmas_array, row, column)
            column += 1
        row += 1
    return result

puzzle = Puzzle(year=2024, day=4)
example: Example = puzzle.examples[0]


assert str(solution_a(example.input_data)) == str(4)

input_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
assert str(solution_a(input_data)) == str(18)
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 9
assert answer_b is not None
assert str(solution_b(input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")