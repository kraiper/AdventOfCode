from aocd.models import Puzzle
from aocd.examples import Example
import re

def solution_a(data: str):
    result = 0
    for line in data.splitlines():
        numbers = line.split(": ")[1]
        winning_numbers = numbers.split(" | ")[0]
        my_numbers = numbers.split(" | ")[1]
        winning_numbers = re.findall(r"\d+", winning_numbers)
        my_numbers = re.findall(r"\d+", my_numbers)

        card_winning = 0

        for number in my_numbers:
            if number in winning_numbers:
                if card_winning == 0:
                    card_winning += 1
                else:
                    card_winning *= 2
        result += card_winning
    return result     

def solution_b(data: str):
    result = 0
    sum_cards = {}
    card_winnings = {}
    extra_cards = []
    for line in data.splitlines():
        card_number = int(line.split(": ")[0].split(" ")[-1])
        sum_cards[card_number] = 0
        card_winnings[card_number] = []
        numbers = line.split(": ")[1]
        winning_numbers = numbers.split(" | ")[0]
        my_numbers = numbers.split(" | ")[1]
        winning_numbers = re.findall(r"\d+", winning_numbers)
        my_numbers = re.findall(r"\d+", my_numbers)
        lot_winning = 0
        sum_cards[card_number] += 1
        for number in my_numbers:
            if number in winning_numbers:
                lot_winning += 1
                card_winnings[card_number].append(card_number + lot_winning)
                extra_cards.append(card_number + lot_winning)

    while extra_cards:
        card_number = extra_cards.pop()
        extra_cards.extend(card_winnings[card_number])
        sum_cards[card_number] += 1

    for value in sum_cards.values():
        result += value
    return result  

puzzle = Puzzle(year=2023, day=4)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 30
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")