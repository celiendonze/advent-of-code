from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from shapely import Polygon
from tqdm import tqdm

input_path = Path(__file__).parent.parent.parent / "data/2025/day_9.txt"

lines = input_path.read_text().splitlines()

lines = [np.array(list(map(int, line.split(",")))) for line in lines]

max_area = 0
for line in lines:
    for other_line in lines:
        if line is other_line:
            continue
        v = abs(line - other_line)
        area = (v[0] + 1) * (v[1] + 1)
        if area > max_area:
            max_area = area
print("Part 1:", max_area)

polygon = Polygon(lines)

max_area = 0
for line in tqdm(lines):
    for other_line in lines:
        if line is other_line:
            continue
        rect = Polygon(
            [
                line,
                [line[0], other_line[1]],
                other_line,
                [other_line[0], line[1]],
            ]
        )
        if not rect.within(polygon):
            continue
        v = abs(line - other_line)
        area = (v[0] + 1) * (v[1] + 1)
        if area > max_area:
            max_area = area
print("Part 2:", max_area)
