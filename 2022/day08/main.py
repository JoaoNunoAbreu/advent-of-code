def create_matrix(lines):
    matrix = []
    for i in lines:
        matrix.append([int(j) for j in "".join(i)])
    return matrix

def check_around(matrix, i, j):
    left = [matrix[i][k] for k in range(j)]
    right = [matrix[i][k] for k in range(j+1, len(matrix[0]))]
    up = [matrix[k][j] for k in range(i)]
    down = [matrix[k][j] for k in range(i+1, len(matrix))]
    
    return matrix[i][j] > max(left) or matrix[i][j] > max(right) or matrix[i][j] > max(up) or matrix[i][j] > max(down)

def cut_until(arr, val):
    res = 0
    for k in arr:
        if k < val:
            res += 1
        else:
            res += 1
            break
    return res
    
def scenic_score(matrix, i, j):
    left = [matrix[i][k] for k in range(j)][::-1]
    right = [matrix[i][k] for k in range(j+1, len(matrix[0]))]
    up = [matrix[k][j] for k in range(i)][::-1]
    down = [matrix[k][j] for k in range(i+1, len(matrix))]
    
    res_left = cut_until(left, matrix[i][j])
    res_right = cut_until(right, matrix[i][j])
    res_up = cut_until(up, matrix[i][j])
    res_down = cut_until(down, matrix[i][j])
    
    return res_left * res_right * res_up * res_down
    
# Part 1 ----------------------------------------------------------------------

def part1(lines):
    matrix = create_matrix(lines)
    res = 0
    checking_spots = [(i, j) for i in range(1, len(matrix)-1) for j in range(1, len(matrix[0])-1)]
    for i in checking_spots:
        if check_around(matrix, i[0], i[1]):
            res += 1
    
    return len(matrix) * 2 + (len(matrix[0]) - 2) * 2 + res

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    matrix = create_matrix(lines)
    max_val = 0
    checking_spots = [(i, j) for i in range(1, len(matrix)-1) for j in range(1, len(matrix[0])-1)]
    for i in checking_spots:
        max_val = max(scenic_score(matrix, i[0], i[1]), max_val)
    return max_val


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
