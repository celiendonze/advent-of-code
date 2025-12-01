from pathlib import Path

HERE = Path(__file__).parent
DATA_DIR = HERE.parent.parent / "data"
INPUTS_DIR = DATA_DIR / "2024"

if __name__ == "__main__":
    with open(INPUTS_DIR / "25.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    # remove empty lines
    lines = [line for line in lines if line]
    keys_or_lock = [lines[i : i + 7] for i in range(0, len(lines), 7)]
    print(keys_or_lock)
    keys = []
    locks = []
    for item in keys_or_lock:
        if item[0] == "#####":
            locks.append(item)
        elif item[-1] == "#####":
            keys.append(item)
    for key in keys:
        # remove last line
        key_body = key[:-1]

    for lock in locks:
        # remove first line
        lock_body = lock[1:]
