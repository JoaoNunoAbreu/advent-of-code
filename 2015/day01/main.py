# Part 1 ----------------------------------------------------------------------

def part1(lines):
    sequence = lines[0]
    floor = 0
    for i in sequence:
        if i == '(':
            floor += 1
        else:
            floor -= 1
    return floor

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    index = 0
    sequence = lines[0]
    floor = 0
    for i in sequence:
        if i == '(':
            floor += 1
        else:
            floor -= 1
        index += 1
        if floor == -1:
            return index
    return floor

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()