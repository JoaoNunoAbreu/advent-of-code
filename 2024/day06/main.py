from utils.files import *

# matrix
# . . . . # . . . . .
# . . . . . . . . . #
# . . . . . . . . . .
# . . # . . . . . . .
# . . . . . . . # . .
# . . . . . . . . . .
# . # . . ^ . . . . .
# . . . . . . . . # .
# # . . . . . . . . .
# . . . . . . # . . .

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

def print_path(matrix, visited):
    print("-" * 20)
    matrix = [list(row) for row in matrix]
    for i, j in visited:
        matrix[i][j] = "X"

    matrix = ["".join(row) for row in matrix]
    print_matrix(matrix)

def walk(matrix, start_i, start_j, start_direction):
    visited = set()
    current_direction = start_direction
    i, j = start_i, start_j

    while True:
        print(f"Current: ({i}, {j}), Direction: {current_direction}, Visited: {len(visited)}")

        visited.add((i, j))

        if i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1:
            break

        new_i, new_j = i + directions[current_direction][0], j + directions[current_direction][1]

        if matrix[new_i][new_j] == '#':
            current_direction = new_direction[current_direction]
            new_i, new_j = i + directions[current_direction][0], j + directions[current_direction][1]

        i, j = new_i, new_j

    return visited

def part_1(matrix):
    i, j = find_start(matrix)
    visited = walk(matrix, i, j, matrix[i][j])
    print_path(matrix, visited)
    return len(visited)

def part_2(matrix):
    pass


def main():
    data = read_file_lines()
    matrix = build_matrix(data)
    print_matrix(matrix)

    part1 = part_1(data)
    part2 = part_2(data)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
