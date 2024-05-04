
#! --- Importing input from the file ---
import os
def get_lines(file_path):
    with open(file_path, "r") as file: return file.readlines()
file_path = os.path.join(os.getcwd(), "2023", "Day_01", "input.txt")
lines = get_lines(file_path)


#! --- Part One ---
def sum_calibration_values(lines):
    total_sum = 0
    for line in lines:
        numbers = [int(char) for char in line if char.isdigit()]
        total_sum += numbers[0] * 10 + numbers[-1]

    return total_sum

print(sum_calibration_values(lines))
# Output: 54390


#! --- Part Two ---
mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
new_lines = []
for line in lines:
    new_line = []
    for i in range(len(line)):
        x = ""
        for id, val in enumerate(mappings, 1):
            if line[i:].startswith(val):
                x = "".join([str(id)])
                break
        if not x:
            new_line.append(line[i])
        else:
            new_line.append(x)
    new_lines.append(new_line)

print(sum_calibration_values(new_lines))
# Output: 54277