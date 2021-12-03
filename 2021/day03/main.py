# Funções Auxiliares ----------------------------------------------------------


def get_bit_column(lines, column, gamma=True):
    zeros = 0
    ones = 0
    res = "0"
    for j in range(len(lines)):
        if(lines[j][column] == "0"):
            zeros += 1
        else:
            ones += 1

    if(ones >= zeros and gamma):
        res = "1"
    elif(ones < zeros and not gamma):
        res = "1"
    elif(ones == zeros and not gamma):
        res = "0"

    return res


def get_gamma(lines):
    result = ""
    for i in range(len(lines[0])):
        result += get_bit_column(lines, i)
    return result


def get_epsilon(gamma_binary):
    epsilon = ""
    for i in gamma_binary:
        if(i == "1"):
            epsilon += "0"
        else:
            epsilon += "1"

    return epsilon


def bin_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        if(binary[i] == "1"):
            decimal += 2**(len(binary)-i-1)
    return decimal


def filter_lines(lines, oxygen=False):
    res = [lines]
    size = len(lines[0])
    i = 0
    while(len(res[-1]) != 1):
        l = []
        for j in res[-1]:
            if(get_bit_column(res[-1], i, oxygen) == j[i]):
                l.append(j)
        res.append(l)
        i += 1
    return res[-1][0]


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    gamma_binary = get_gamma(lines)
    print("gamma_binary = ", gamma_binary)
    epsilon_binary = get_epsilon(gamma_binary)
    return bin_to_decimal(gamma_binary) * bin_to_decimal(epsilon_binary)


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    oxygen = filter_lines(lines, True)
    co2 = filter_lines(lines)
    return bin_to_decimal(oxygen) * bin_to_decimal(co2)


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
