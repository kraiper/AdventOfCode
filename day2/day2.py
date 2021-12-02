file = open("input.txt")
file_content = file.readlines()

#p1
depth = 0
pos = 0
for value in file_content:
    command, value = value.split(" ")
    value = int(value)
    if command == "forward":
        pos += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value

print(depth*pos)

#p2
depth = 0
pos = 0
aim = 0
for value in file_content:
    command, value = value.split(" ")
    value = int(value)
    if command == "forward":
        pos += value
        depth += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(depth*pos)