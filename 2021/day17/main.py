import re
import matplotlib.pyplot as plt

# Funções Auxiliares ----------------------------------------------------------


def process_input(lines):
    line = lines[0]
    line = line[13:]
    xi, xf = re.search('(?<=x=)(.*?)(?=,)', line).group().split('..')
    yi, yf = re.search('(?<=y=)(.*)', line).group().split('..')
    return int(xi), int(xf), int(yi), int(yf)


def calculate_range_of_values(xi, xf, yi, yf):
    res = []
    for x in range(xi, xf + 1):
        for y in range(yi, yf + 1):
            res.append((x, y))
    return res


def draw(res):
    x = [i[0] for i in res]
    y = [i[1] for i in res]
    plt.scatter(x, y)
    plt.show()

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    xi, xf, yi, yf = process_input(lines)
    res = calculate_range_of_values(xi, xf, yi, yf)
    draw(res)
    return len(res)


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = 'input2.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
