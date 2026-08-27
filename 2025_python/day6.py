# ----------------- Part1, day6 ----------------

import os

script_dir = os.path.dirname(__file__)

# --------------- v1 ---------------------

# rows: list = []
# with open(f"{script_dir}/input.txt", "r") as file:
#     for line in file.readlines():
#         rows.append(line.split())

# overall_sum: int = 0
# for columns in range(len(rows[0])):
#     operation = rows[-1][columns]
#     if operation == "+":
#         sub_result = 0
#     else:
#         sub_result = 1

#     if operation == "+":
#         for i in range(len(rows) - 1):
#             sub_result += int(rows[i][columns])
#     else:
#         for i in range(len(rows) - 1):
#             sub_result *= int(rows[i][columns])
#     overall_sum += sub_result

# print(overall_sum)

# --------------- v2 ---------------------

# rows: list = []
# with open(f"{script_dir}/input.txt", "r") as file:
#     for line in file:
#         rows.append(line.split())

# overall_sum: int = 0
# for column in zip(*rows):
#     operation = column[-1]
#     if operation == "+":
#         sub_result = 0
#         for number in column[:-1]:
#             sub_result += int(number)
#     else:
#         sub_result = 1
#         for number in column[:-1]:
#             sub_result *= int(number)

#     overall_sum += sub_result
# print(overall_sum)


# ----------------- Part2, day6 ----------------


rows: list = []
with open(f"{script_dir}/input.txt", "r") as file:

    for line in file:
        rows.append(line)

# --------------- v1 ---------------------

# operator_line = rows[-1]
# highest_digits_in_column = []

# space_count = 0
# for i in range(1, len(operator_line)):
#     if operator_line[i] != " ":
#         highest_digits_in_column.append(space_count)
#         space_count = 0
#     elif i == len(operator_line) - 1:
#         highest_digits_in_column.append(space_count + 2)
#     else:
#         space_count += 1

# split_rows = []
# for row in rows:
#     index_position = 0
#     single_row = []
#     for digit in highest_digits_in_column:
#         single_row.append(row[index_position:index_position + digit])
#         index_position += digit + 1
#     split_rows.append(single_row)
# index = 0

# overall_sum = 0
# for column in zip(*split_rows):
#     operation = column[-1].strip()
#     if operation == "+":
#         sub_result = 0
#         for i in range(highest_digits_in_column[index], 0, -1):
#             crafted_number = ""
#             for number in column[:-1]:
#                 if len(number) >= i:
#                     crafted_number += number[i-1]
#             sub_result += int(crafted_number)
#     else:
#         sub_result = 1
#         for i in range(highest_digits_in_column[index], 0, -1):
#             crafted_number = ""
#             for number in column[:-1]:
#                 if len(number) >= i:
#                     crafted_number += number[i-1]
#             sub_result *= int(crafted_number)
#     overall_sum += sub_result
#     index += 1
# print(overall_sum)


# --------------- v2 ---------------------

# overall_sum = 0
# column_numbers = zip(*rows)
# for number in column_numbers:
#     crafted_number = ""
#     for i in range(len(rows)):
#         if number[i] != " " and i != len(rows) - 1:
#             crafted_number += number[i]
#         if i == len(rows) - 1 and number[i] != " ":
#             operation = number[i]
#             if operation == "+":
#                 sub_result = 0
#             else:
#                 sub_result = 1
#     if crafted_number == "":
#         overall_sum += sub_result
#         continue
#     if operation == "+":
#         sub_result += int(crafted_number)
#     else:
#         sub_result *= int(crafted_number)

# overall_sum += sub_result
# print(overall_sum)


# --------------- v3 ---------------------

overall_sum = 0
column_numbers = zip(*rows)
for number in column_numbers:
    crafted_number = "".join(digit for digit in number[:-1] if digit != " ")

    if number[-1] != " ":
        operation = number[-1]
        if operation == "+":
            sub_result = 0
        else:
            sub_result = 1
    if crafted_number == "":
        overall_sum += sub_result
        continue
    if operation == "+":
        sub_result += int(crafted_number)
    else:
        sub_result *= int(crafted_number)

overall_sum += sub_result
print(overall_sum)
