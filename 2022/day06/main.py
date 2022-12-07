# Part 1 ----------------------------------------------------------------------

def part1(lines):
    for line in lines:
        begin = 0
        end = 4
        while(end < len(line)):
            four_elements = line[begin:end]
            if len(four_elements) == len(set(four_elements)):
                print(four_elements)
                return end
            begin += 1
            end += 1
            

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    for line in lines:
        begin = 0
        end = 14
        while(end < len(line)):
            fourteen_elements = line[begin:end]
            if len(fourteen_elements) == len(set(fourteen_elements)):
                print(fourteen_elements)
                return end
            begin += 1
            end += 1


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
