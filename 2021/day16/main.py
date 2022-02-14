# Funções Auxiliares ----------------------------------------------------------

def hex_to_bin(hex_num):
    res = ""
    for i in hex_num:
        res += bin(int(i, 16))[2:].zfill(4)
    return res


def bin_to_dec(bin_num):
    return int(bin_num, 2)


def process_one_packet(bin_num):
    print("-------------------------------------")
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
    print(version, type_id, parts, tail)
    print("-------------------------------------")
    return version


def process_0_operator(bin_num):
    # com length dos packets todos
    print("-------------------------------------")
    res = 0
    length = bin_to_dec(bin_num[7:7+15])
    sub_packets = bin_num[7+15:7+15+length]
    print("sub_packets:", sub_packets)
    #tail = bin_num[7+15+length:]
    while(sub_packets != ""):
        res += process_bin(sub_packets)
    print("-------------------------------------")
    return res


def process_1_operator(bin_num):
    print("-------------------------------------")
    # contem n sub packets
    number_of_sub_packets = bin_to_dec(bin_num[7:7+11])
    sub_tail = bin_num[7+11:]
    res = 0
    for _ in range(number_of_sub_packets):
        res += process_bin(sub_tail)
    print("-------------------------------------")
    return res


def process_bin(bin_num):
    print("bin_num:", bin_num)
    version = bin_to_dec(bin_num[:3])
    type_id = bin_to_dec(bin_num[3:6])
    print("version, type_id:", version, type_id)
    res = 0

    if(type_id == 4):
        res += process_one_packet(bin_num)
    else:
        length_type_id = bin_num[6]
        if(length_type_id == "0"):
            res += process_0_operator(bin_num)
        elif(length_type_id == "1"):
            res += process_1_operator(bin_num)
        else:
            print("Unknown type_id:", type_id)
    return res

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = lines[0]
    print(process_bin(hex_to_bin(line)))

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
