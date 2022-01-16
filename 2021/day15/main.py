import bisect

# Funções Auxiliares ----------------------------------------------------------


def minPathSumDijkstra(matrix):
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for j in range(m)] for i in range(n)]
    distances = [[float("inf") for j in range(m)] for i in range(n)]
    distances[0][0] = 0
    queue = [(0, (0, 0))]

    while queue:
        x = queue.pop(0)
        i, j = x[1][0], x[1][1]
        if visited[i][j]:
            continue
        visited[i][j] = True

        if i > 0 and not visited[i-1][j]:
            distances[i-1][j] = min(distances[i-1][j],
                                    distances[i][j] + matrix[i-1][j])
            bisect.insort(queue, (distances[i-1][j], (i-1, j)))
        if j > 0 and not visited[i][j-1]:
            distances[i][j-1] = min(distances[i][j-1],
                                    distances[i][j] + matrix[i][j-1])
            bisect.insort(queue, (distances[i][j-1], (i, j-1)))

        if i < n-1 and not visited[i+1][j]:
            distances[i+1][j] = min(distances[i+1][j],
                                    distances[i][j] + matrix[i+1][j])
            bisect.insort(queue, (distances[i+1][j], (i+1, j)))
        if j < m-1 and not visited[i][j+1]:
            distances[i][j+1] = min(distances[i][j+1],
                                    distances[i][j] + matrix[i][j+1])
            bisect.insort(queue, (distances[i][j+1], (i, j+1)))

    return distances[n-1][m-1]


def convert_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(i) for i in list(line)])
    return matrix


def generate_big_map_step(matrix):
    res = []
    for line in matrix:
        new_line = []
        for num in line:
            if(num == 9):
                new_line.append(1)
            else:
                new_line.append(num+1)

        res.append(new_line)
    return res


def generate_big_map(matrix):
    l = [matrix]
    for _ in range(8):
        matrix = generate_big_map_step(matrix)
        l.append(matrix)

    full_matrix = [
        [l[0], l[1], l[2], l[3], l[4]],
        [l[1], l[2], l[3], l[4], l[5]],
        [l[2], l[3], l[4], l[5], l[6]],
        [l[3], l[4], l[5], l[6], l[7]],
        [l[4], l[5], l[6], l[7], l[8]],
    ]

    processed_matrix = []
    for line in full_matrix:
        l = concat_list_of_matrices(line)
        for i in l:
            processed_matrix.append(i)

    return processed_matrix


def concat_list_of_matrices(l):
    res = []
    for i in l:
        res = concat_matrices(res, i)
    return res


def concat_matrices(matrix1, matrix2):
    res = []
    if(len(matrix1) == 0):
        return matrix2
    if(len(matrix2) == 0):
        return matrix1
    for i in range(len(matrix1)):
        res.append(matrix1[i] + matrix2[i])
    return res


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    matrix = convert_to_matrix(lines)
    return minPathSumDijkstra(matrix)

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    matrix = convert_to_matrix(lines)
    new_matrix = generate_big_map(matrix)
    return minPathSumDijkstra(new_matrix)


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
