def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def sumPos(file_con, length):
    sum = [0] * length
    for value in file_con:
        value_list = list(value)
        i = 0
        while i < len(value_list):
            if value_list[i] != "\n":
                sum[i] += int(value_list[i])
            i += 1
    return sum


def calcGE(sum, file_con):
    gamma = ""
    epsilon = ""
    i = 0
    while i < len(sum):
        if sum[i] < len(file_con) / 2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
        i += 1
    return gamma, epsilon


# test_len = 5
test_len = 12
# file = open("example.txt")
file = open("input.txt")
file_content = file.readlines()

sum = sumPos(file_content, test_len)
# sum = sumPos(file_content,12)
gamma, epsilon = calcGE(sum, file_content)

gamma_result = binaryToDecimal(int(gamma))
epsilon_result = binaryToDecimal(int(epsilon))

print(gamma_result * epsilon_result)


def purgeLesser(file_con, pos, max):
    sum = sumPos(file_con, test_len)
    sum_of_intrest = 0
    if sum[pos] >= (len(file_con) / 2):
        sum_of_intrest = 1

    i = 0
    while i < len(file_con):
        value_list = list(file_con[i])
        if value_list[pos] != str(sum_of_intrest):
            file_con.pop(i)
        else:
            i += 1

    if pos < max - 1:
        purgeLesser(file_con, pos + 1, max)
    return file_con


def purgeHigher(file_con, pos, max):
    sum = sumPos(file_con, test_len)
    sum_of_intrest = 1
    if sum[pos] >= (len(file_con) / 2):
        sum_of_intrest = 0

    i = 0
    while i < len(file_con) and len(file_con) != 1:
        value_list = list(file_con[i])
        if value_list[pos] != str(sum_of_intrest):
            file_con.pop(i)
        else:
            i += 1

    if pos < max - 1:
        purgeHigher(file_con, pos + 1, max)
    return file_con


o2 = purgeLesser(file_content, 0, test_len)
file.close()

# file2 = open("example.txt")
file2 = open("input.txt")
file2_content = file2.readlines()
co2 = purgeHigher(file2_content, 0, test_len)

print(binaryToDecimal(int(o2[0])), binaryToDecimal(int(co2[0])))
print(binaryToDecimal(int(o2[0])) * binaryToDecimal(int(co2[0])))
