from aocd.models import Puzzle
from aocd.examples import Example

from utils.linked_list import LinkedList, Node

def split_str(data):
    return str(int(data[0:int(len(data)/2)])), str(int(data[int(len(data)/2):]))

def get_length(blink_list):
    length = 0
    for _ in blink_list:
        length += 1
    return length

def solution_a(data: str):
    blink_list = LinkedList(data.splitlines()[0].split(" "))

    blink = 0
    while blink < 25:
        current_node = blink_list.head
        while current_node:
            if current_node.data == "0":
                current_node.data = "1"
            elif len(current_node.data) % 2 == 0:
                first, second = split_str(current_node.data)
                new_node = Node(second)
                new_node.next = current_node.next
                current_node.next = new_node
                current_node.data = first
                current_node = current_node.next
            else:
                current_node.data = str(int(current_node.data) * 2024)
            current_node = current_node.next
        blink += 1
    return get_length(blink_list)

def solution_b(data: str):
    full_list = data.splitlines()[0].split(" ")
    result = 0
    for value in full_list:
        blink_list = LinkedList([value])

        blink = 0
        while blink < 75:
            current_node = blink_list.head
            while current_node:
                if current_node.data == "0":
                    current_node.data = "1"
                elif len(current_node.data) % 2 == 0:
                    first, second = split_str(current_node.data)
                    new_node = Node(second)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    current_node.data = first
                    current_node = current_node.next
                else:
                    current_node.data = str(int(current_node.data) * 2024)
                current_node = current_node.next
            blink += 1
            print(blink)
        result += get_length(blink_list)
    return result

puzzle = Puzzle(year=2024, day=11)
example: Example = puzzle.examples[0]
input_data = """125 17"""
assert str(solution_a(input_data)) == example.answer_a
print(f"Solution_a: {solution_a(puzzle.input_data)}")

# answer_b = None
# assert answer_b is not None
# assert str(solution_b(input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")