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


# def check_row(row):
#     brackets = {
#             "(": ")",
#             "[": "]",
#             "{": "}",
#             "<": ">",
#             ")": "",
#             "}": "",
#             "]": "",
#             ">": ""
#         }
#     closed_bracket = [")", "]", "}", ">"]
#
#     row_list = list(row)
#     end = 1
#     while end > 0:
#         end = 0
#         i = 0
#         while i < len(row_list) - 1:
#             if brackets[row_list[i]] == row_list[i+1]:
#                 pop1 = row_list.pop(i+1)
#                 pop2 = row_list.pop(i)
#                 if pop1 != brackets[pop2]:
#                     print(pop1, pop2)
#                 end += 1
#             else:
#                 i += 1
#
#     i = 0
#     while i < len(row_list):
#         if row_list[i] in closed_bracket:
#             return row_list[i]
#         i += 1

def check_row(row):
    brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">",
            ")": "",
            "}": "",
            "]": "",
            ">": ""
        }
    open_bracket = ["(", "{", "[", "<"]
    closed_bracket = [")", "]", "}", ">"]

    i = 0
    row_list = list(row)
    match_list = []
    while i < len(row_list):
        if row_list[i] in open_bracket:
            match_list.append(row_list[i])
        else:
            if brackets[match_list[len(match_list) - 1]] != row_list[i]:
                return row_list[i]
            else:
                match_list.pop(len(match_list) - 1)
        i += 1


def calc_points(symbol_list):
    result = 0
    points = {")": 3,
            "}": 57,
            "]": 1197,
            ">": 25137}
    for symbol in symbol_list:
        result += points[symbol]
    return result


def p1():
    lines = read_lines("day10/input.txt")
    error_symbols = []
    for row in lines:
        value = check_row(row)
        if value:
            error_symbols.append(value)
    print(len(error_symbols))
    print(calc_points(error_symbols))


p1()

