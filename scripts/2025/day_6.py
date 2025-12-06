import re
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "data/2025/day_6.txt"

with open(input_path) as file:
    lines = file.readlines()


def remove_extra_spaces(s):
    return re.sub(r"\s+", " ", s).strip()


line_1 = remove_extra_spaces(lines[0]).split(" ")
line_2 = remove_extra_spaces(lines[1]).split(" ")
line_3 = remove_extra_spaces(lines[2]).split(" ")
line_4 = remove_extra_spaces(lines[3]).split(" ")
line_operators = remove_extra_spaces(lines[4]).split(" ")

total = 0
for l1, l2, l3, l4, op in zip(line_1, line_2, line_3, line_4, line_operators):
    if op == "+":
        result = int(l1) + int(l2) + int(l3) + int(l4)
    elif op == "*":
        result = int(l1) * int(l2) * int(l3) * int(l4)
    total += result

print("Part 1:", total)

total = 0
columns = list(zip(lines[0], lines[1], lines[2], lines[3], lines[4]))
numbers = []
operators = []
for col in columns:
    operator = col[4]
    col_number = "".join([c for c in col[:4] if c.strip().isdigit()])
    if col_number:
        col_number = int(col_number)
    if operator in ["+", "*"]:
        operators.append(operator)
        numbers.append([])
    if col_number:
        numbers[-1].append(col_number)

for nums, op in zip(numbers, operators):
    if op == "+":
        result = sum(nums)
    elif op == "*":
        result = 1
        for n in nums:
            result *= n
    total += result

print("Part 2:", total)
