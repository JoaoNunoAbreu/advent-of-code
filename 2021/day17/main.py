# Funções Auxiliares ----------------------------------------------------------


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    pass

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
