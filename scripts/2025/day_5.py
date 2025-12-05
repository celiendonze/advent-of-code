from pathlib import Path

input_path = Path(__file__).parent.parent.parent / "data/2025/day_5.txt"

with open(input_path) as file:
    lines = file.readlines()

ranges = []
ingredients = []
passed_empty_line = False
for line in lines:
    if line.strip() == "":
        passed_empty_line = True
        continue
    if passed_empty_line:
        ingredients.append(int(line.strip()))
    else:
        a, b = line.strip().split("-")
        ranges.append((int(a), int(b)))


def is_valid(ingredient: int) -> bool:
    """Check if an ingredient is valid for any of the ranges.

    Args:
        ingredient (int): The ingredient to check.
    Returns:
        bool: True if the ingredient is valid, False otherwise.
    """
    for a, b in ranges:
        if a <= ingredient <= b:
            return True
    return False


total = 0
for ingredient in ingredients:
    if is_valid(ingredient):
        total += 1

print("Part 1:", total)


def find_all_overlapping_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Find all overlapping ranges and merge them.

    Args:
        ranges (list[tuple[int, int]]): The list of ranges to check.
    Returns:
        list[tuple[int, int]]: The list of merged ranges.
    """
    merged_ranges = []
    for a, b in sorted(ranges):
        if not merged_ranges or merged_ranges[-1][1] < a:
            merged_ranges.append((a, b))
        else:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], b))
    return merged_ranges


total = 0

new_ranges = find_all_overlapping_ranges(ranges)

for a, b in new_ranges:
    total += b - a + 1

print("Part 2:", total)
