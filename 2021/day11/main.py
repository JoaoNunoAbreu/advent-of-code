# Funções Auxiliares ----------------------------------------------------------

def print_matrix(matrix):
    for line in matrix:
        print(line)


def convert_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(i) for i in list(line)])
    return matrix


def flash(matrix, x, y):
    width = len(matrix[0])
    height = len(matrix)

    matrix[y][x] = 0

    if(x == 0 and y == 0):
        matrix[y+1][x] += 1
        matrix[y][x+1] += 1
        matrix[y+1][x+1] += 1
    elif(x == width-1 and y == 0):
        matrix[y+1][x] += 1
        matrix[y][x-1] += 1
        matrix[y+1][x-1] += 1
    elif(x == 0 and y == height-1):
        matrix[y-1][x] += 1
        matrix[y][x+1] += 1
        matrix[y-1][x+1] += 1
    elif(x == width-1 and y == height-1):
        matrix[y-1][x] += 1
        matrix[y][x-1] += 1
        matrix[y-1][x-1] += 1
    elif(x == 0):
        matrix[y-1][x] += 1
        matrix[y][x+1] += 1
        matrix[y+1][x] += 1
        matrix[y+1][x+1] += 1
    elif(x == width-1):
        matrix[y-1][x] += 1
        matrix[y][x-1] += 1
        matrix[y+1][x] += 1
        matrix[y+1][x-1] += 1
    elif(y == 0):
        matrix[y+1][x] += 1
        matrix[y][x-1] += 1
        matrix[y+1][x-1] += 1
        matrix[y+1][x+1] += 1
    elif(y == height-1):
        matrix[y-1][x] += 1
        matrix[y][x-1] += 1
        matrix[y-1][x-1] += 1
        matrix[y-1][x+1] += 1
    else:
        matrix[y-1][x] += 1
        matrix[y][x-1] += 1
        matrix[y+1][x] += 1
        matrix[y+1][x-1] += 1
        matrix[y+1][x+1] += 1
        matrix[y-1][x+1] += 1


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    matrix = convert_to_matrix(lines)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(matrix[y][x] == 9):
                flash(matrix, x, y)
            else:
                matrix[y][x] += 1

    print_matrix(matrix)


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    pass


def main():
    file = open('input3.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
