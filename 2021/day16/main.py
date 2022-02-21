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

    return bin_to_dec("".join(parts)), tail, i

# Part 1 ----------------------------------------------------------------------


def process_rest(type_id, rest):
    if(type_id == 4):
        _, tail, _ = process_literal(rest)
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


def process2(bin_num, length=0):
    packet_type = int(bin_num[3:6], 2)
    length += 6
    packet_value = ''
    if packet_type == 4:
        remaining = bin_num[6:]
        while True:
            if remaining[0] == '0':
                packet_value += remaining[1:5]
                remaining = remaining[5:]
                length += 5
                break
            packet_value += remaining[1:5]
            remaining = remaining[5:]
            length += 5
        packet_value = int(packet_value, 2)
    else:
        type_id = bin_num[6]
        remaining = bin_num[7:]
        length += 1
        if type_id == '0':
            total_length = int(remaining[:15], 2)
            remaining = remaining[15:]
            length += 15
            sub_packet_length = 0
            values = []
            while sub_packet_length != total_length:
                remaining, sub_packet_length, value = process2(
                    remaining, sub_packet_length)
                values.append(value)
            length += sub_packet_length
        elif type_id == '1':
            total_count = int(remaining[:11], 2)
            remaining = remaining[11:]
            length += 11
            sub_packet_length = 0
            count = 0
            values = []
            while count != total_count:
                remaining, sub_packet_length, value = process2(
                    remaining, sub_packet_length)
                values.append(value)
                count += 1
            length += sub_packet_length

        if packet_type == 0:
            packet_value = sum(values)
        elif packet_type == 1:
            packet_value = 1
            for item in values:
                packet_value *= item
        elif packet_type == 2:
            packet_value = min(values)
        elif packet_type == 3:
            packet_value = max(values)
        elif packet_type == 5:
            packet_value = 1 if values[0] > values[1] else 0
        elif packet_type == 6:
            packet_value = 1 if values[0] < values[1] else 0
        elif packet_type == 7:
            packet_value = 1 if values[0] == values[1] else 0

    return remaining, length, packet_value


def part2(lines):
    return process2(hex_to_bin(lines[0]))[2]


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
