# Funções Auxiliares ----------------------------------------------------------


def len_of_dict(d):
    return sum(d.values())


def fill_dict(lines):
    d = {}
    for i in lines:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def create_new_dict(d):
    new_dict = {}
    for i in d:
        if(i == 0 and 6 in new_dict and 8 in new_dict):
            new_dict[6] += d[i]
            new_dict[8] += d[i]
        elif(i == 0 and 6 not in new_dict and 8 in new_dict):
            new_dict[6] = d[i]
            new_dict[8] += d[i]
        elif(i == 0 and 6 in new_dict and 8 not in new_dict):
            new_dict[6] += d[i]
            new_dict[8] = d[i]
        elif(i == 0 and 6 not in new_dict and 8 not in new_dict):
            new_dict[6] = d[i]
            new_dict[8] = d[i]
        else:
            if(i-1 in new_dict):
                new_dict[i-1] += d[i]
            else:
                new_dict[i-1] = d[i]
    return new_dict


def print_dict(d):
    for i in d:
        print(i, ":", d[i])

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = [int(i) for i in lines[0].split(',')]
    d = fill_dict(line)

    for i in range(80):
        d = create_new_dict(d)
    return len_of_dict(d)


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    line = [int(i) for i in lines[0].split(',')]
    d = fill_dict(line)

    for i in range(256):
        d = create_new_dict(d)
    return len_of_dict(d)


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
