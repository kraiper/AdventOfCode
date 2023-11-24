def p1():
    file = open("day7/input.txt")
    file_content = file.readlines()

    file_content_list = file_content[0].split(",")
    file_content_int = []
    i = 0
    while i < len(file_content_list):
        file_content_int.append(int(file_content_list[i]))
        i += 1


    highest_number = 0

    for number in file_content_int:
        if number > highest_number:
            highest_number = number

    fuel_bucket = [0] * (highest_number+1)
    for number in file_content_int:
        i = 0
        while i < len(fuel_bucket):
            fuel_bucket[i] += (abs(i - number))
            i += 1

    lowest_index = 0

    i = 0
    while i < len(fuel_bucket):
        if fuel_bucket[i] < fuel_bucket[lowest_index]:
            lowest_index = i
        i += 1

    print(lowest_index, fuel_bucket[lowest_index])


def p2():
    file = open("day7/input.txt")
    file_content = file.readlines()

    file_content_list = file_content[0].split(",")
    file_content_int = []
    i = 0
    while i < len(file_content_list):
        file_content_int.append(int(file_content_list[i]))
        i += 1

    highest_number = 0

    for number in file_content_int:
        if number > highest_number:
            highest_number = number

    fuel_bucket = [0] * (highest_number+1)
    for number in file_content_int:
        i = 0
        while i < len(fuel_bucket):
            steps = (abs(i - number))
            fuel_bucket[i] += ((1+steps)/2) * steps
            i += 1

    lowest_index = 0

    i = 0
    while i < len(fuel_bucket):
        if fuel_bucket[i] < fuel_bucket[lowest_index]:
            lowest_index = i
        i += 1
    print(lowest_index, fuel_bucket[lowest_index])


# p1()
p2()