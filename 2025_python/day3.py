# ----------------- Part1, day2 ----------------

import os

script_dir = os.path.dirname(__file__)

# ------------------- v1 ---------------------


def find_both_highest(number_list: list):
    highest = 0
    h_i = 0
    second_highest = 0
    s_i = 0
    for i, number in enumerate(number_list):

        # First 2 numbers in bank
        if highest == 0:
            highest = number
            h_i = i
            continue
        if second_highest == 0:
            second_highest = number
            s_i = i
            continue

        if number > highest:
            if i != len(number_list) - 1:
                second_highest = 0
                s_i = 0
            else:
                second_highest = highest
                s_i = h_i
            highest = number
            h_i = i

    return (highest, h_i), (second_highest, s_i)


with open(f"{script_dir}/testinput.txt", "r") as file:
    lines = file.readlines()

for line in lines:

    a, b = find_both_highest(list(map(int, list(str(line.strip())))))
    print(f"{a[0]}{b[0]}")
