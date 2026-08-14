# ----------------- Part1, day3 ----------------

import os

script_dir = os.path.dirname(__file__)

# ------------------- v1 ---------------------


def find_both_highest(number_list: list):
    highest = -1
    second_highest = -1
    for i, number in enumerate(number_list):

        if number > highest and i != len(number_list) - 1:
            highest = number
            second_highest = -1
        elif number > second_highest:
            second_highest = number
        elif i == len(number_list) - 1 and number > highest:
            highest = second_highest
            second_highest = number
            

    return highest, second_highest


with open(f"{script_dir}/input.txt", "r") as file:
    lines = file.readlines()

sum_of_joltages = 0
for line in lines:

    a, b = find_both_highest(list(map(int, list(str(line.strip())))))
    #print(f"{a}{b}")
    sum_of_joltages += int(f"{a}{b}")
print(sum_of_joltages)
