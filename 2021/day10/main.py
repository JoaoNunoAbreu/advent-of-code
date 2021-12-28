# Funções Auxiliares ----------------------------------------------------------

chunks = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>'
}

pontos = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

pontos2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def get_reverse_array(arr):
    res = []
    for i in arr:
        res.insert(0, chunks[i])

    return res


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    contador = 0
    for line in lines:
        arr = []
        for j in line:
            if j in chunks:
                arr.append(j)
            else:
                if(chunks[arr[-1]] == j):
                    arr.pop()
                else:
                    # print(
                    #    f'Expected {chunks[arr[-1]]}, but found {j} instead.')
                    contador += pontos[j]
                    break
    return contador


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    values = []
    for line in lines:
        arr = []
        somador = 0
        corrupto = False

        for j in line:
            if j in chunks:
                arr.append(j)
            else:
                if(chunks[arr[-1]] == j):
                    arr.pop()
                else:
                    # print(
                    #     f'Expected {chunks[arr[-1]]}, but found {j} instead.')
                    corrupto = True
                    break

        if(corrupto == False):
            for i in get_reverse_array(arr):
                somador = somador * 5 + pontos2[i]
            values.append(somador)

    values.sort()

    return values[int((len(values) - 1) / 2)]


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
