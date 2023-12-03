from curses.ascii import isdigit
from aocd.models import Puzzle
from aocd.examples import Example

def _check_index_in_numbers(column, numbers, adjacent_numbers):
    for number in numbers:
        if column in list(number.values())[0]:
            adjacent_numbers.append(list(number.keys())[0])
            numbers.remove(number)
            return

def solution_a(data: str):
    lines = data.splitlines()
    number_indexes = {}
    symbols = []
    row = 0
    for line in lines:
        column = 0
        while column < len(line):
            if line[column] != '.' and not isdigit(line[column]):
                symbols.append({line[column]: (row, column)})
            column += 1
        row += 1
    row = 0
    for line in lines:
        column = 0
        number_indexes[row] = []
        while column < len(line):
            if isdigit(line[column]):
                n = line[column]
                s = set([column])
                while column+1 < len(line) and isdigit(line[column+1]):
                    column += 1
                    s.add(column)
                    n += line[column]
                number_indexes[row].append({n: s})
                column += 1
            column += 1
        row += 1
    
    adjacent_numbers = []

    for symbol in symbols:
        row, column = list(symbol.values())[0]
        if row > 0:
            _check_index_in_numbers(column, number_indexes[row-1], adjacent_numbers)
            if column > 0:
                _check_index_in_numbers(column - 1, number_indexes[row-1], adjacent_numbers)
            if column < len(lines[0]) - 1:
                _check_index_in_numbers(column + 1, number_indexes[row-1], adjacent_numbers)

        if row < len(lines) - 1:
            _check_index_in_numbers(column, number_indexes[row+1], adjacent_numbers)
            if column > 0:
                _check_index_in_numbers(column - 1, number_indexes[row+1], adjacent_numbers)
            if column < len(lines[0]) - 1:
                _check_index_in_numbers(column + 1, number_indexes[row+1], adjacent_numbers)

        if column > 0:
            _check_index_in_numbers(column - 1, number_indexes[row], adjacent_numbers)
            if row > 0:
                _check_index_in_numbers(column - 1, number_indexes[row-1], adjacent_numbers)
            if row < len(lines) - 1:
                _check_index_in_numbers(column - 1, number_indexes[row+1], adjacent_numbers)

        if column < len(lines[0]) - 1:
            _check_index_in_numbers(column + 1, number_indexes[row], adjacent_numbers)
            if row > 0:
                _check_index_in_numbers(column + 1, number_indexes[row-1], adjacent_numbers)
            if row < len(lines) - 1:
                _check_index_in_numbers(column + 1, number_indexes[row+1], adjacent_numbers)

    sum = 0
    for number in adjacent_numbers:
        sum += int(number)
    return sum
    

def solution_b(data: str):
    lines = data.splitlines()
    number_indexes = {}
    symbols = []
    row = 0
    for line in lines:
        column = 0
        while column < len(line):
            if line[column] != '.' and not isdigit(line[column]):
                symbols.append({line[column]: (row, column)})
            column += 1
        row += 1
    row = 0
    for line in lines:
        column = 0
        number_indexes[row] = []
        while column < len(line):
            if isdigit(line[column]):
                n = line[column]
                s = set([column])
                while column+1 < len(line) and isdigit(line[column+1]):
                    column += 1
                    s.add(column)
                    n += line[column]
                number_indexes[row].append({n: s})
                column += 1
            column += 1
        row += 1
    
    for symbol in symbols:
        if list(symbol.keys())[0] != "*":
            symbols.remove(symbol)

    sum = 0
    for symbol in symbols:
        adjacent_numbers = []
        row, column = list(symbol.values())[0]
        if row > 0:
            _check_index_in_numbers(column, number_indexes[row-1], adjacent_numbers)
            if column > 0:
                _check_index_in_numbers(column - 1, number_indexes[row-1], adjacent_numbers)
            if column < len(lines[0]) - 1:
                _check_index_in_numbers(column + 1, number_indexes[row-1], adjacent_numbers)

        if row < len(lines) - 1:
            _check_index_in_numbers(column, number_indexes[row+1], adjacent_numbers)
            if column > 0:
                _check_index_in_numbers(column - 1, number_indexes[row+1], adjacent_numbers)
            if column < len(lines[0]) - 1:
                _check_index_in_numbers(column + 1, number_indexes[row+1], adjacent_numbers)

        if column > 0:
            _check_index_in_numbers(column - 1, number_indexes[row], adjacent_numbers)
            if row > 0:
                _check_index_in_numbers(column - 1, number_indexes[row-1], adjacent_numbers)
            if row < len(lines) - 1:
                _check_index_in_numbers(column - 1, number_indexes[row+1], adjacent_numbers)

        if column < len(lines[0]) - 1:
            _check_index_in_numbers(column + 1, number_indexes[row], adjacent_numbers)
            if row > 0:
                _check_index_in_numbers(column + 1, number_indexes[row-1], adjacent_numbers)
            if row < len(lines) - 1:
                _check_index_in_numbers(column + 1, number_indexes[row+1], adjacent_numbers)
        if len(adjacent_numbers) == 2:
            sum += int(adjacent_numbers[0]) * int(adjacent_numbers[1])

    return sum

puzzle = Puzzle(year=2023, day=3)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 467835
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")