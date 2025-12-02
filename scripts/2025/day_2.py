from itertools import batched
from pathlib import Path

from tqdm import tqdm

input_path = Path(__file__).parent.parent.parent / "data/2025/day_2.txt"

with open(input_path) as file:
    line = file.read().strip()

total = 0
for s in tqdm(line.split(",")):
    a, b = s.split("-")
    for n in range(int(a), int(b) + 1):
        m = str(n)
        if m[: len(m) // 2] == m[len(m) // 2 :]:
            total += n

print("Part 1:", total)

total = 0
for s in tqdm(line.split(",")):
    a, b = s.split("-")
    for n in range(int(a), int(b) + 1):
        m = str(n)
        for size in range(1, len(m) // 2 + 1):
            b = batched(m, size)
            if len(set(b)) == 1:
                total += n
                break

print("Part 2:", total)
