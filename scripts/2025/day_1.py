from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "data/2025/day_1.txt"

with open(input_path) as file:
    lines = [line.strip() for line in file.readlines()]

clock = list(range(100))
current = 50
password = 0
for line in lines:
    if line[0] == "R":
        current += int(line[1:])
    else:
        current -= int(line[1:])
    current %= 100
    if current == 0:
        password += 1

print(f"Part 1 Password: {password}")

clock = list(range(100))
current = 50
password = 0  # count number of times we pass 0
for line in lines:
    direction = line[0]
    rotation = int(line[1:])  # Rotation can be higher than 100 (one full turn)
    number_of_full_turns, reminder = divmod(rotation, 100)
    password += number_of_full_turns
    for _ in range(reminder):
        if direction == "R":
            current += 1
        else:
            current -= 1
        current %= 100
        if current == 0:
            password += 1

print(f"Part 2 Password: {password}")
