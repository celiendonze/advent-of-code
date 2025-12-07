from pathlib import Path

from tqdm import tqdm

input_path = Path(__file__).parent.parent.parent / "data/2025/day_7.txt"

with open(input_path) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

beams = set()
total = 0
for idxline, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == "S":
            beams.add(i)
        if char == "^" and i in beams:
            beams.add(i - 1)
            beams.add(i + 1)
            beams.remove(i)
            total += 1
print("Part 1:", total)

beams = set()
total = 0
paths = None
for idxline, line in enumerate(lines):
    if paths is None:
        paths = [0] * len(line)
    for i, char in enumerate(line):
        if char == "S":
            beams.add(i)
            paths[i] += 1
        if char == "^" and i in beams:
            beams.add(i - 1)
            paths[i - 1] += paths[i]
            beams.add(i + 1)
            paths[i + 1] += paths[i]
            beams.remove(i)
            paths[i] = 0

print("Part 2:", sum(paths))
