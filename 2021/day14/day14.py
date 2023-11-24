from collections import Counter


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


def p1(file):
    lines = read_lines(file)
    template = lines.pop(0)
    template_list = list(template)
    pair_dict = {}
    for line in lines:
        pair, insert = line.split(" -> ")
        pair_dict[pair] = insert

    l = len(template_list)
    expected_length = [l]
    iteration = 0

    for key in pair_dict.keys():
        test = key + " -> " + pair_dict[key]
        assert test in lines

    while iteration < 11:
        l += l - 1
        expected_length.append(l)
        iteration += 1

    iteration = 0
    result_list = [template_list]
    while iteration < 10:

        result_list.append([])
        i = 0
        while i < len(result_list[iteration]) - 1:
            result_list[iteration + 1].append(result_list[iteration][i])
            result_list[iteration + 1].append(pair_dict[result_list[iteration][i] + result_list[iteration][i+1]])
            i += 1
        result_list[iteration + 1].append(result_list[iteration][i])

        assert len(result_list[iteration + 1]) == expected_length[iteration+1]

        iteration += 1

    count = Counter(result_list[iteration])

    highest = 0
    lowest = 9999999999999999999999999999
    for value in count.values():
        if highest < value:
            highest = value
        if lowest > value:
            lowest = value
    print(highest, "-", lowest, "=", highest - lowest)
    return highest - lowest


def p2(file):
    lines = read_lines(file)
    template = lines.pop(0)
    template_list = list(template)
    pair_dict = {}
    deep_dict = {}
    for line in lines:
        pair, insert = line.split(" -> ")
        p_l = list(pair)
        pair_dict[pair] = insert
        deep_dict[pair] = p_l[0] + insert + p_l[1]


    start_kombos = []
    i = 0
    while i < len(template_list) - 1:
        start_kombos.append(template_list[i] + template_list[i + 1])
        i += 1
    #
    # print(template_list)
    # print(start_kombos)
    #
    # print(deep_dict)
    # i = 0
    # parts = []
    # for combo in start_kombos:
    #     p = [combo]
    #     while i < 40:
    #
    #         i += 1
    #     parts.append(p)


    l = len(template_list)
    expected_length = [l]
    iteration = 0

    for key in pair_dict.keys():
        test = key + " -> " + pair_dict[key]
        assert test in lines

    while iteration < 41:
        l += l - 1
        expected_length.append(l)
        iteration += 1

    z = 0
    end = []
    while z < len(start_kombos):
        result_list = [start_kombos[z]]

        iteration = 0
        while iteration < 2:

            result_list.append([])
            i = 0
            while i < len(result_list[iteration]) - 1:
                result_list[iteration + 1].append(result_list[iteration][i])
                result_list[iteration + 1].append(pair_dict[result_list[iteration][i] + result_list[iteration][i+1]])
                i += 1
            result_list[iteration + 1].append(result_list[iteration][i])

            # assert len(result_list[iteration + 1]) == expected_length[iteration+1]

            iteration += 1
            print(iteration)
            end.append(result_list)
        z += 1

    result_list = []
    i = 0
    while i < len(end):
        end[i].pop(0)
        # print(end[i])
        if i != len(end) - 1:
            end[i][0].pop(len(end[i][0]) - 1)
        # print(listToString(end[i][0]))
        result_list.append(listToString(end[i][0]))
        i += 1

    # print(template_list)
    # print((result_list))
    # print(listToString(result_list))

    count = Counter(list(listToString(result_list)))

    highest = 0
    lowest = 9999999999999999999999999999
    for value in count.values():
        if highest < value:
            highest = value
        if lowest > value:
            lowest = value
    print(highest, "-", lowest, "=", highest - lowest)
    return highest - lowest
    # return 0


# result = p1("day14/test.txt")
# assert result == 1588
#
# print(p1("day14/input.txt"))



result = p2("day14/test.txt")
# assert result == 2188189693529
assert result == 1588

# print(p2("day14/input.txt"))



