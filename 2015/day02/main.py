# Part 1 ----------------------------------------------------------------------

def part1(lines):
    total = 0
    for i in lines:
        l, w, h = map(int, i.split("x"))
        area = 2*l*w + 2*w*h + 2*h*l
        smallest = min(l*w, w*h, h*l)
        total += area + smallest
    return total

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    total = 0
    for i in lines:
        l, w, h = map(int, i.split("x"))
        arr = [l, w, h]
        arr.sort()
        l, w, h = arr[0], arr[1], arr[2],
        total += l*2 + w*2 + l*w*h
    return total

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()