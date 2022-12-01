def get_list_of_sums(lines):
    string = ",".join(lines)
    separated = string.split(",,")
    list_of_lists = [x.split(",") for x in separated]
    list_of_lists = [[int(y) for y in x] for x in list_of_lists]
    list_of_sums = [sum(x) for x in list_of_lists]
    return list_of_sums

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    list_of_sums = get_list_of_sums(lines)
    return max(list_of_sums)


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    list_of_sums = get_list_of_sums(lines)
    list_of_sums.sort(reverse=True)
    return list_of_sums[0] + list_of_sums[1] + list_of_sums[2]


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
