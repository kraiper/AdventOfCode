file = open("input.txt")
file_content = file.readlines()

#p1
i = 0
count = 0
prev_value = -1
for value in file_content:
    value = int(value)
    if prev_value != -1 and value > prev_value:
        count += 1
    prev_value = value
    i += 1

print(count)

#p2
i = 0
count = 0
prev_value = -1
value_list = []
while i < len(file_content) - 2:
    value_list.append(int(file_content[i]) + int(file_content[i+1]) + int(file_content[i+2]))
    i += 1

for value in value_list:
    if prev_value != -1 and value > prev_value:
        count += 1
    prev_value = value
    i += 1

print(count)
