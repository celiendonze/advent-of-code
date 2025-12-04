from pathlib import Path

from tqdm import tqdm

day_11_input = Path("data/inputs/day_11/input.txt").read_text().strip().split(" ")
day_11_input = [int(x) for x in day_11_input]


def apply_rules(input_list: list[int]) -> list[int]:
    new_list = []
    for i in input_list:
        len_str_i = len(str(i))
        if i == 0:
            new_list.append(1)
        elif len_str_i % 2 == 0:
            # split in 2 parts
            left_part = int(str(i)[: len_str_i // 2])
            right_part = int(str(i)[len_str_i // 2 :])
            new_list.append(left_part)
            new_list.append(right_part)
        else:
            new_list.append(i * 2024)

    return new_list


final_list = day_11_input
for i in range(25):
    final_list = apply_rules(final_list)

print("Part 1:")
print(len(final_list))

# Part 2


def explore_recursively(input_list: list[int], depth: int) -> int:
    if depth == 0:
        return len(input_list)
    else:
        new_list = apply_rules(input_list)
        return sum(explore_recursively([l], depth - 1) for l in new_list)


final_list = day_11_input
total_len = explore_recursively(final_list, 40)

print("Part 2:")
print(total_len)
