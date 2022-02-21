import re
''' import matplotlib.pyplot as plt '''

# Funções Auxiliares ----------------------------------------------------------


def process_input(lines):
    line = lines[0]
    line = line[13:]
    xi, xf = re.search('(?<=x=)(.*?)(?=,)', line).group().split('..')
    yi, yf = re.search('(?<=y=)(.*)', line).group().split('..')
    return int(xi), int(xf), int(yi), int(yf)


def calculate_range(xi, xf, yi, yf):
    res = []
    for x in range(xi, xf + 1):
        for y in range(yi, yf + 1):
            res.append((x, y))
    return res


def is_inside_area(x, y, area):
    return (x, y) in area


def calculate_trajectory(vel_x, vel_y, area, min_y):
    pos_x, pos_y = 0, 0
    res = []
    for _ in range(30):
        pos_x += vel_x
        pos_y += vel_y
        res.append((pos_x, pos_y))
        if(is_inside_area(pos_x, pos_y, area)):
            break
        if(pos_y < min_y):
            break
        vel_x = vel_x - 1 if vel_x > 0 else vel_x + 1
        vel_y = vel_y - 1

    return res


def get_max_y_from_trajectory(trajectory):
    max_y = -9e99
    for i in trajectory:
        max_y = max(max_y, i[1])
    return max_y


def test_possibilities(area, vel_x_min, vel_x_max, vel_y_min, vel_y_max):
    max_y = -9e99
    min_y = min(area, key=lambda x: x[1])[1]
    count = 0
    for i in range(vel_x_min, vel_x_max + 1):
        for j in range(vel_y_min, vel_y_max + 1):
            trajectory = calculate_trajectory(i, j, area, min_y)
            if(is_inside_area(trajectory[-1][0], trajectory[-1][1], area)):
                max_y_in_trajectory = get_max_y_from_trajectory(trajectory)
                if(max_y_in_trajectory > max_y):
                    max_y = max_y_in_trajectory
                #plot_graph(area, trajectory)
            print(count, "/", (vel_x_max - vel_x_min + 1)
                  * (vel_y_max - vel_y_min + 1))
            count += 1
    return max_y


''' def plot_graph(area, trajectory):
    x = [i[0] for i in area]
    y = [i[1] for i in area]
    x1 = [i[0] for i in trajectory]
    y1 = [i[1] for i in trajectory]
    plt.scatter(x, y, color='blue')
    plt.scatter(x1, y1, color='red')
    plt.show() '''

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    xi, xf, yi, yf = process_input(lines)
    area = calculate_range(xi, xf, yi, yf)
    #trajectory = calculate_trajectory(6, 9, area)
    #plot_graph(area, trajectory)
    return test_possibilities(area, 1, 200, -200, 200)


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    pass


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
