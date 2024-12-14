from utils.files import *


DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

NEXT_DIRECTION = {
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
    for i, j in visited:
        matrix[i][j] = "X"

    return matrix


def is_looking_at_edge(matrix, i, j, direction):
    if direction == '^':
        return i == 0
    if direction == 'v':
        return i == len(matrix) - 1
    if direction == '<':
        return j == 0
    if direction == '>':
        return j == len(matrix[0]) - 1


def next_position(i, j, current_direction):
    di, dj = DIRECTIONS[current_direction]
    new_i, new_j = i + di, j + dj
    return new_i, new_j


def walk(matrix, i, j, current_direction):
    state_history = set()
    visited = []
    loop = False
    while True:
        state = (i, j, current_direction)
        if state in state_history:
            loop = True
            break

        state_history.add(state)
        visited.append((i, j))

        if is_looking_at_edge(matrix, i, j, current_direction):
            break

        new_i, new_j = next_position(i, j, current_direction)

        while matrix[new_i][new_j] == '#':
            current_direction = NEXT_DIRECTION[current_direction]
            new_i, new_j = next_position(i, j, current_direction)

        i, j = new_i, new_j

    return visited, loop


def part_1(path):
    return len(path)


def part_2(matrix, visited):
    i, j = find_start(matrix)
    res = 0

    for (visited_i, visited_j) in visited[1:]:
        matrix[visited_i][visited_j] = '#'

        _, loop = walk(matrix, i, j, matrix[i][j])
        if loop:
            res += 1

        matrix[visited_i][visited_j] = '.'

    return res


def main():
    data = read_file_lines()
    matrix = build_matrix(data)
    print_matrix(matrix)

    i, j = find_start(matrix)
    visited, _ = walk(matrix, i, j, matrix[i][j])
    visited = remove_duplicates_preserve_order(visited)

    new_matrix = build_path(matrix, visited)
    print_matrix(new_matrix)

    part1 = part_1(visited)
    part2 = part_2(matrix, visited)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
