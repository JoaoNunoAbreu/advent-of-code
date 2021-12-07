# Funções Auxiliares ----------------------------------------------------------


def get_fuel(position, target):
    return abs(position - target)


def get_fuel_plus(position, target):
    return abs(position - target) + sum(range(0, abs(position - target)))


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = [int(i) for i in lines[0].split(',')]
    count = 0
    min_value = 9e99
    for i in range(min(line), max(line)):
        for j in line:
            count += get_fuel(i, j)
        min_value = min(min_value, count)
        count = 0

    return min_value


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    line = [int(i) for i in lines[0].split(',')]
    count = 0
    min_value = 9e99
    for i in range(min(line), max(line)):
        print("i: ", i)
        for j in line:
            count += get_fuel_plus(i, j)
        min_value = min(min_value, count)
        count = 0

    return min_value


def main():
    file = open('input.txt', 'r')
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
