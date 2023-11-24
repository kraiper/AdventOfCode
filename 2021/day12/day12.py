def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += str(ele)

        # return string
    return str1


def read_lines(file_name):
    file = open(file_name)
    file_content = file.readlines()
    i = 0
    while i < len(file_content):
        file_content[i] = file_content[i].rstrip("\n")
        i += 1
    return file_content


class Move():
    def __init__(self, path, next_move, small_visit = True):
        self.path = []
        self.path.extend(path)
        self.next_move = next_move
        self.small_visit = small_visit


def p1():
    lines = read_lines("day12/input.txt")

    cave_system = {}
    for line in lines:
        letter = line.split("-")

        if letter[0] not in cave_system:
            cave_system[letter[0]] = [letter[1]]
        else:
            cave_system[letter[0]].append(letter[1])

        if letter[1] not in cave_system:
            cave_system[letter[1]] = [letter[0]]
        else:
            cave_system[letter[1]].append(letter[0])

    paths = []
    next_move = []
    for path in cave_system["start"]:
        next_move.append(Move(["start"], path))

    while len(next_move) > 0:
        nm = next_move.pop()
        if nm.next_move == "end":
            nm.path.append(nm.next_move)
            paths.append(nm)
        if nm.next_move.islower() and nm.next_move in nm.path:
            continue
        nm.path.append(nm.next_move)
        for p in cave_system[nm.next_move]:
            next_move.append(Move(nm.path, p))

    print(len(paths))


def p2():
    lines = read_lines("day12/input.txt")

    cave_system = {}
    for line in lines:
        letter = line.split("-")

        if letter[0] not in cave_system:
            cave_system[letter[0]] = [letter[1]]
        else:
            cave_system[letter[0]].append(letter[1])

        if letter[1] not in cave_system:
            cave_system[letter[1]] = [letter[0]]
        else:
            cave_system[letter[1]].append(letter[0])

    paths = []
    next_move = []
    for path in cave_system["start"]:
        next_move.append(Move(["start"], path, True))

    while len(next_move) > 0:
        nm = next_move.pop()
        if nm.next_move == "end":
            nm.path.append(nm.next_move)
            paths.append(nm)
        if nm.next_move.islower() and nm.next_move in nm.path:
            if not nm.small_visit or nm.next_move == "start" or nm.next_move == "end":
                continue
            else:
                nm.small_visit = False
        nm.path.append(nm.next_move)
        for p in cave_system[nm.next_move]:
            next_move.append(Move(nm.path, p, nm.small_visit))



    print(len(paths))


# p1()
p2()

