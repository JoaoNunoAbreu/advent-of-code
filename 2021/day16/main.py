# Funções Auxiliares ----------------------------------------------------------

def hex_to_bin(hex_num):
    res = ""
    for i in hex_num:
        res += bin(int(i, 16))[2:].zfill(4)
    return res


def bin_to_dec(bin_num):
    return int(bin_num, 2)


def process_bin(bin_num):
    print("bin_num:", bin_num)
    version = bin_to_dec(bin_num[:3])
    type_id = bin_to_dec(bin_num[3:6])
    print("version, type_id:", version, type_id)

    if(type_id == 4):
        rest = bin_num[6:]
        parts = []
        i = 0
        while(rest[i] == "1"):
            parts.append(rest[i+1:i+5])
            i += 5
        parts.append(rest[i+1:i+5])
        tail = rest[i+5:]
        print(version, type_id, parts, tail)
        return bin_to_dec("".join(parts))
    else:
        length_type_id = bin_num[6]
        if(length_type_id == 0):
            length = bin_to_dec(bin_num[7:7+15])
            print("length:", length)
        else:
            print("length_type_id == 1")

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = lines[0]
    print(process_bin(hex_to_bin(line)))

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = 'sub_packets.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
