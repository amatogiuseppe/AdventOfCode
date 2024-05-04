
#! --- Importing input from the file ---
import os
def get_almanac(file_path):
    with open(file_path, "r") as file: return file.readlines()
file_path = os.path.join(os.getcwd(), "2023", "Day_05", "input.txt")
almanac = get_almanac(file_path)


#! --- Part One ---
def find_lowest_location(almanac):
    seeds = [int(seed) for seed in almanac[0].split()[1:]]
    pass

print(find_lowest_location(almanac))
# Output: