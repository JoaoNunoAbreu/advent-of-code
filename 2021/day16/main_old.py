# Funções Auxiliares ----------------------------------------------------------

import sys


def hex_to_bin(hex_num):
    res = ""
    for i in hex_num:
        res += bin(int(i, 16))[2:].zfill(4)
    return res


def bin_to_dec(bin_num):
    return int(bin_num, 2)


def initial_process(bin_num):
    version = bin_to_dec(bin_num[:3])
    type_id = bin_to_dec(bin_num[3:6])
    rest = bin_num[6:]
    return version, type_id, rest


def process_literal(bin_num):
    parts = []
    i = 0
    while(bin_num[i] == "1"):
        parts.append(bin_num[i+1:i+5])
        i += 5
    parts.append(bin_num[i+1:i+5])
    tail = bin_num[i+5:]

    return bin_to_dec("".join(parts)), tail

# Part 1 ----------------------------------------------------------------------


def process_rest(type_id, rest):
    if(type_id == 4):
        _, tail = process_literal(rest)
        return process(tail)
    else:
        length_type_id = rest[0]
        if(length_type_id == "0"):
            length_sub_packets = bin_to_dec(rest[1:16])
            sub_packets = rest[16:16+length_sub_packets]
            tail = rest[16+length_sub_packets:]
            return process(sub_packets) + process(tail)
        elif(length_type_id == "1"):
            return process(rest[12:])
        else:
            print("Error")
            sys.exit(0)


def process(bin_num):
    if(bin_num == "" or bin_to_dec(bin_num) == 0):
        return 0
    else:
        version, type_id, rest = initial_process(bin_num)
        return version + process_rest(type_id, rest)


def part1(lines):
    return process(hex_to_bin(lines[0]))

# Part 2 ----------------------------------------------------------------------


d = {
    0: lambda x, y: x+y,
    1: lambda x, y: x*y,
    2: min,
    3: max,
    5: lambda x, y: 1 if x > y else 0,
    6: lambda x, y: 1 if x < y else 0,
    7: lambda x, y: 1 if x == y else 0,
}

d2 = {
    0: 0,
    1: 1,
    2: 9e99,
    3: -9e99,
    5: -9e99,
    6: 9e99,
    7: -9e98,
}


def process_rest2(type_id, rest, extra):
    if(type_id == 4):
        value, tail = process_literal(rest)
        print("value:", value, "tail:", tail, "extra:", extra)
        if(tail == "" or bin_to_dec(tail) == 0):
            return value
        else:
            return d[extra](value, process2(tail, extra))
    else:
        length_type_id = rest[0]
        if(length_type_id == "0"):
            length_sub_packets = bin_to_dec(rest[1:16])
            sub_packets = rest[16:16+length_sub_packets]
            tail = rest[16+length_sub_packets:]
            a = process2(sub_packets, type_id)
            b = process2(tail, type_id)
            print("a:", a, "b:", b)
            if(type_id == 7 and b == -9e98 and a != 0):
                return 1
            else:
                return d[type_id](a, b)
        elif(length_type_id == "1"):
            number_of_sub_packets = bin_to_dec(rest[1:12])
            return process2(rest[12:], type_id)
        else:
            print("Error")
            sys.exit(0)


def process2(bin_num, extra=-1):
    if(bin_num == "" or bin_to_dec(bin_num) == 0):
        return d2[extra]
    else:
        version, type_id, rest = initial_process(bin_num)
        return process_rest2(type_id, rest, extra)


def part2(lines):
    results = [3, 54, 7, 9, 1, 0, 0, 1]
    for i in range(len(lines)):
        a = process2(hex_to_bin(lines[i]))
        b = results[i]
        if a == b:
            print("OK")
        else:
            print("ERROR", a, "!=", b)
        print("----------------------")
    return None
    # return process2(hex_to_bin(lines[0]))


def main():
    filename = 'input2.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    # print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
