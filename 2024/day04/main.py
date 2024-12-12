from utils.files import read_file_lines


def build_matrix(data):
    return [[char for char in line] for line in data]


def print_matrix(matrix):
    for i, line in enumerate(matrix):
        print(i, "|", ' '.join(line))


def extract_coordinates(data, char):
    return [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == char]


def xmas_search(data, x, y):
    count = 0

    if y >= 3 and data[x][y - 1] == "M" and data[x][y - 2] == "A" and data[x][y - 3] == "S":
        count += 1

    if y <= len(data[0]) - 4 and data[x][y + 1] == "M" and data[x][y + 2] == "A" and data[x][y + 3] == "S":
        count += 1

    if x >= 3 and data[x - 1][y] == "M" and data[x - 2][y] == "A" and data[x - 3][y] == "S":
        count += 1

    if x <= len(data) - 4 and data[x + 1][y] == "M" and data[x + 2][y] == "A" and data[x + 3][y] == "S":
        count += 1

    if x >= 3 and y >= 3 and data[x - 1][y - 1] == "M" and data[x - 2][y - 2] == "A" and data[x - 3][y - 3] == "S":
        count += 1

    if x <= len(data) - 4 and y >= 3 and data[x + 1][y - 1] == "M" and data[x + 2][y - 2] == "A" and data[x + 3][
        y - 3] == "S":
        count += 1

    if x >= 3 and y <= len(data[0]) - 4 and data[x - 1][y + 1] == "M" and data[x - 2][y + 2] == "A" and data[x - 3][
        y + 3] == "S":
        count += 1

    if x <= len(data) - 4 and y <= len(data[0]) - 4 and data[x + 1][y + 1] == "M" and data[x + 2][y + 2] == "A" and \
            data[x + 3][y + 3] == "S":
        count += 1

    return count


def mas_finder(data, x, y):
    count = 0

    if (0 < x < len(data) - 1 and 0 < y < len(data[0]) - 1
            and data[x - 1][y - 1] == "M"
            and data[x + 1][y + 1] == "S"
            and data[x - 1][y + 1] == "M"
            and data[x + 1][y - 1] == "S"):
        count += 1

    if (0 < x < len(data) - 1 and 0 < y < len(data[0]) - 1
            and data[x - 1][y - 1] == "S"
            and data[x + 1][y + 1] == "M"
            and data[x - 1][y + 1] == "S"
            and data[x + 1][y - 1] == "M"):
        count += 1

    if (0 < x < len(data) - 1 and 0 < y < len(data[0]) - 1
            and data[x - 1][y - 1] == "S"
            and data[x + 1][y + 1] == "M"
            and data[x - 1][y + 1] == "M"
            and data[x + 1][y - 1] == "S"):
        count += 1

    if (0 < x < len(data) - 1 and 0 < y < len(data[0]) - 1
            and data[x - 1][y - 1] == "M"
            and data[x + 1][y + 1] == "S"
            and data[x - 1][y + 1] == "S"
            and data[x + 1][y - 1] == "M"):
        count += 1

    return count


def part_1(data):
    count = 0
    coordinates = extract_coordinates(data, "X")
    for x, y in coordinates:
        count += xmas_search(data, x, y)
    return count


def part_2(data):
    count = 0
    coordinates = extract_coordinates(data, "A")
    for x, y in coordinates:
        count += mas_finder(data, x, y)
    return count


def main():
    data = read_file_lines()
    data = build_matrix(data)

    part1 = part_1(data)
    part2 = part_2(data)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
