# ----------------- Part1, day2 ----------------

# ------------------- v1 ---------------------

# import os

# script_dir = os.path.dirname(__file__)

# with open(f"{script_dir}/input.txt", "r") as file:
#     ranges = file.readline().split(",")

# invalid_id_sum = 0
# for id_ranges in ranges:
#     start, end = map(int, id_ranges.split("-"))

#     for number in range(start, end+1):
#         string_number = str(number)
#         if len(string_number) % 2 != 0:
#             continue

#         half_index = len(string_number)//2
#         if string_number[:half_index] == string_number[half_index:]:
#             invalid_id_sum += number
#             print(f"invalid ID: {number}")

# print(invalid_id_sum)

# ------------------- v2 ---------------------

# import os

# script_dir = os.path.dirname(__file__)

# with open(f"{script_dir}/input.txt", "r") as file:
#     ranges = file.readline().split(",")

# invalid_id_sum = 0
# threshold = 0

# for id_ranges in ranges:

#     start, end = map(int, id_ranges.split("-"))

#     digits = 1
#     digit_number = start
#     while digit_number >= 10:
#         digit_number //= 10
#         digits += 1
#     threshold = 10**digits

#     for number in range(start, end + 1):
#         if number == threshold:
#             digits += 1
#             threshold *= 10

#         if digits % 2 == 1:
#             continue

#         divisor = 10 ** (digits // 2)
#         if number // divisor == number % divisor:
#             #print(number)
#             invalid_id_sum += number

# print(invalid_id_sum)


# ------------------- v3 ---------------------


# import os

# script_dir = os.path.dirname(__file__)

# with open(f"{script_dir}/input.txt", "r") as file:
#     ranges = file.readline().split(",")

# invalid_id_sum = 0

# for id_range in ranges:

#     start, end = map(int, id_range.split("-"))

#     digits = 1
#     digit_number = start
#     while digit_number >= 10:
#         digit_number //= 10
#         digits += 1

#     if digits % 2 == 1:
#         candidate_start = 10**digits
#         candidate_digits = digits + 1
#     else:
#         candidate_start = start
#         candidate_digits = digits

#     starting_number = candidate_start // 10 ** (candidate_digits // 2)

#     check_number = int(str(starting_number) * 2)
#     while check_number <= end:
#         if check_number >= start:
#             invalid_id_sum += check_number
#         starting_number += 1
#         check_number = int(str(starting_number) * 2)

# print(invalid_id_sum)


# ----------------- Part2, day2 ----------------


import os

script_dir = os.path.dirname(__file__)

def get_digit_amount(number: int):
    digits = 1
    digit_number = number
    while digit_number >= 10:
        digit_number //= 10
        digits += 1
    return digits

with open(f"{script_dir}/input.txt", "r") as file:
    ranges = file.readline().split(",")

invalid_ids = set()
invalid_id_sum = 0

for id_range in ranges:
    start, end = map(int, id_range.split("-"))
    
    start_digits = get_digit_amount(start)
    end_digits = get_digit_amount(end)
    
    for i in range(start_digits, end_digits + 1):
        
        half_digits = i//2
        for pattern_length in range(1, half_digits + 1):
            if i % pattern_length != 0:
                continue
            
            repetitions = i // pattern_length
            pattern_start = 10 ** (pattern_length - 1)
            pattern_end = 10 ** pattern_length
            
            for pattern in range(pattern_start, pattern_end):
                formed_id = int(str(pattern) * repetitions)
                if start <= formed_id <=end:
                    invalid_ids.add(formed_id)

for id in invalid_ids:
    invalid_id_sum += id
print(invalid_id_sum)