# Funções Auxiliares ----------------------------------------------------------

def hex_to_bin(hex_num):
    res = ""
    for i in hex_num:
        res += bin(int(i, 16))[2:].zfill(4)
    return res


def bin_to_dec(bin_num):
    return int(bin_num, 2)


def process_one_packet(bin_num):
    print("bin_num single:", bin_num)
    version = bin_to_dec(bin_num[:3])
    type_id = bin_to_dec(bin_num[3:6])
    rest = bin_num[6:]
    parts = []
    i = 0
    while(rest[i] == "1"):
        parts.append(rest[i+1:i+5])
        i += 5
    parts.append(rest[i+1:i+5])
    tail = rest[i+5:]
    return version, type_id, parts, tail


def process_bin(bin_num):
    print("bin_num:", bin_num)
    version = bin_to_dec(bin_num[:3])
    type_id = bin_to_dec(bin_num[3:6])
    print("version, type_id:", version, type_id)

    length_type_id = bin_num[6]
    if(length_type_id == "0"):
        # com length dos packets todos
        length = bin_to_dec(bin_num[7:7+15])
        sub_packets = bin_num[7+15:7+15+length]
        tail = bin_num[7+15+length:]
        print(version, type_id, length, sub_packets, tail)
        # ainda falta acabar isto
    else:
        # contem n sub packets
        number_of_sub_packets = bin_to_dec(bin_num[7:7+11])
        sub_tail = bin_num[7+11:]
        for i in range(number_of_sub_packets):
            sub_version, sub_type_id, sub_parts, sub_tail = process_one_packet(
                sub_tail)
            print(sub_version, sub_type_id, sub_parts, sub_tail)

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = lines[0]
    print(process_bin(hex_to_bin(line)))

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = '3_sub_packets.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
