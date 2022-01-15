# Classes Auxiliares ----------------------------------------------------------


# Funções Auxiliares ----------------------------------------------------------


def convert_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(i) for i in list(line)])
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print(line)


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    matrix = convert_to_matrix(lines)
    print_matrix(matrix)

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = 'input3.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
