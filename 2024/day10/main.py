from collections import defaultdict

from utils.files import *

def find_paths(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(x, y, current_value):
        return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == current_value + 1

    def dfs(x, y, path, visited):
        if matrix[x][y] == 9:
            paths.append(path[:])
            return

        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, matrix[x][y]) and (nx, ny) not in visited:
                dfs(nx, ny, path + [(nx, ny)], visited)
        visited.remove((x, y))


    zero_positions = [(i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == 0]
    paths = []

    for x, y in zero_positions:
        dfs(x, y, [(x, y)], set())

    return paths

def part_1(arr):
    res = defaultdict(set)
    for i in arr:
       res[i[0]].add(i[-1])

    return sum(len(v) for v in res.values())


def part_2(arr):
    res = defaultdict(int)
    for i in arr:
        res[i[0]] += 1

    return sum(res.values())


def main():
    data = read_file_lines()
    matrix = build_matrix_ints(data)
    arr = find_paths(matrix)

    part1 = part_1(arr)
    part2 = part_2(arr)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
