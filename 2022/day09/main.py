def print_board(visited):
    min_x = min([i[0] for i in visited])
    max_x = max([i[0] for i in visited])
    min_y = min([i[1] for i in visited])
    max_y = max([i[1] for i in visited])
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()
        
def move_to_near(x, y, target_x, target_y):
    if x == target_x and y == target_y:
        return x, y
    elif x < target_x and y == target_y:
        x += 1
    elif x > target_x and y == target_y:
        x -= 1
    elif y < target_y and x == target_x:
        y += 1
    elif y > target_y and x == target_x:
        y -= 1
    elif x < target_x and y < target_y:
        x += 1
        y += 1
    elif x > target_x and y > target_y:
        x -= 1
        y -= 1
    elif x < target_x and y > target_y:
        x += 1
        y -= 1
    elif x > target_x and y < target_y:
        x -= 1
        y += 1
    return x, y

def check_around(h_x, h_y, t_x, t_y):
    return (h_x, h_y) == (t_x, t_y + 1) or \
        (h_x, h_y) == (t_x, t_y - 1) or \
        (h_x, h_y) == (t_x + 1, t_y) or \
        (h_x, h_y) == (t_x - 1, t_y) or \
        (h_x, h_y) == (t_x + 1, t_y + 1) or \
        (h_x, h_y) == (t_x - 1, t_y - 1) or \
        (h_x, h_y) == (t_x + 1, t_y - 1) or \
        (h_x, h_y) == (t_x - 1, t_y + 1) or \
        (h_x, h_y) == (t_x, t_y)

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    h_x, h_y = 0, 0
    t_x, t_y = 0, 0
    visited = set()
    for i in lines:
        direction, count = i.split()[0], int(i.split()[1])
        for _ in range(count):
            old_x, old_y = h_x, h_y
            if direction == "U":
                h_y += 1
            elif direction == "D":
                h_y -= 1
            elif direction == "R":
                h_x += 1
            elif direction == "L":
                h_x -= 1
            
            if check_around(t_x, t_y, old_x, old_y) is False:
                t_x, t_y = move_to_near(t_x, t_y, old_x, old_y)
            visited.add((t_x, t_y))
    print_board(visited)
    return len(visited)

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    knots = {i: (0, 0) for i in range(10)}
    visited = set()
        
    for i in lines:
        direction, count = i.split()[0], int(i.split()[1])
        for _ in range(count):
            old_x, old_y = knots[9]
            h_x, h_y = knots[9]
            if direction == "U":
                h_y += 1
            elif direction == "D":
                h_y -= 1
            elif direction == "R":
                h_x += 1
            elif direction == "L":
                h_x -= 1
                
            knots[9] = (h_x, h_y)
            i = 8
            while (i >= 0):
                old_x, old_y = knots[i+1]
                t_x, t_y = knots[i]
                if check_around(t_x, t_y, old_x, old_y) is False:
                    knots[i] = move_to_near(t_x, t_y, old_x, old_y)
                i -= 1
            
            visited.add((knots[0]))

    
    # Even though the head stop moving, the tail still moves
    for _ in range(10):
        i = 8
        while (i >= 0):
            old_x, old_y = knots[i+1]
            t_x, t_y = knots[i]
            if check_around(t_x, t_y, old_x, old_y) is False:
                knots[i] = move_to_near(t_x, t_y, old_x, old_y)
            i -= 1
        
        visited.add((knots[0]))

    print_board(visited)
    return len(visited)


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
