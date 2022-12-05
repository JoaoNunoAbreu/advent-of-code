def pretty_print(stack):
    for key, value in stack.items():
        print(key, value)

def separate_input(lines):
    numbers_line = 0
    moves_line = 0
    for index, line in enumerate(lines):
        if line.startswith(" 1"):
            numbers_line = index
        if line == "":
            moves_line = index
    return lines[0:numbers_line], lines[numbers_line:moves_line], lines[moves_line+1:]

def process_stack(stack, numbers):
    d = {
        k+1: []
        for k in range(len(numbers))
    }
    for line in stack:
        line = line.split(" ")
        for index, char in enumerate(line):
            if char != "_":
                d[index+1].append(char)

    for key, value in d.items():
        d[key] = value[::-1]
    
    return d

def process_numbers(numbers):
    return [int(i.strip()) for i in numbers[0].split("   ")]

def process_moves(moves):
    res = []
    for move in moves:
        parts = move.split(" ")
        count, origem, destino = int(parts[1]), int(parts[3]), int(parts[5])
        res.append((count, origem, destino))
    return res

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    stack, numbers, moves = separate_input(lines)
    numbers = process_numbers(numbers)
    stack = process_stack(stack, numbers)
    moves = process_moves(moves)
    for move in moves:
        count, origem, destino = move
        for _ in range(count):
            stack[destino].append(stack[origem].pop())
    
    message = "".join([stack[i][-1] for i in numbers])
    return message

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    stack, numbers, moves = separate_input(lines)
    numbers = process_numbers(numbers)
    stack = process_stack(stack, numbers)
    moves = process_moves(moves)
    for move in moves:
        count, origem, destino = move
        stack[destino] = stack[destino] + stack[origem][-count:]
        stack[origem] = stack[origem][:-count]
    
    message = "".join([stack[i][-1] for i in numbers])
    return message


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.replace("   \n", "[_]\n").replace("\n", "").replace("     ", " [_] ").replace("     ", " [_] ").replace("    ", "[_] ").replace("[", "").replace("]", "") for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
