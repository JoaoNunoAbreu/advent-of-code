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

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
