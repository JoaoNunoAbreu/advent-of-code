VALS = [40, 80, 120, 160, 200, 240]

def normalize_crt(cycle):
    for i in VALS[::-1]:
        if cycle > i - 1:
            cycle -= i
    return cycle

def print_pixels(pixels):
    for j in VALS:
        for i in range(j-40, j):
            print(pixels[i+1], end='')
        print()

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    cycle = 1
    x = 1
    d = {}
    for line in lines:
        if line.startswith('addx'):
            number = int(line[5:])
            d[cycle] = x
            x += number
            d[cycle + 1] = x
            cycle += 1
        else:
            d[cycle] = x
        cycle += 1
    
    vals = [20, 60, 100, 140, 180, 220]
    return sum([d[i-1]*i for i in vals])


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    cycle = 1
    x = 1
    d = {}
    pixels = {}
    for line in lines:
        
        light_up = x, x+1, x+2
        crt = normalize_crt(cycle)
        if crt in light_up:
            pixels[cycle] = '#'
        else:
            pixels[cycle] = '.'
        
        if line.startswith('addx'):
            number = int(line[5:])
            d[cycle] = x
            x += number
            d[cycle + 1] = x
            
            if crt+1 in light_up:
                pixels[cycle+1] = '#'
            else:
                pixels[cycle+1] = '.'
            
            cycle += 1
        else:
            d[cycle] = x
        cycle += 1

    return print_pixels(pixels)

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
