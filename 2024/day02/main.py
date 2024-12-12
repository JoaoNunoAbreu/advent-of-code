from utils.files import read_file_lines


def split_lines(data):
    return data.splitLines()


def process_data(data):
    return [[int(x) for x in line.split(' ')] for line in data]


def check_increasing_or_decreasing(data):
    return data == sorted(data) or data == sorted(data, reverse=True)


def check_adjacent_difference(data):
    return all(1 <= abs(data[i] - data[i + 1]) <= 3 for i in range(len(data) - 1))


def part_1(data):
    count = 0
    for line in data:
        if check_increasing_or_decreasing(line) and check_adjacent_difference(line):
            count += 1
    return count


def part_2(data):
    count = 0
    for line in data:
        if check_increasing_or_decreasing(line) and check_adjacent_difference(line):
            count += 1
        else:
            for i in range(len(line)):
                segment = line[:i] + line[i + 1:]
                if check_increasing_or_decreasing(segment) and check_adjacent_difference(segment):
                    count += 1
                    break
    return count


def main():
    data = read_file_lines()
    processed_data = process_data(data)
    part1 = part_1(processed_data)
    part2 = part_2(processed_data)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
