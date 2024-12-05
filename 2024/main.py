INPUT_FILE = 'input.txt'

def read_file():
    with open(INPUT_FILE, 'r') as file:
        return [x.strip() for x in file.readlines()]

def process_data(data):
    return [[int(x) for x in line.split('   ')] for line in data]

def part_1(data):
    arr1 = [x[0] for x in data]
    arr2 = [x[1] for x in data]

    arr1.sort()
    arr2.sort()

    return sum([abs(x-y) for x,y in zip(arr1, arr2)])

def part_2(data):
    arr1 = [x[0] for x in data]
    arr2 = [x[1] for x in data]

    arr1.sort()
    arr2.sort()

    map2 = {x:arr2.count(x) for x in arr2}

    return sum([x * map2.get(x, 0) for x in arr1])
    

def main():
    data = read_file()
    processed_data = process_data(data)
    part1 = part_1(processed_data)
    part2 = part_2(processed_data)

    print("Part 1:", part1)
    print("Part 2:", part2)

if __name__ == '__main__':
    main()