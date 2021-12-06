import re

# Funções Auxiliares ----------------------------------------------------------


def process_line(line):
    x1, y1 = re.search('(.*?)(?= ->)', line).group().split(',')
    x2, y2 = re.search('(?<=-> )(.*)', line).group().split(',')

    return int(x1), int(y1), int(x2), int(y2)


def check_vertical_or_horizontal(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


def get_vertical_or_horizontal(lines):
    res = []
    for i in lines:
        x1, y1, x2, y2 = process_line(i)
        if(check_vertical_or_horizontal(x1, y1, x2, y2)):
            res.append((x1, y1, x2, y2))
    return res


def get_vertical_or_horizontal_or_diagonal(lines):
    return [process_line(i) for i in lines]


def get_path(x1, y1, x2, y2):
    if(x1 == x2):
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif(y1 == y2):
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif(x1 < x2 and y1 < y2):
        return [(x1 + i, y1 + i) for i in range(abs(x2 - x1)+1)]
    elif(x1 < x2 and y1 > y2):
        return [(x1 + i, y1 - i) for i in range(abs(x2 - x1)+1)]
    elif(x1 > x2 and y1 < y2):
        return [(x1 - i, y1 + i) for i in range(abs(x2 - x1)+1)]
    elif(x1 > x2 and y1 > y2):
        return [(x1 - i, y1 - i) for i in range(abs(x2 - x1)+1)]


def count_coords_twice(d):
    count = 0
    for i in d:
        if(d[i] >= 2):
            count += 1
    return count

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    d = {}
    new_lines = get_vertical_or_horizontal(lines)
    for (x1, y1, x2, y2) in new_lines:
        path = get_path(x1, y1, x2, y2)
        for coord in path:
            if coord in d:
                d[coord] += 1
            else:
                d[coord] = 1

    return count_coords_twice(d)

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    d = {}
    new_lines = get_vertical_or_horizontal_or_diagonal(lines)
    for (x1, y1, x2, y2) in new_lines:
        path = get_path(x1, y1, x2, y2)
        for coord in path:
            if coord in d:
                d[coord] += 1
            else:
                d[coord] = 1

    return count_coords_twice(d)


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part: ", end="")
    part = input()

    if(part == "1"):
        print(part1(lines))
    elif(part == "2"):
        print(part2(lines))
    else:
        print("Parte inválida!")


if __name__ == "__main__":
    main()
