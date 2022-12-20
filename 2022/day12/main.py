from collections import deque


def print_matrix(matrix):
    print("-" * (len(matrix[0]) * 3))
    for line in matrix:
        for x in line:
            print(f'{x:<2}', end=' ')
        print()
    print("-" * (len(matrix[0]) * 3))


def process_input(lines):
    matrix = []
    d = {}
    for i in range(26):
        d[chr(ord('a') + i)] = i

    d['S'] = 0
    d['E'] = 26

    start = None
    end = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                start = (i, j)
            elif lines[i][j] == 'E':
                end = (i, j)

    for line in lines:
        matrix.append([d[x] for x in line])
    return matrix, start, end


def find_shortest_path(matrix, start, end):
    queue = deque([start])
    visited = set([start])
    path = {start: [start]}

    while queue:
        current_pos = queue.popleft()
        current_val = matrix[current_pos[0]][current_pos[1]]
        for next_pos in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            row = current_pos[0] + next_pos[0]
            col = current_pos[1] + next_pos[1]
            if (0 <= row < len(matrix)) and (0 <= col < len(matrix[0])) and (matrix[row][col] <= current_val + 1):
                next_pos = (row, col)
                if next_pos not in visited:
                    queue.append(next_pos)
                    visited.add(next_pos)
                    path[next_pos] = path[current_pos] + [next_pos]
    if end in path:
        return path[end]
    else:
        return []


# Part 1 ----------------------------------------------------------------------

def part1(lines):
    matrix, start, end = process_input(lines)
    path = find_shortest_path(matrix, start, end)
    return len(path) - 1


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    matrix, _, end = process_input(lines)
    starts = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                starts.append((i, j))
    
    res = []
    for start in starts:
        path = find_shortest_path(matrix, start, end)
        if path != []:
            res.append(len(path) - 1)
    return min(res)


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
