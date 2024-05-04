
#! --- Importing input from the file ---
import os
def get_engine_schematic(file_path):
    with open(file_path, "r") as file: return file.readlines()
file_path = os.path.join(os.getcwd(), "2023", "Day_03", "input.txt")
engine_schematic = [line.rstrip("\n") for line in get_engine_schematic(file_path)]


#! --- Utility Functions ---
def get_adjacent_coordinates(x, y, width, height):
    return [(new_x, new_y) for dx in range(-1, 2) for dy in range(-1, 2)
            if not (dx == 0 and dy == 0)
            for new_x in range(x + dx, x + dx + 1)
            for new_y in range(y + dy, y + dy + 1)
            if 0 <= new_x < width and 0 <= new_y < height]


#! --- Part One ---
def calculate_part_numbers(grid):
    grid_width, grid_height = len(grid[0]), len(grid)
    total_sum = 0

    for y in range(grid_height):
        x = 0
        while x < grid_width:
            if not grid[y][x].isdigit():
                x += 1
                continue

            part_number = ""
            adjacent_coords = []

            for i in range(x, grid_width):
                if not grid[y][i].isdigit():
                    break

                part_number += grid[y][i]
                adjacent_coords.extend(get_adjacent_coordinates(i, y, grid_width, grid_height))

            if any(grid[ny][nx] != "." and not grid[ny][nx].isdigit() for nx, ny in adjacent_coords):
                total_sum += int(part_number)

            x += len(part_number)

    return total_sum

print(calculate_part_numbers(engine_schematic))
# Output: 525911


#! --- Part Two ---
def calculate_total_gear_ratio(grid):
    grid_width, grid_height = len(grid[0]), len(grid)
    gear_dict = {}
    total_gear_ratio = 0

    for y in range(grid_height):
        x = 0
        while x < grid_width:
            if not grid[y][x].isdigit():
                x += 1
                continue

            adjacent_checks = get_adjacent_coordinates(x, y, grid_width, grid_height)
            part_number = grid[y][x]

            for i in range(x + 1, grid_width):
                if not grid[y][i].isdigit():
                    break

                part_number += grid[y][i]
                adjacent_checks.extend(get_adjacent_coordinates(i, y, grid_width, grid_height))
                x += 1

            for nx, ny in adjacent_checks:
                if grid[ny][nx] == "*":
                    gear_dict.setdefault((nx, ny), []).append(int(part_number))
                    break

            x += 1

    for nums in gear_dict.values():
        if len(nums) > 1:
            total_gear_ratio += nums[0] * nums[1]

    return total_gear_ratio

print(calculate_total_gear_ratio(engine_schematic))
# Output: 75805607
