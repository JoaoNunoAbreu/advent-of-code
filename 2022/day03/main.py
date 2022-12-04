alphabet = [chr(i) for i in range(65, 91)]
lower_alphabet = [chr(i) for i in range(97, 123)]
points = {alphabet[i]: i+27 for i in range(len(alphabet))}
lower_points = {lower_alphabet[i]: i+1 for i in range(len(lower_alphabet))}


# Part 1 ----------------------------------------------------------------------

def part1(lines):
    res = 0
    for line in lines:
        first, second = line[:len(line)//2], line[len(line)//2:]
        commons = {i for i in first if i in second}
        sum_val = sum([points[i] if i in points else lower_points[i] for i in commons])
        res += sum_val
    return res    

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    res = 0
    lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
    for sublist in lines:
        commons = {i for i in sublist[0] if i in sublist[1] and i in sublist[2]}
        sum_val = sum([points[i] if i in points else lower_points[i] for i in commons])
        res += sum_val
    return res


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
