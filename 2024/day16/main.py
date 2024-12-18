from aocd.models import Puzzle
from aocd.examples import Example

class Node:
    def __init__(self, weight, pos, dir):
        self.weight = weight
        self.pos = pos
        self.dir = dir
        self.next: Node = None

    def __repr__(self):
        return self.weight

    def __str__(self):
        return f"{self.weight}: {self.pos} {self.dir}"

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def insert_node(node_list: Node, new_node: Node):
    current_node = node_list
    previous_node: Node = None
    while current_node:
        if current_node.weight > new_node.weight:
            new_node.next = current_node
            if previous_node:
                previous_node.next = new_node
                return node_list
            else:
                return new_node
        if not current_node.next:
            current_node.next = new_node
            return node_list
        else:
            previous_node = current_node
            current_node = current_node.next
    return node_list

def print_moves(moves):
    current = moves
    while current:
        print(current)
        current = current.next

def create_board(data: str):
    board = [[] for _ in range(len(data.splitlines()))]
    start = []
    i = 0
    for line in data.splitlines():
        for value in line:
            if value == "S":
                start.append(i)
                start.append(len(board[i]))
            board[i].append(value)
        print(line)
        i += 1
    return board, start

def turn(direction, current):
    if current + direction >= len(directions):
        return 0
    elif current + direction < 0:
        return len(directions) - 1
    return current + direction

def move_char(board: list, moves: Node, visited: []):
    pos_row = moves.pos[0]
    pos_col = moves.pos[1]
    if board[pos_row][pos_col] == "E":
        return False

    move_row = pos_row + directions[moves.dir][0]
    move_col = pos_col + directions[moves.dir][1]
    # Move forward
    if board[move_row][move_col] != "#":
        new_node = Node(moves.weight + 1, [move_row, move_col], moves.dir)
        if new_node.pos not in visited:
            moves = insert_node(moves, new_node)
    # Turn left and move
    move_row_left = pos_row + directions[turn(-1, moves.dir)][0]
    move_col_left = pos_col + directions[turn(-1, moves.dir)][1]
    if board[move_row_left][move_col_left] != "#":
        new_node_left = Node(moves.weight + 1001, [move_row_left, move_col_left], turn(-1, moves.dir))
        if new_node_left.pos not in visited:
            moves = insert_node(moves, new_node_left)
    # Turn right
    move_row_right = pos_row + directions[turn(1, moves.dir)][0]
    move_col_right = pos_col + directions[turn(1, moves.dir)][1]
    if board[move_row_right][move_col_right] != "#":
        new_node_right = Node(moves.weight + 1001, [move_row_right, move_col_right], turn(1, moves.dir))
        if new_node_right.pos not in visited:
            moves = insert_node(moves, new_node_right)
    return True


def solution_a(data: str):
    board, start = create_board(data)
    moves = Node(0, start, 1)
    visited = []
    goal_weights = []
    while moves:
        visited.append(moves.pos)
        if not move_char(board, moves, visited):
            goal_weights.append(moves.weight)
        moves = moves.next

    result_weight = goal_weights[0]
    for weight in goal_weights:
        if weight < result_weight:
            result_weight = weight
    print(goal_weights)
    return result_weight

def solution_b(data: str):
    pass

puzzle = Puzzle(year=2024, day=16)
example: Example = puzzle.examples[0]

assert str(solution_a(example.input_data)) == "7036"
answer_a = solution_a(puzzle.input_data)
assert answer_a != "102508"
assert answer_a < "102508"
print(f"Solution_a: {answer_a}")

answer_b = None
assert answer_b is not None
assert str(solution_b(example.input_data)) == str(answer_b)
print(f"Solution_b: {solution_b(puzzle.input_data)}")