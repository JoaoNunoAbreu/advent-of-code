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


def calculate_antinodes(a, b):
    distance_i, distance_j = get_distance(a, b)
    return (a[0] + distance_i, a[1] + distance_j), (b[0] - distance_i, b[1] - distance_j)

def calculate_antinodes_part2(matrix, a, b):
    distance_i, distance_j = get_distance(a, b)
    antinode_1, antinode_2 = (a[0] + distance_i, a[1] + distance_j), (b[0] - distance_i, b[1] - distance_j)

    res = {a, b}
    while is_in_matrix(matrix, antinode_1):
        res.add(antinode_1)
        antinode_1 = (antinode_1[0] + distance_i, antinode_1[1] + distance_j)

    while is_in_matrix(matrix, antinode_2):
        res.add(antinode_2)
        antinode_2 = (antinode_2[0] - distance_i, antinode_2[1] - distance_j)

    return res


def get_possibilities(coords):
    return list(combinations(coords, 2))


def is_in_matrix(matrix, coords):
    return 0 <= coords[0] < len(matrix) and 0 <= coords[1] < len(matrix[0])


def draw_antinodes(matrix, res):
    matrix2 = [list(line) for line in matrix]
    for i in range(len(matrix2)):
        for j in range(len(matrix2[i])):
            if (i, j) in res:
                matrix2[i][j] = '#'

    print_matrix(matrix2)


def part_1(matrix):
    locations = get_locations(matrix)
    res = set()
    for coords in locations.values():
        possibilities = get_possibilities(coords)
        for a, b in possibilities:
            antinodes = calculate_antinodes(a, b)
            for antinode in antinodes:
                if is_in_matrix(matrix, antinode):
                    res.add(antinode)

    draw_antinodes(matrix, res)
    return len(res)


def part_2(matrix):
    locations = get_locations(matrix)
    res = set()
    for coords in locations.values():
        possibilities = get_possibilities(coords)
        for a, b in possibilities:
            antinodes = calculate_antinodes_part2(matrix, a, b)
            for antinode in antinodes:
                if is_in_matrix(matrix, antinode):
                    res.add(antinode)

    draw_antinodes(matrix, res)
    return len(res)


def main():
    data = read_file_lines()
    matrix = build_matrix(data)

    part1 = part_1(matrix)
    part2 = part_2(matrix)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
