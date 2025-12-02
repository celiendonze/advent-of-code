from itertools import batched
from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "data/2025/day_2.txt"

with open(input_path) as file:
    line = file.read().strip()

total = 0
for s in line.split(","):
    a, b = s.split("-")
    a = int(a)
    b = int(b)
    for n in range(a, b + 1):
        m = str(n)
        if (
            m[: len(m) // 2] == m[len(m) // 2 :]
        ):  # detect repeat of 2 times the same number
            total += n

print("Part 1:", total)

total = 0
for s in line.split(","):
    a, b = s.split("-")
    a = int(a)
    b = int(b)
    for n in range(a, b + 1):
        m = str(n)
        # detect repeat of n times the same number
        for size in range(1, len(m) // 2 + 1):
            try:
                b = batched(m, size, strict=True)
                if len(set(b)) == 1:
                    total += n
                    break
            except ValueError:
                continue

print("Part 2:", total)
