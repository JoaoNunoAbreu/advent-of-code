from utils.files import *


directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

new_direction = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}


def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^':
                return i, j


def build_path(matrix, visited):
    print("-" * 20)
    matrix = [list(row) for row in matrix]
    for i, j, _ in visited:
        matrix[i][j] = "X"

    return matrix


def is_edge(matrix, i, j):
    return i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1


def extract_visited(state_history):
    return {(i, j) for i, j, _ in state_history}

def walk(matrix, start_i, start_j, start_direction):
    cache = set()
    visited = []
    current_direction = start_direction
    i, j = start_i, start_j

    while True:
        state = (i, j, current_direction)
        if state in cache:
            break

        cache.add(state)
        visited.append((i, j))

        if is_edge(matrix, i, j):
            break

        di, dj = directions[current_direction]
        new_i, new_j = i + di, j + dj

        if matrix[new_i][new_j] == '#':
            current_direction = new_direction[current_direction]
            di, dj = directions[current_direction]
            new_i, new_j = i + di, j + dj

        i, j = new_i, new_j

    return visited


def part_1(path):
    return len(path)


def part_2(matrix, visited):
    i, j = find_start(matrix)
    res = 0

    # remove repeated elements
    visited = list(dict.fromkeys(visited))

    start_pos = (i, j)
    for count, (visited_i, visited_j) in enumerate(visited):

        if (visited_i, visited_j) == start_pos:
            continue
        if matrix[visited_i][visited_j] != '.':
            continue

        original_value = matrix[visited_i][visited_j]
        matrix[visited_i][visited_j] = '#'

        new_visited = walk(matrix, i, j, matrix[i][j])
        last_i, last_j = new_visited[-1]
        if not is_edge(matrix, last_i, last_j):
            res += 1

        matrix[visited_i][visited_j] = original_value

    return res


def main():
    data = read_file_lines()
    matrix = build_matrix(data)
    print_matrix(matrix)

    i, j = find_start(matrix)
    visited = walk(matrix, i, j, matrix[i][j])

    part1 = part_1(set(visited))
    part2 = part_2(matrix, visited)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
