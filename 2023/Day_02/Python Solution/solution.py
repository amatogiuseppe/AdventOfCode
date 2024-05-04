
#! --- Importing input from the file ---
import os
def get_games(file_path):
    with open(file_path, "r") as file: return file.readlines()
file_path = os.path.join(os.getcwd(), "2023", "Day_02", "input.txt")
games = get_games(file_path)


#! --- Part One ---
def possible_games(games):
    thresholds = {"red": 12, "green": 13, "blue": 14}
    possibles = 0

    for game in games:
        game_info, sets = game.split(": ")
        groups = [subset.split() for subset in sets.replace(";", ",").split(", ")]
        if all(int(cube_nums) <= thresholds[cube_color] for cube_nums, cube_color in groups):
            possibles += int(game_info.split(" ")[1])

    return possibles

print(possible_games(games))
# Output: 2600


#! --- Part Two ---
def calculate_total_power(games):
    total_power = 0

    for game in games:
        counts = {"red": 0, "green": 0, "blue": 0}
        _, sets = game.split(": ")
        sets = sets.split("; ")

        for subset in sets:
            subset_counts = {color: int(count) for count, color in map(str.split, subset.split(", "))}
            counts = {color: max(count, subset_counts.get(color, 0)) for color, count in counts.items()}

        game_power = counts["red"] * counts["green"] * counts["blue"]
        total_power += game_power

    return total_power

print(calculate_total_power(games))
# Output: 86036
