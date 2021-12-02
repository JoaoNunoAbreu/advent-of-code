import sys


def part1(lines):
    depth = 0
    horizontal = 0
    for i in lines:
        operation, units = i.split()
        units = int(units)
        if(operation == "down"):
            depth += units
        elif(operation == "up"):
            depth -= units
        elif(operation == "forward"):
            horizontal += units

    return depth * horizontal


def part2(lines):
    depth = 0
    horizontal = 0
    aim = 0
    for i in lines:
        operation, units = i.split()
        units = int(units)
        if(operation == "down"):
            aim += units
        elif(operation == "up"):
            aim -= units
        elif(operation == "forward"):
            horizontal += units
            depth += aim * units
    return depth * horizontal


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
