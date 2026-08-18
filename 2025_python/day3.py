# ----------------- Part1, day3 ----------------

import os

script_dir = os.path.dirname(__file__)

# ------------------- v1 ---------------------


# def find_both_highest(number_list: list):
#     highest = -1
#     second_highest = -1
#     for i, number in enumerate(number_list):

#         if number > highest and i != len(number_list) - 1:
#             highest = number
#             second_highest = -1
#         elif number > second_highest:
#             second_highest = number
#         elif i == len(number_list) - 1 and number > highest:
#             highest = second_highest
#             second_highest = number
            

#     return highest, second_highest


# with open(f"{script_dir}/input.txt", "r") as file:
#     lines = file.readlines()

# sum_of_joltages = 0
# for line in lines:

#     a, b = find_both_highest(list(map(int, list(str(line.strip())))))
#     #print(f"{a}{b}")
#     sum_of_joltages += int(f"{a}{b}")
# print(sum_of_joltages)

# ----------------- Part2, day3 ----------------


with open(f"{script_dir}/input.txt", "r") as file:
    lines = file.readlines()

def find_highest(_number_list: list, _start_index: int, _end_index: int):
    
    highest = -1
    highest_i = 0
    for number in range(_start_index, _end_index):
        if _number_list[number] > highest:
            highest = _number_list[number]
            highest_i = number
            
    return highest, highest_i


sum_of_all = 0
for line in lines:
    the_big_line = list(map(int, list(str(line.strip()))))
    start_index = 0
    jolts_to_find = 12
    result_number = []
    loop_counter = jolts_to_find
    end_index = len(the_big_line) - jolts_to_find + 1
    for i in range(loop_counter):
        highest, highest_index = find_highest(the_big_line, start_index, end_index)
        result_number.append(str(highest))
        jolts_to_find -= 1
        start_index = highest_index + 1
        end_index = len(the_big_line) - jolts_to_find + 1

    sum_of_all += int("".join(result_number))
print(sum_of_all)