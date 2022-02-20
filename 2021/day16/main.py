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
        parts.append(bin_num[i:i+5])
        i += 5
    parts.append(bin_num[i:i+5])
    tail = bin_num[i+5:]
    return parts, tail


def process_rest(type_id, rest):
    if(type_id == 4):
        parts, tail = process_literal(rest)
        print(parts, tail)
        return process(tail)
    else:
        length_type_id = rest[0]
        if(length_type_id == "0"):
            length_sub_packets = bin_to_dec(rest[1:16])
            sub_packets = rest[16:16+length_sub_packets]
            tail = rest[16+length_sub_packets:]
            return process(sub_packets) + process(tail)
        elif(length_type_id == "1"):
            number_of_sub_packets = bin_to_dec(rest[1:12])
            return process(rest[12:])
        else:
            print("Error")
            sys.exit(0)
    return 0


def process(bin_num):
    if(bin_num == "" or bin_to_dec(bin_num) == 0):
        return 0
    else:
        version, type_id, rest = initial_process(bin_num)
        return version + process_rest(type_id, rest)

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = lines[0]
    bin_num = hex_to_bin(line)
    return process(bin_num)

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
