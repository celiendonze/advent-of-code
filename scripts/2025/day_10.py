import re
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np
from tqdm import tqdm

input_path = Path(__file__).parent.parent.parent / "data/2025/day_10.txt"

lines = input_path.read_text().splitlines()

# [.#..] any combination of dots and
lights_pattern = re.compile(r"\[([.#]+)\]")
# any number of numbers in parentheses, comma separated
buttons_pattern = re.compile(r"\(([\d, ]+)\)")
# numbers comma separated, in {} braces
joltage_pattern = re.compile(r"\{([\d, ]+)\}")

total_1 = 0
total_2 = 0
for line in tqdm(lines):
    lights_match = lights_pattern.search(line)
    buttons_match = buttons_pattern.findall(line)
    joltage_match = joltage_pattern.search(line)

    lights = list(lights_match.group(1)) if lights_match else []
    buttons = (
        [list(map(int, btn.split(","))) for btn in buttons_match]
        if buttons_match
        else []
    )
    joltage = list(map(int, joltage_match.group(1).split(","))) if joltage_match else []

    # print("Line:", line)
    # print("Lights:", lights)
    # print("Buttons:", buttons)
    # print("Joltage:", joltage)

    lights = np.array([1 if c == "#" else 0 for c in lights])
    switches = []
    # print("Lights array:", lights)
    for button in buttons:
        s = np.zeros(len(lights), dtype=int)
        for v in button:
            s[v] += 1
        switches.append(s)

    found = False
    for i in range(1, 100):
        for combo in combinations_with_replacement(range(len(switches)), i):
            state = lights.copy()
            for idx in combo:
                state += switches[idx]
            state = state % 2
            if all(state == 0):
                total_1 += i
                # buttons_to_use = [buttons[idx] for idx in combo]
                # print("Found solution with", i, "buttons:", buttons_to_use)
                found = True
                break
        if found:
            break
    # solve a*b1 + a*b2 + ... = joltage
    # print(switches)
    # # array([1, 0, 1, 1, 1]), array([1, 1, 0, 1, 1]), array([1, 0, 0, 1, 1])]
    # print(joltage)  # [220, 13, 8, 220, 220]

    coeffs, residuals, rank, s = np.linalg.lstsq(
        np.array(switches).T, np.array(joltage), rcond=None
    )
    total_2 += sum(coeffs)

print("Part 1:", total_1)
print("Part 2:", total_2)
