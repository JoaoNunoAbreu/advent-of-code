# Part 1 ----------------------------------------------------------------------

def part1(lines):
    count = 0
    for line in lines:
        first, second = line.split(',')
        first_parts, second_parts = first.split('-'), second.split('-')
        first_min, first_max = int(first_parts[0]), int(first_parts[1])
        second_min, second_max = int(second_parts[0]), int(second_parts[1])
        range_first = [i for i in range(first_min, first_max + 1)]
        range_second = [i for i in range(second_min, second_max + 1)]
        
        if all([i in range_second for i in range_first]) or all([i in range_first for i in range_second]):
            count += 1
    return count
        

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    count = 0
    for line in lines:
        first, second = line.split(',')
        first_parts, second_parts = first.split('-'), second.split('-')
        first_min, first_max = int(first_parts[0]), int(first_parts[1])
        second_min, second_max = int(second_parts[0]), int(second_parts[1])
        range_first = [i for i in range(first_min, first_max + 1)]
        range_second = [i for i in range(second_min, second_max + 1)]
        
        if any([i in range_second for i in range_first]) or any([i in range_first for i in range_second]):
            count += 1
    return count


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
