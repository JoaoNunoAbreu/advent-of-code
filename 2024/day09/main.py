from utils.files import *


def calculate_representation(num):
    i = 0
    is_file = True
    res = []
    for digit in num:
        res.extend([str(i) if is_file else "."] * int(digit))
        if is_file:
            i += 1
        is_file = not is_file
    return res

def calculate_representation_arrays(num):
    i = 0
    is_file = True
    res = []
    for digit in num:
        part = [str(i) if is_file else "." for _ in range(int(digit))]
        if part:
            res.append(part)
        if is_file:
            i += 1
        is_file = not is_file
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
    return sum(int(digit) * i for i, digit in enumerate(num) if digit != '.')


def part_1(num):
    representation = calculate_representation(num)
    compacted = file_compacting(representation)
    return checksum(compacted)


def swap_files(representation, start_index, last_index):
    start = representation[start_index]
    last = representation[last_index]

    new_start = last + start[len(last):]
    new_last = start[:len(last)]

    representation[start_index] = new_start
    representation[last_index] = new_last

    return representation


def normalize(representation):
    normalized = []

    for sublist in representation:
        if '.' in sublist:
            non_dots = [x for x in sublist if x != '.']
            dots = ['.'] * sublist.count('.')

            if non_dots:
                normalized.append(non_dots)
            normalized.append(dots)
        else:
            normalized.append(sublist)

    return normalized


def part_2(num):
    representation = calculate_representation_arrays(num)

    original_representation = [i for i in representation]

    last_index = len(representation) - 1
    while last_index > 0:
        start_index = 0

        while representation[last_index][0] == ".":
            last_index -= 1

        while start_index < last_index and representation[start_index][0] != "." or len(representation[start_index]) < len(representation[last_index]):
            start_index += 1

        if start_index == last_index:
            last_index -= 1
        else:
            representation = swap_files(representation, start_index, last_index)
            representation = normalize(representation)

            if original_representation == representation:
                break

            original_representation = [i for i in representation]

    flat_representation = [item for sublist in representation for item in sublist]
    return checksum(flat_representation)


def main():
    data = read_file_lines()

    part1 = part_1(data[0])
    part2 = part_2(data[0])

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
