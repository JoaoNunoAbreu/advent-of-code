import sys


def part1(lines):
    count = 0
    for i in range(1, len(lines)):
        if(lines[i] > lines[i-1]):
            count += 1
    return count


def part2(lines):
    count = 0
    for i in range(1, len(lines)-2):
        if(lines[i] + lines[i+1] + lines[i+2] > lines[i-1] + lines[i] + lines[i+1]):
            count += 1
    return count


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [int(i) for i in lines]

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
