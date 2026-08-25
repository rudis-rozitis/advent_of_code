# ----------------- Part1, day3 ----------------

import os

script_dir = os.path.dirname(__file__)
with open(f"{script_dir}/input.txt", "r") as file:
    lines = file.readlines()

# ----------------------- v1 ------------------------
# def check_adjacent_paper_rolls(_grid: list[list], _i: int, _j: int):
    
#     adjacent_paper_rolls = 0
    
#     if _i - 1 >= 0 and _j-1 >= 0 and grid[_i - 1][_j - 1] == "@":
#         adjacent_paper_rolls += 1
#     if _i - 1 >= 0 and grid[_i - 1][_j] == "@":
#         adjacent_paper_rolls += 1
#     if _i - 1 >= 0 and _j + 1 <= len(grid) - 1 and  grid[_i - 1][_j + 1] == "@":
#         adjacent_paper_rolls += 1
    
#     if _j-1 >= 0 and  grid[_i][_j - 1] == "@":
#         adjacent_paper_rolls += 1
#     if _j + 1 <= len(grid) - 1 and grid[_i][_j + 1] == "@":
#         adjacent_paper_rolls += 1

#     if _i + 1 <= len(grid) - 1 and _j-1 >= 0 and  grid[_i + 1][_j - 1] == "@":
#             adjacent_paper_rolls += 1
#     if _i + 1 <= len(grid) - 1 and grid[_i + 1][_j] == "@":
#         adjacent_paper_rolls += 1
#     if _i + 1 <= len(grid) - 1 and _j + 1 <= len(grid) - 1 and grid[_i + 1][_j + 1] == "@":
#         adjacent_paper_rolls += 1
    
#     return adjacent_paper_rolls

# ----------------------- v2 ------------------------

# def check_adjacent_paper_rolls(_grid: list[list], index_i: int, index_j: int):
    
#     adjacent_paper_rolls = 0
    
#     for _i in range(-1, 2):
#         for _j in range(-1, 2):
#             if index_i + _i >=0 and index_i + _i < len(grid) and \
#                index_j + _j >=0 and index_j + _j < len(grid[index_i + _i]) and \
#                not (_i == 0 and _j == 0) and grid[index_i + _i][index_j + _j] == "@":
#                 adjacent_paper_rolls += 1
#             if adjacent_paper_rolls >= 4:
#                 return adjacent_paper_rolls
#     return adjacent_paper_rolls

# grid = []
# for line in lines:
#     grid.append(list(line.strip()))
    

# available_forklifts = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == "@" and check_adjacent_paper_rolls(grid, i, j) < 4 :
#             #print(i, j)
#             available_forklifts += 1
# print(available_forklifts)


# ----------------------- Part2, day4 ------------------------

def check_adjacent_paper_rolls(_grid: list[list], index_i: int, index_j: int):
    
    adjacent_paper_rolls = 0
    
    for _i in range(-1, 2):
        for _j in range(-1, 2):
            if index_i + _i >=0 and index_i + _i < len(_grid) and \
               index_j + _j >=0 and index_j + _j < len(_grid[index_i + _i]) and \
               not (_i == 0 and _j == 0) and _grid[index_i + _i][index_j + _j] == "@":
                adjacent_paper_rolls += 1
            if adjacent_paper_rolls >= 4:
                return adjacent_paper_rolls
    return adjacent_paper_rolls

def copy_grid(_grid: list[list]):
    copied_grid = []
    for i in range(len(_grid)):
        copied_grid.append(_grid[i].copy())
    return copied_grid

grid = []

for line in lines:
    grid.append(list(line.strip()))

second_grid = copy_grid(grid)

available_forklifts = 0
while True:
    swapped = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@" and check_adjacent_paper_rolls(grid, i, j) < 4 :
                swapped = True
                second_grid[i][j]="."
                available_forklifts += 1

    grid = copy_grid(second_grid)
    if not swapped:
        break
    
print(available_forklifts)
