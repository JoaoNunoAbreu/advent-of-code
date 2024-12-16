from utils.files import *


def calculate_representation(num):
    i = 0
    is_file = True
    res = []
    for digit in num:
        if is_file:
            for _ in range(int(digit)):
                res.append(str(i))
            is_file = False
            i += 1
        else:
            for _ in range(int(digit)):
                res.append(".")
            is_file = True

    return res


def file_compacting(representation):
    res = []
    last_elem = len(representation) - 1
    i = 0
    while i <= last_elem:
        if representation[i] == ".":
            while representation[last_elem] == '.':
                last_elem -= 1

            res.append(representation[last_elem])
            last_elem -= 1
        else:
            res.append(representation[i])
        i += 1

    return res


def checksum(num):
    return sum(int(digit) * i for i, digit in enumerate(num))


def part_1(num):
    representation = calculate_representation(num)
    compacted = file_compacting(representation)
    return checksum(compacted)


def part_2(num):
    pass


def main():
    data = read_file_lines()

    part1 = part_1(data[0])
    part2 = part_2(data[0])

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
