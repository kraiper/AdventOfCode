import queue
from threading import Thread

my_queue = queue.Queue()


def calc_fish(days, fish_list):
    i = 0
    while i < days:
        print(i)
        y = 0
        loop_end = len(fish_list)
        while y < loop_end:
            fish_list[y] -= 1
            if fish_list[y] < 0:
                fish_list[y] = 6
                fish_list.append(8)
            y += 1
        i += 1
    return len(fish_list)


class Fish():
    def __init__(self, cycle, day):
        self.cycle = cycle
        self.day = day


def calc_fish_mem_save(days, f_list):
    num_of_fishes = len(f_list)
    fish_list = []
    for fish in f_list:
        fish_list.append(Fish(fish, 0))

    while len(fish_list) > 0:
        # print(num_of_fishes)
        fish = fish_list.pop()
        while fish.day < days:
            fish.cycle -= 1
            fish.day += 1
            if fish.cycle < 0:
                fish.cycle = 6
                fish_list.append(Fish(8, fish.day))
                num_of_fishes += 1
    # return num_of_fishes
    my_queue.put(num_of_fishes)


file = open("day6/input.txt")
file_content = file.readlines()
fish_list_str = file_content[0].split(",")
i = 0
fish_list_int = []

while i < len(fish_list_str):
    fish_list_int.append(int(fish_list_str[i]))
    i += 1

thread_list = []

fish_dict = {}
i = 0
while i < 300:
    fish_dict[i] = 0
    i += 1


for fish in fish_list_int:
    fish_dict[fish] += 1

i = 0
fish_sum = len(fish_list_int)
while i < 256:
    fish_dict[i + 7] += fish_dict[i]
    fish_dict[i + 9] += fish_dict[i]
    fish_sum += fish_dict[i]
    i += 1

# print(fish_dict)
print(fish_sum)
