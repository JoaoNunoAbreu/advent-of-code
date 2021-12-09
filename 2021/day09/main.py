import re

# Funções Auxiliares ----------------------------------------------------------


def get_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(i) for i in list(line)])
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print("".join(line))


def check_adjacent(matrix, x, y):
    width = len(matrix[0])
    height = len(matrix)

    # Canto superior esquerdo
    if(x == 0 and y == 0 and matrix[y][x] < min(matrix[y+1][x], matrix[y][x+1])):
        return True
    # Canto superior direito
    elif(x == width-1 and y == 0 and matrix[y][x] < min(matrix[y+1][x], matrix[y][x-1])):
        return True
    # Canto inferior esquerdo
    elif(x == 0 and y == height-1 and matrix[y][x] < min(matrix[y-1][x], matrix[y][x+1])):
        return True
    # Canto inferior direito
    elif(x == width-1 and y == height-1 and matrix[y][x] < min(matrix[y-1][x], matrix[y][x-1])):
        return True
    # Primeira linha
    elif(y == 0 and x != 0 and x != width-1 and
         matrix[y][x] < min(matrix[y+1][x], matrix[y][x-1], matrix[y][x+1])):
        return True
    # Última linha
    elif(y == height-1 and x != 0 and x != width-1 and
         matrix[y][x] < min(matrix[y-1][x], matrix[y][x-1], matrix[y][x+1])):
        return True
    # Primeira coluna
    elif(x == 0 and y != 0 and y != height-1 and
         matrix[y][x] < min(matrix[y-1][x], matrix[y+1][x], matrix[y][x+1])):
        return True
    # Última coluna
    elif(x == width-1 and y != 0 and y != height-1 and
         matrix[y][x] < min(matrix[y+1][x], matrix[y-1][x], matrix[y][x-1])):
        return True
    elif(y-1 >= 0 and y+1 <= height-1 and x - 1 >= 0 and x + 1 <= width-1 and
         matrix[y][x] < min(matrix[y-1][x], matrix[y+1][x], matrix[y][x-1], matrix[y][x+1])):
        return True


def checker(matrix):
    res = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(check_adjacent(matrix, x, y)):
                res.append((y, x))
    return res


def depth_find_adjacent(matrix, x, y, visited):
    width = len(matrix[0])
    height = len(matrix)
    res = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if(i == x and j == y):
                continue
            if(i >= 0 and i < width and j >= 0 and j < height and
               not visited[i][j] and matrix[i][j] > matrix[y][x]):
                print("i,j:", i, j, "=", matrix[i][j])
                print("x,y:", x, y, "=", matrix[y][x])
                print("----")
                res.append((i, j))
                visited[i][j] = True
    return res

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    matrix = get_matrix(lines)
    res = checker(matrix)
    return sum([matrix[y][x] + 1 for (y, x) in res])

# Part 2 ----------------------------------------------------------------------

# DOESNT WORK :(


def part2(lines):
    matrix = get_matrix(lines)
    res = checker(matrix)
    result = []
    for (y, x) in res:
        print("x,y: ", x, y)
        result.append(depth_find_adjacent(matrix, x, y, [[False for i in range(len(matrix[0]))]
                                                         for j in range(len(matrix))]))
    for i in result:
        print("len(i): ", len(i))
        print(i)
        print("")
    return None


def main():
    file = open('input2.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part: ", end="")
    part = input()

    if(part == "1"):
        print(part1(lines))
    elif(part == "2"):
        print(part2(lines))
    else:
        print("Parte inválida!")


if __name__ == "__main__":
    main()
