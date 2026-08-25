# ----------------- Part1, day5 ----------------

import os

script_dir = os.path.dirname(__file__)

# all_ranges = set()
# fresh_items = set()
# end_of_ranges = False
# with open(f"{script_dir}/input.txt", "r") as file:
#     for line in file.readlines():
#         if not end_of_ranges:
#             if line.strip() == "":
#                 end_of_ranges = True
#             else:
#                 start, end = line.strip().split("-")
#                 all_ranges.add((int(start), int(end)))
#         else:
#             for _range in all_ranges:
#                 if _range[0] <= int(line.strip()) <= _range[1]:
#                     fresh_items.add(int(line.strip()))
# print(len(fresh_items))

# ----------------- Part2, day5 ----------------


sorted_list_of_ranges = []
fresh_item_count = 0
with open(f"{script_dir}/input.txt", "r") as file:
    for line in file.readlines():
        if line.strip() == "":
            break
        else:
            start, end = line.strip().split("-")
            sorted_list_of_ranges.append(tuple([int(start), int(end)]))

sorted_list_of_ranges.sort()

current_range = sorted_list_of_ranges[0]
list_of_merged_ranges = []
for i in range(1, len(sorted_list_of_ranges)):
    if sorted_list_of_ranges[i][0] <= current_range[1]:
        if sorted_list_of_ranges[i][1] > current_range[1]:
            current_range = tuple([current_range[0], sorted_list_of_ranges[i][1]])

    elif sorted_list_of_ranges[i][0] > current_range[1]:
        list_of_merged_ranges.append(current_range)
        current_range = sorted_list_of_ranges[i]
list_of_merged_ranges.append(current_range)

for merged_range in list_of_merged_ranges:
    fresh_item_count += merged_range[1] - merged_range[0] + 1
print(fresh_item_count)
