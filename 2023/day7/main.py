from math import e
from operator import index, le
from os import linesep
import re
from aocd.models import Puzzle
from aocd.examples import Example


def _sort_hands(hands):
    result_list = []
    power_list = list(hands.keys())
    power_list.sort()
    power_list.reverse()
    for power in power_list:
        result_list.append(hands[power])
    return result_list

def solution_a(data: str):
    card_power = {"2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
    lines = data.splitlines()
    hands = {"5": {}, "4": {}, "3.5": {}, "3": {}, "2.5": {}, "2": {}, "1": {}}
    for line in lines:
        cards, bet = line.split(" ")
        max_number = 0
        pair_check = 0
        hand_power = ""
        for card in cards:
            hand_power += card_power[card]
        hand_power = int(hand_power)
        for card in cards:
            count = cards.count(card)
            if count > max_number:
                max_number = count
            if count == 2:
                pair_check += 1
        if pair_check == 4:
            hands["2.5"][hand_power] = bet
        elif max_number == 3 and pair_check == 2:
            hands["3.5"][hand_power] = bet
        else:
            hands[str(max_number)][hand_power] = bet
    ranking_list = []

    for hand in hands.values():
        ranking_list.extend(_sort_hands(hand))
    assert len(ranking_list) == len(lines)

    r_index = 0
    result = 0
    ranking_list.reverse()
    while r_index < len(ranking_list):
        result += int(ranking_list[r_index]) * (r_index + 1)
        r_index += 1

    return result

def solution_b(data: str):
    card_power = {"2": "02", "3": "03", "4": "04", "5": "05", "6": "06", "7": "07", "8": "08", "9": "09", "T": "10", "J": "01", "Q": "12", "K": "13", "A": "14"}

    lines = data.splitlines()
    hands = {"5": {}, "4": {}, "3.5": {}, "3": {}, "2.5": {}, "2": {}, "1": {}}
    for line in lines:
        cards, bet = line.split(" ")
        max_number = 0
        pair_check = 0
        triss_check = 0
        hand_power = ""
        for card in cards:
            hand_power += card_power[card]
        hand_power = int(hand_power)
        jokers = cards.count("J")
        for card in cards:
            count = cards.count(card)
            if count > max_number:
                max_number = count
            if count == 2:
                pair_check += 1
        target = ""
        if pair_check == 4:
            target = "2.5"
        elif max_number == 3 and pair_check == 2:
            target = "3.5"
        else:
            target = str(max_number)
        
        if jokers > 0:
            if jokers == 1:
                if target == "2.5":
                    target = "3.5"
                elif target == "3.5":
                    target = "4"
                else:
                    target = str(int(target) + 1)
            elif jokers == 2:
                if target == "2":
                    target = "3"
                elif target == "2.5":
                    target = "4"
                elif target == "3.5":
                    target = "5"
                elif target == "4":
                    target = "5"
            elif jokers == 3:
                if target == "3":
                    target = "4"
                elif target == "3.5":
                    target = "5"
            elif jokers == 4:
                target = "5"

        hands[target][hand_power] = bet
    ranking_list = []

    for hand in hands.values():
        ranking_list.extend(_sort_hands(hand))
    assert len(ranking_list) == len(lines)

    r_index = 0
    result = 0
    ranking_list.reverse()
    while r_index < len(ranking_list):
        result += int(ranking_list[r_index]) * (r_index + 1)
        r_index += 1

    return result

puzzle = Puzzle(year=2023, day=7)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

answer_b = 5905
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")