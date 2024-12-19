from collections import defaultdict

from utils.files import *


def apply_rules(stone):
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        first, second = stone[:len(stone) // 2].lstrip("0") or "0", stone[len(stone) // 2:].lstrip("0") or "0"
        return [first, second]

    return [str(int(stone) * 2024)]

def part_1(data):
    data = data.split()
    for _ in range(25):
        res = []
        for stone in data:
            new_value = apply_rules(stone)
            res.extend(new_value)
        data = res
    return len(data)


def part_2(data):
    data = data.split()
    cache = {}
    occur = {i: 1 for i in data}
    for _ in range(75):
        res = defaultdict(int)
        for stone in occur:
            if stone not in cache:
                cache[stone] = apply_rules(stone)
            for new_stone in cache[stone]:
                res[new_stone] += occur[stone]

        occur = res
    return sum(occur.values())


def main():
    data = read_file_lines()

    part1 = part_1(data[0])
    part2 = part_2(data[0])

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
