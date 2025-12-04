import re
from pathlib import Path

from tqdm import tqdm

input_path = Path(__file__).parent.parent.parent / "data/2025/day_3.txt"

with open(input_path) as file:
    lines = file.readlines()

patterns = [
    re.compile(rf".*({i}).*({j}).*") for i in range(9, 0, -1) for j in range(9, 0, -1)
]

total = 0
for line in tqdm(lines):
    for pattern in patterns:
        m = pattern.match(line)
        if m:
            number = int(f"{m.group(1)}{m.group(2)}")
            total += number
            break

print("Part 1:", total)


total = 0
for line in tqdm(lines):
    # print(line)
    n = ""
    s = 9
    while len(n) < 12:
        p = line.find(str(s))
        if p != -1 and (len(line) - p) >= (13 - len(n)):
            n += str(s)
            s = 9
            line = line[p + 1 :]
        else:
            s -= 1
        if s < 0:
            break
    total += int(n)

print("Part 2:", total)
