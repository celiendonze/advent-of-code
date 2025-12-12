from pathlib import Path

import numpy as np

input_path = Path(__file__).parent.parent.parent / "data/2025/day_12.txt"

lines = input_path.read_text().splitlines()

gifts = []
for line in lines[:30]:
    if "#" in line:
        gifts.append([1 if e == "#" else 0 for e in line.strip()])
gifts = np.array([np.array(gifts[i : i + 3]) for i in range(0, len(gifts), 3)])

total_1 = 0
for line in lines[30:]:
    space, n = line.split(":")
    x, y = map(int, space.split("x"))
    n = list(map(int, n.strip().split(" ")))
    total_size_needed = 0
    for i, gift in enumerate(gifts):
        needed = sum(gift.flatten())
        total_size_needed += needed * n[i]

    if x * y < total_size_needed:
        continue
    else:
        # print("Maybe Possible")
        total_1 += 1

print(total_1)
