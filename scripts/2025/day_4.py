from pathlib import Path

import numpy as np
from tqdm import tqdm

input_path = Path(__file__).parent.parent.parent / "data/2025/day_4.txt"

with open(input_path) as file:
    lines = file.readlines()

map_data = [list(line.strip()) for line in lines]
map_array = np.array(map_data)


def can_be_accessed(map: np.ndarray, x: int, y: int) -> bool:
    """Check if a cell can be accessed, meaning it has less than 4 "@" in the 8 slots around.

    Args:
        map (np.ndarray): 2d array representing the map
        x (int): x-coordinate of the cell
        y (int): y-coordinate of the cell

    Returns:
        bool: True if the cell can be accessed, False otherwise
    """
    if map[y, x] != "@":
        return False
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= y + j < map.shape[0] and 0 <= x + i < map.shape[1]:
                if map[y + j, x + i] == "@":
                    count += 1
    return count < 4


total = 0
for x, y in tqdm(
    [(x, y) for x in range(map_array.shape[1]) for y in range(map_array.shape[0])]
):
    if can_be_accessed(map_array, x, y):
        total += 1

print("Part 1:", total)


total = 0
while True:
    inner_total = 0
    new_map_array = map_array.copy()
    for x, y in tqdm(
        [(x, y) for x in range(map_array.shape[1]) for y in range(map_array.shape[0])]
    ):
        if can_be_accessed(map_array, x, y):
            new_map_array[y, x] = "."
            inner_total += 1

    total += inner_total
    if inner_total == 0:
        break
    map_array = new_map_array

print("Part 2:", total)
