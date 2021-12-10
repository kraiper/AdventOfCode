def p1():
    file = open("day8/input.txt")
    file_content = file.readlines()

    wire_list = []
    display_list = []
    for row in file_content:
        row = row.rstrip("\n")
        s1, s2 = row.split(" | ")
        wire_list.append(s1)
        display_list.append(s2)

    unique_numbers = 0
    for row in display_list:
        numbers = row.split(" ")
        for number in numbers:
            if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
                unique_numbers += 1

    print(unique_numbers)


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += str(ele)

        # return string
    return str1


def print_display(display):
    print(f" {display[0]} ")
    print(f"{display[1]} {display[2]}")
    print(f" {display[3]} ")
    print(f"{display[4]} {display[5]}")
    print(f" {display[6]} ")


def p2():
    file = open("day8/input.txt")
    file_content = file.readlines()
    result = 0
    for row in file_content:
        row = row.rstrip("\n")
        s1, s2 = row.split(" | ")

        ordered_wires = [""] * 10
        digit_list = s1.split(" ")
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 2:
                ordered_wires[1] = digit_list[i]
                digit_list.pop(i)
            elif len(digit_list[i]) == 3:
                ordered_wires[7] = digit_list[i]
                digit_list.pop(i)
            elif len(digit_list[i]) == 4:
                ordered_wires[4] = digit_list[i]
                digit_list.pop(i)
            elif len(digit_list[i]) == 7:
                ordered_wires[8] = digit_list[i]
                digit_list.pop(i)
            else:
                i += 1

        # 3
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 5:
                count_overlap = 0
                for l in list(ordered_wires[1]):
                    if l in list(digit_list[i]):
                        count_overlap += 1
                if count_overlap == 2:
                    ordered_wires[3] = digit_list[i]
                    digit_list.pop(i)
                else:
                    i += 1
            else:
                i += 1

        # 9
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 6:
                count_overlap = 0
                for l in list(ordered_wires[3]):
                    if l in list(digit_list[i]):
                        count_overlap += 1
                if count_overlap == 5:
                    ordered_wires[9] = digit_list[i]
                    digit_list.pop(i)
                else:
                    i += 1
            else:
                i += 1

        # 0
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 6:
                count_overlap = 0
                for l in list(ordered_wires[7]):
                    if l in list(digit_list[i]):
                        count_overlap += 1
                if count_overlap == 3:
                    ordered_wires[0] = digit_list[i]
                    digit_list.pop(i)
                else:
                    i += 1
            else:
                i += 1

        # 6
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 6:
                ordered_wires[6] = digit_list[i]
                digit_list.pop(i)
            else:
                i += 1

        # 5
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 5:
                count_overlap = 0
                for l in list(ordered_wires[9]):
                    if l in list(digit_list[i]):
                        count_overlap += 1
                if count_overlap == 5:
                    ordered_wires[5] = digit_list[i]
                    digit_list.pop(i)
                else:
                    i += 1
            else:
                i += 1

        # 2
        i = 0
        while i < len(digit_list):
            if len(digit_list[i]) == 5:
                ordered_wires[2] = digit_list[i]
                digit_list.pop(i)
            else:
                i += 1

        output = ""
        d_list = s2.split(" ")
        j = 0
        while j < len(d_list):
            k = 0
            while k < len(ordered_wires):
                if len(d_list[j]) == len(ordered_wires[k]):
                    matches = 0
                    for l in list(d_list[j]):
                        if l in list(ordered_wires[k]):
                            matches += 1
                    if matches == len(d_list[j]):
                        output = output + str(k)
                k += 1
            j += 1
        result += int(output)
    print(result)

# p1()
p2()
