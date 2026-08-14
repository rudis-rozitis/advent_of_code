
# ----------------- Part1, day1 ----------------
import os

script_dir = os.path.dirname(__file__) 

# with open(f"{script_dir}/day1input.txt", "r") as file:
#     lines = file.readlines()

# start_number = 50
# password = 0
# for line in lines: 
    
#     if line.startswith("R"):
#         start_number += int(line[1:])
#     else:
#         start_number -= int(line[1:])
#     start_number = start_number % 100
#     if start_number == 0:
#         password += 1

# print(password)


# ----------------- Part2, day1 ----------------

with open(f"{script_dir}/day1input.txt", "r") as file:
    lines = file.readlines()

start_number = 50
password = 0

for line in lines: 

    if line.startswith("R"):
        end_number = start_number + int(line[1:])
    else:
        end_number = start_number - int(line[1:])
    
    # --------------- v2 ----------------
    # if end_number < start_number:   
    #     numbers = range(end_number, start_number)
    # else: 
    #     numbers = range(start_number + 1, end_number+1)
    # clicks = 0
    # for i in numbers:
    #     if i % 100 == 0:
    #         clicks += 1
            
    # --------------- v1 -----------------
    # clicks = abs(end_number) // 100
    # if end_number > start_number and end_number >= 100:
    #     password += clicks
    # elif end_number < start_number and end_number < 0 and start_number != 0:
    #     number = clicks + 1 if clicks else 1
    #     password += number
    # elif end_number < start_number and end_number < -100 and start_number == 0:
    #     number = clicks if clicks else 1
    #     password += number
        
    # if end_number == 0:
    #     password += 1

    start_number = end_number % 100

print(password)

