from collections import defaultdict
from itertools import combinations

from utils.files import *


def get_locations(matrix):
    d = defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tile = matrix[i][j]
            if tile != '.':
                d[tile].append((i, j))
    return d


def get_distance(a, b):
    return a[0] - b[0], a[1] - b[1]


def get_antinodes_coords(a, b):
    distance_i, distance_j = get_distance(a, b)
    return (a[0] + distance_i, a[1] + distance_j), (b[0] - distance_i, b[1] - distance_j)


def get_possibilities(coords):
    return list(combinations(coords, 2))


def is_in_matrix(matrix, coords):
    return 0 <= coords[0] < len(matrix) and 0 <= coords[1] < len(matrix[0])


def draw_antinodes(matrix, res):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) in res:
                matrix[i][j] = '#'

    print_matrix(matrix)


def part_1(matrix):
    locations = get_locations(matrix)
    res = set()
    for coords in locations.values():
        possibilities = get_possibilities(coords)
        for a, b in possibilities:
            antinodes = get_antinodes_coords(a, b)
            for antinode in antinodes:
                if is_in_matrix(matrix, antinode):
                    res.add(antinode)

    draw_antinodes(matrix, res)
    print(res)
    return len(res)


def part_2(matrix):
    pass


def main():
    data = read_file_lines()
    matrix = build_matrix(data)

    part1 = part_1(matrix)
    part2 = part_2(matrix)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
