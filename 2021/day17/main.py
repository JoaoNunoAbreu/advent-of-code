import re

# Funções Auxiliares ----------------------------------------------------------


def process_input(lines):
    line = lines[0]
    line = line[13:]
    xi, xf = re.search('(?<=x=)(.*?)(?=,)', line).group().split('..')
    yi, yf = re.search('(?<=y=)(.*)', line).group().split('..')
    return int(xi), int(xf), int(yi), int(yf)


def calculate_trajectory(initial_vel_x, initial_vel_y, area):
    pos_x, pos_y = 0, 0
    max_y = -9e99
    vel_x = initial_vel_x
    vel_y = initial_vel_y
    while True:

        # Next position
        pos_x += vel_x
        pos_y += vel_y

        # Drag and gravity adjustments
        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1
        else:
            vel_x = 0
        vel_y -= 1

        # Stop unnecessary calculations
        if pos_x > area[1]:
            break
        if pos_y < area[2] or pos_y > 10000:
            break

        # Check if it's the highest point
        if(pos_y > max_y):
            max_y = pos_y

        # Check if we've reached the area
        if area[0] <= pos_x <= area[1] and area[2] <= pos_y <= area[3]:
            return max_y

    # In case we didn't reach the area
    return None


def test_possibilities(area):
    vel_x_min = 1
    vel_x_max = area[1]
    vel_y_min = -10000
    vel_y_max = 10000
    d = {}
    res = -9e99
    for i in range(vel_x_min, vel_x_max + 1):
        for j in range(vel_y_min, vel_y_max + 1):
            max_y = calculate_trajectory(i, j, area)
            if(max_y != None):
                d[(i, j)] = max_y
                if(max_y > res):
                    res = max_y
    return res, d


def exercise(lines):
    area = process_input(lines)
    return test_possibilities(area)

# Part 1 ----------------------------------------------------------------------


def part1(res):
    return res[0]


# Part 2 ----------------------------------------------------------------------

def part2(res):
    return len(res[1])


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    res = exercise(lines)
    print("Part 1:", part1(res))
    print("Part 2:", part2(res))


if __name__ == "__main__":
    main()
