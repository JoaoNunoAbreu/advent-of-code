# Part 1 ----------------------------------------------------------------------

def part1(lines):
    moves = lines[0]
    x_val = y_val = 0
    res = set((0, 0))
    for move in moves:
        if move == ">":
            x_val += 1
        elif move == "<":
            x_val -= 1
        elif move == "^":
            y_val += 1
        elif move == "v":
            y_val -= 1
        else:
            print("invalid move")
        res.add((x_val, y_val))
    return len(res)

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    moves = lines[0]
    x_val = y_val = 0
    x_val_r = y_val_r = 0
    res = set()
    santa_turn = True
    for move in moves:
        if move == ">":
            if santa_turn: 
                x_val += 1
            else:
                x_val_r += 1
        elif move == "<":
            if santa_turn:
                x_val -= 1
            else:
                x_val_r -= 1
        elif move == "^":
            if santa_turn:
                y_val += 1
            else:
                y_val_r += 1
        elif move == "v":
            if santa_turn:
                y_val -= 1
            else:
                y_val_r -= 1
        else:
            print("invalid move")

        res.add((x_val, y_val))
        res.add((x_val_r, y_val_r))
            
        santa_turn = not santa_turn
    return len(res)

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()