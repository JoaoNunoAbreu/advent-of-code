import re
from utils.files import read_file


def clean_regex(match):
    return match.replace("mul(", "").replace(")", "").split(",")


def remove_muls(data):
    indexes_to_remove = []
    flag = False
    for i, j in enumerate(data):
        if j == "don't()":
            flag = True
        if j == "do()":
            indexes_to_remove.append(i)
            flag = False
        if flag:
            indexes_to_remove.append(i)

    return indexes_to_remove


def part_1(data):
    res = 0
    regex = "mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(regex, data)
    for match in matches:
        match = clean_regex(match)
        res += int(match[0]) * int(match[1])
    return res


def part_2(data):
    res = 0
    regex = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    matches = re.findall(regex, data)
    print(matches)
    indexes = remove_muls(matches)
    matches = [j for i, j in enumerate(matches) if i not in indexes]
    for match in matches:
        match = clean_regex(match)
        res += int(match[0]) * int(match[1])
    return res


def main():
    data = read_file()
    part1 = part_1(data)
    part2 = part_2(data)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
