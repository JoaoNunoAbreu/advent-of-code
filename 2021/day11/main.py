# Funções Auxiliares ----------------------------------------------------------


def convert_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(i) for i in list(line)])
    return matrix


def flash(matrix, x, y, flashed_points):
    width = len(matrix[0])
    height = len(matrix)

    if(x == 0 and y == 0):
        if((x, y+1) not in flashed_points):
            matrix[y+1][x] += 1
        if((x+1, y) not in flashed_points):
            matrix[y][x+1] += 1
        if((x+1, y+1) not in flashed_points):
            matrix[y+1][x+1] += 1
    elif(x == width-1 and y == 0):
        if((x, y+1) not in flashed_points):
            matrix[y+1][x] += 1
        if((x-1, y) not in flashed_points):
            matrix[y][x-1] += 1
        if((x-1, y+1) not in flashed_points):
            matrix[y+1][x-1] += 1
    elif(x == 0 and y == height-1):
        if((x, y - 1) not in flashed_points):
            matrix[y-1][x] += 1
        if((x+1, y) not in flashed_points):
            matrix[y][x+1] += 1
        if((x+1, y-1) not in flashed_points):
            matrix[y-1][x+1] += 1
    elif(x == width-1 and y == height-1):
        if((x, y - 1) not in flashed_points):
            matrix[y-1][x] += 1
        if((x-1, y) not in flashed_points):
            matrix[y][x-1] += 1
        if((x-1, y-1) not in flashed_points):
            matrix[y-1][x-1] += 1
    elif(x == 0):
        if((x, y - 1) not in flashed_points):
            matrix[y-1][x] += 1
        if((x+1, y) not in flashed_points):
            matrix[y][x+1] += 1
        if((x, y+1) not in flashed_points):
            matrix[y+1][x] += 1
        if((x+1, y+1) not in flashed_points):
            matrix[y+1][x+1] += 1
        if((x+1, y-1) not in flashed_points):
            matrix[y-1][x+1] += 1
    elif(x == width-1):
        if((x, y - 1) not in flashed_points):
            matrix[y-1][x] += 1
        if((x-1, y) not in flashed_points):
            matrix[y][x-1] += 1
        if((x, y+1) not in flashed_points):
            matrix[y+1][x] += 1
        if((x-1, y+1) not in flashed_points):
            matrix[y+1][x-1] += 1
        if((x-1, y-1) not in flashed_points):
            matrix[y-1][x-1] += 1
    elif(y == 0):
        if((x, y+1) not in flashed_points):
            matrix[y+1][x] += 1
        if((x-1, y) not in flashed_points):
            matrix[y][x-1] += 1
        if((x+1, y) not in flashed_points):
            matrix[y][x+1] += 1
        if((x-1, y+1) not in flashed_points):
            matrix[y+1][x-1] += 1
        if((x+1, y+1) not in flashed_points):
            matrix[y+1][x+1] += 1
    elif(y == height-1):
        if((x, y - 1) not in flashed_points):
            matrix[y-1][x] += 1
        if((x-1, y) not in flashed_points):
            matrix[y][x-1] += 1
        if((x+1, y) not in flashed_points):
            matrix[y][x+1] += 1
        if((x-1, y-1) not in flashed_points):
            matrix[y-1][x-1] += 1
        if((x+1, y-1) not in flashed_points):
            matrix[y-1][x+1] += 1
    else:
        if((x, y - 1) not in flashed_points):
            matrix[y-1][x] += 1
        if((x-1, y) not in flashed_points):
            matrix[y][x-1] += 1
        if((x+1, y) not in flashed_points):
            matrix[y][x+1] += 1
        if((x, y+1) not in flashed_points):
            matrix[y+1][x] += 1
        if((x-1, y+1) not in flashed_points):
            matrix[y+1][x-1] += 1
        if((x+1, y+1) not in flashed_points):
            matrix[y+1][x+1] += 1
        if((x-1, y-1) not in flashed_points):
            matrix[y-1][x-1] += 1
        if((x+1, y-1) not in flashed_points):
            matrix[y-1][x+1] += 1


def replace_above_nine_with_zero(matrix, flashed_points):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(matrix[y][x] > 9 and (x, y) in flashed_points):
                matrix[y][x] = 0
    return matrix


def step(matrix):
    flashed_points = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] += 1
            if(matrix[y][x] > 9):
                flash(matrix, x, y, flashed_points)
                flashed_points.append((x, y))
    return flashed_points


def step_without_increment(matrix, flashed_points):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(matrix[y][x] > 9 and (x, y) not in flashed_points):
                flash(matrix, x, y, flashed_points)
                flashed_points.append((x, y))
    return flashed_points


def search_for_suitable_flash(matrix, flashed_points):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(matrix[y][x] > 9 and (x, y) not in flashed_points):
                flash(matrix, x, y, flashed_points)
                flashed_points.append((x, y))
    return flashed_points

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    matrix = convert_to_matrix(lines)
    res = 0
    for _ in range(100):
        flashed_points = step(matrix)
        replace_above_nine_with_zero(matrix, flashed_points)

        # Repeat until no more flashes are available
        old_flashes = []
        while(old_flashes != flashed_points):
            old_flashes = [i for i in flashed_points]
            flashed_points = search_for_suitable_flash(matrix, flashed_points)

        replace_above_nine_with_zero(matrix, flashed_points)
        res += len(flashed_points)
    return res

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    matrix = convert_to_matrix(lines)
    res = 0
    size_of_matrix = len(matrix) * len(matrix[0])
    for i in range(int(9e99)):
        flashed_points = step(matrix)
        replace_above_nine_with_zero(matrix, flashed_points)

        # Repeat until no more flashes are available
        old_flashes = []
        while(old_flashes != flashed_points):
            old_flashes = [i for i in flashed_points]
            flashed_points = search_for_suitable_flash(matrix, flashed_points)

        replace_above_nine_with_zero(matrix, flashed_points)
        if(len(flashed_points) == size_of_matrix):
            res = i
            break
    return res+1


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
