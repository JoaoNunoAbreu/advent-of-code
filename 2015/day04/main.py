from hashlib import md5


def calculate_md5_hash(string):
    hash_object = md5(string.encode())
    return hash_object.hexdigest()

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    secret_key = lines[0]
    i = 1
    while True:
        hash = calculate_md5_hash(secret_key + str(i))
        if hash.startswith("00000"):
            return i
        i += 1

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    secret_key = lines[0]
    i = 1
    while True:
        hash = calculate_md5_hash(secret_key + str(i))
        if hash.startswith("000000"):
            return i
        i += 1

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()