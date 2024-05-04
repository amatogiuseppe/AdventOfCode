
#! --- Importing input from the file ---
import os
def get_scratchcards(file_path):
    with open(file_path, "r") as file: return file.readlines()
file_path = os.path.join(os.getcwd(), "2023", "Day_04", "input.txt")
scratchcards = [scratchcard.rstrip("\n") for scratchcard in get_scratchcards(file_path)]


#! --- Part One ---
def calculate_total_points(cards):
    total_points = 0
    for card in cards:
        parts = [value for value in card.split(" ") if value != ""]
        separator_index = parts.index("|")

        winning_numbers = parts[2:separator_index]
        numbers_owned = parts[separator_index + 1:]

        score = 0
        for number in numbers_owned:
            if number in winning_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total_points += score
    return total_points

print(calculate_total_points(scratchcards))
# Output: 23941


#! --- Part Two ---
def calculate_total_scratchcards(cards):
    total_cards = 0
    copies = {i: 1 for i in range(len(cards) + 1)}

    for i, card in enumerate(cards):
        parts = [value for value in card.split(" ") if value != ""]
        separator_index = parts.index("|")

        winning_numbers = parts[2:separator_index]
        numbers_owned = parts[separator_index + 1:]

        matches = sum(1 for number in numbers_owned if number in winning_numbers)

        for j in range(i + 1, i + matches + 1):
            copies[j] += copies[i]

        total_cards += copies[i]

    return total_cards


print(calculate_total_scratchcards(scratchcards))
# Output: 5571760