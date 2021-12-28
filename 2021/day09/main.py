# Funções Auxiliares ----------------------------------------------------------


def convert_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(i) for i in list(line)])
    return matrix


def checker(matrix):
    res = {}
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            l = [matrix[y][x] for (x, y) in get_around_values(matrix, x, y)]
            if matrix[y][x] < min(l):
                res[(x, y)] = matrix[y][x]
    return res


def get_around_values(matrix, x, y):
    width = len(matrix[0])
    height = len(matrix)

    if(x == 0 and y == 0):
        return [(x, y+1), (x+1, y)]
    elif(x == width-1 and y == 0):
        return [(x, y+1), (x-1, y)]
    elif(x == 0 and y == height-1):
        return [(x, y-1), (x+1, y)]
    elif(x == width-1 and y == height-1):
        return [(x, y-1), (x-1, y)]
    elif(y == 0 and x != 0 and x != width-1):
        return [(x, y+1), (x-1, y), (x+1, y)]
    elif(y == height-1 and x != 0 and x != width-1):
        return [(x, y-1), (x-1, y), (x+1, y)]
    elif(x == 0 and y != 0 and y != height-1):
        return [(x, y-1), (x, y+1), (x+1, y)]
    elif(x == width-1 and y != 0 and y != height-1):
        return [(x, y-1), (x, y+1), (x-1, y)]
    else:
        return [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]


def get_all_around_values(matrix, x, y, visited):

    if((x, y) in visited):
        return []
    else:
        visited.append((x, y))

    positions = get_around_values(matrix, x, y)
    positions = filter_nines_and_visiteds(matrix, positions, visited)

    for (x1, y1) in positions:
        get_all_around_values(matrix, x1, y1, visited)


def filter_nines_and_visiteds(matrix, arr, visited):
    return [(x, y) for (x, y) in arr if matrix[y][x] != 9 or (x, y) in visited]


def get_three_biggest_basins(visited):
    visited.sort(key=len)
    return len(visited[-1]) * len(visited[-2]) * len(visited[-3])

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    matrix = convert_to_matrix(lines)
    res = checker(matrix)
    return sum(res.values()) + len(res)

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    matrix = convert_to_matrix(lines)
    res = checker(matrix)
    all_visited = []
    for (x, y) in res:
        visited = []
        get_all_around_values(matrix, x, y, visited)
        all_visited.append(visited)

    return get_three_biggest_basins(all_visited)


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
