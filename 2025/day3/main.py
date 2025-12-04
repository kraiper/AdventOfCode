from aocd.models import Puzzle
from aocd.examples import Example
import time

def number_search(line: str, highest: int, num_index_1: int, num_index_2: int):
    current_number = int(line[num_index_1] + line[num_index_2])
    if highest < current_number:
        highest = current_number
    if num_index_2 < len(line) - 1:
        return number_search(line, highest, num_index_1, num_index_2 + 1)
    else:
        return highest

def solution_a(data: str):
    lines = data.split("\n")
    res = 0
    for line in lines:
        line_max = 0
        for start_index in range(len(line) - 1):
            index_max = number_search(line, 0, start_index, start_index+1)
            if line_max < index_max:
                line_max = index_max
        res += line_max
    return res

# def number_search_2(line: str, highest: int, indexes: list, moving_index: int):
#     current_number = ""
#     print(indexes)
#     for num in indexes:
#         current_number += line[num]
#     current_number = int(current_number)

#     if highest < current_number:
#         highest = current_number

#     if indexes[-1] < len(line) - 1:
#         indexes[-1] += 1
#         return number_search_2(line, highest, indexes, moving_index)
#     elif moving_index == 0 and indexes[moving_index] + 11 == len(line) - 1:
#         print("returning")
#         return highest
#     else: # indexes[moving_index] == len(line) - 1:
#         if (11 - moving_index) + indexes[moving_index] < len(line) - 1:
#             next_moving_index = moving_index
#         else:
#             next_moving_index = moving_index - 1

#         moves = 0
#         step_value = indexes[next_moving_index] + 1
#         while next_moving_index + moves < 12:
#             indexes[next_moving_index + moves] = step_value + moves
#             moves += 1
#         return number_search_2(line, highest, indexes, next_moving_index)



def number_search_2(line: str, highest: int, indexes: list, moving_index: int):
    ### Check current value
    current_number = ""
    for num in indexes:
        current_number += line[num]
    current_number = int(current_number)

    if highest < current_number:
        highest = current_number

    ### index logic

    ### last index loop
    if moving_index == len(indexes) - 1:
        if indexes[moving_index] == len(line) - 1:
            return highest
        indexes[-1] += 1
        number_search_2(line, highest, indexes, moving_index)

    while indexes[moving_index] < len(line) - (len(indexes) - moving_index):
        moves = 0
        step_value = indexes[moving_index] + 1
        while moving_index + moves < 12:
            indexes[moving_index + moves] = step_value + moves
            moves += 1
        number_search_2(line, highest, indexes, moving_index + 1)
    

    # if indexes[-1] < len(line) - 1:
    #     indexes[-1] += 1
    #     return number_search_2(line, highest, indexes, moving_index)
    # elif moving_index == 0 and indexes[moving_index] + 11 == len(line) - 1:
    #     print("returning")
    #     return highest
    # else: # indexes[moving_index] == len(line) - 1:
    #     if (11 - moving_index) + indexes[moving_index] < len(line) - 1:
    #         next_moving_index = moving_index
    #     else:
    #         next_moving_index = moving_index - 1

    #     moves = 0
    #     step_value = indexes[next_moving_index] + 1
    #     while next_moving_index + moves < 12:
    #         indexes[next_moving_index + moves] = step_value + moves
    #         moves += 1
    #     return number_search_2(line, highest, indexes, next_moving_index)


def solution_b(data: str):
    lines = data.split("\n")
    res = 0
    for line in lines:
        line_max = 0
        step = 0
        indexes = [x + step for x in range(12)]
        loop_max = 0
        for x in range(12):
            loop_max = number_search_2(line, line_max, indexes, x)
            print(loop_max)
        res += line_max
    return res

puzzle = Puzzle(year=2025, day=3)
example: Example = puzzle.examples[0]


# assert str(solution_a(example.input_data)) == example.answer_a
# start = time.time()
# sol_answer_a = str(solution_a(puzzle.input_data))
# end = time.time()
# print(f"Solution_a: {sol_answer_a} - time taken: {end - start}")

answer_b = 3121910778619
assert answer_b is not None
sol_b = str(solution_b(example.input_data))
assert sol_b == str(answer_b), f"{answer_b}, {sol_b}"
start = time.time()
sol_answer_b = str(solution_b(puzzle.input_data))
end = time.time()
print(f"Solution_b: {sol_answer_b} - time taken: {end - start}")