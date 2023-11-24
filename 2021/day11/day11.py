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


def print_octo(octo):

    for o in octo:
        out_str = ""
        for b in o:
            out_str = out_str + str(b.value)

        print(out_str)


def test(test_dict, iteration):
    lines = []
    if iteration == 1:
        lines = read_lines("day11/test1.txt")

    if iteration == 2:
        lines = read_lines("day11/test2.txt")

    octo_dict = {}
    i = 0
    while i < len(lines):
        y = 0
        octo_dict[i] = {}
        line_list = list(lines[i])
        while y < 10:
            octo_dict[i][y] = int(line_list[y])
            y += 1
        i += 1

    if octo_dict == test_dict:
        print("iteration: ", iteration, True)
    else:
        print("iteration: ", iteration, False)


class Octopus:
    def __init__(self, value):
        self.value = value
        self.flashed = False

    def should_flash(self):
        return self.value > 9

    def increment(self):
        self.value += 1

    def flash(self):
        self.flashed = True

    def rest(self):
        self.flashed = False
        if self.value > 9:
            self.value = 0

    def is_flashed(self):
        return self.flashed


def p1():
    lines = read_lines("day11/input.txt")
    octo_dict = [None] * 10

    i = 0
    while i < 10:
        octo_dict[i] = []
        i += 1

    i = 0
    while i < 10:
        y = 0
        line_list = list(lines[i])
        while y < 10:
            octo_dict[i].append(Octopus(int(line_list[y])))
            y += 1
        i += 1

    iteration = 0
    nr_of_flashes = 0

    while iteration < 500:
        i = 0
        while i < 10:
            y = 0
            while y < 10:
                octo_dict[i][y].increment()
                y += 1
            i += 1

        flashed = 1
        while flashed > 0:
            flashed = 0
            i = 0
            while i < 10:
                y = 0
                while y < 10:
                    if octo_dict[i][y].should_flash() and not octo_dict[i][y].is_flashed():
                        flashed += 1
                        nr_of_flashes += 1
                        octo_dict[i][y].flash()
                        if i != 9:
                            octo_dict[i + 1][y].increment()
                        if i != 0:
                            octo_dict[i - 1][y].increment()
                        if y != 0:
                            octo_dict[i][y - 1].increment()
                        if y != 9:
                            octo_dict[i][y + 1].increment()
                        if i != 0 and y != 9:
                            octo_dict[i - 1][y + 1].increment()
                        if i != 9 and y != 9:
                            octo_dict[i + 1][y + 1].increment()
                        if i != 0 and y != 0:
                            octo_dict[i - 1][y - 1].increment()
                        if i != 9 and y != 0:
                            octo_dict[i + 1][y - 1].increment()
                    y += 1
                i += 1

        i = 0
        nr_of_resting = 0
        while i < 10:
            y = 0
            while y < 10:
                octo_dict[i][y].rest()
                if octo_dict[i][y].value == 0:
                    nr_of_resting += 1
                y += 1
            i += 1
        iteration += 1
        if nr_of_resting == 100:
            print(iteration)
            break

    print(nr_of_flashes)


p1()

