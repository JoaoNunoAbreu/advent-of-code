# Funções Auxiliares ----------------------------------------------------------

def process_lines(lines):
    parou_coordenadas = False
    coords = []
    folds = []
    for i in lines:
        if i == '':
            parou_coordenadas = True
        elif parou_coordenadas:
            new_line = i.replace('fold along ', '')
            parts = new_line.split('=')
            pair = (parts[0], int(parts[1]))
            folds.append(pair)
        else:
            coords.append((int(i.split(',')[0]), int(i.split(',')[1])))
    return coords, folds


def pretty_matrix(matrix):
    res = ''
    for i in matrix:
        res += ''.join(i).replace('.', ' ') + '\n'
    return res


def calculate_size(coords):
    x = 0
    y = 0
    for i in coords:
        if i[0] > x:
            x = i[0]
        if i[1] > y:
            y = i[1]
    return x, y


def create_matrix(coords):
    width, height = calculate_size(coords)
    matrix = []
    for i in range(height+1):
        matrix.append(['.'] * (width+1))
    return matrix


def place_coords(matrix, coords):
    for i in coords:
        matrix[i[1]][i[0]] = '#'
    return matrix


def match_lines(line1, line2):
    res = []
    for i in range(len(line1)):
        if line1[i] == '#' or line2[i] == '#':
            res.append('#')
        else:
            res.append('.')
    return res


def column(matrix, i):
    return [row[i] for row in matrix]


def mirror_matrix(matrix):
    for i in range(int(len(matrix) / 2)):
        for j in range(len(matrix[i])):
            matrix[i][j], matrix[-i-1][j] = matrix[-i-1][j], matrix[i][j]
    return matrix


def fold_horizontal(matrix, y):
    normal = matrix[:y]
    mirror = mirror_matrix(matrix[y+1:])
    new_matrix = [[] for _ in range(max(len(normal), len(mirror)))]
    size_new_matrix = len(new_matrix)
    size_normal = len(normal)
    size_mirror = len(mirror)
    for i in range(max(len(normal), len(mirror))):
        if(i < len(normal) and i < len(mirror)):
            new_matrix[size_new_matrix-1 -
                       i] = match_lines(normal[size_normal-1-i], mirror[size_mirror-1-i])
        elif(i < len(normal)):
            new_matrix[size_new_matrix-1-i] = normal[size_normal-1-i]
        elif(i < len(mirror)):
            new_matrix[size_new_matrix-1-i] = mirror[size_mirror-1-i]
    return new_matrix


def rotate_matrix_90(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j].append(matrix[i][j])
    return new_matrix


def fold_vertical(matrix, x):
    new_matrix = []
    for i in range(x):
        matched_column = match_lines(column(matrix, i), column(matrix, -i-1))
        new_matrix.append(matched_column)
    return rotate_matrix_90(new_matrix)


def count_hashtags(matrix):
    return sum([line.count('#') for line in matrix])

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    coords, folds = process_lines(lines)
    matrix = create_matrix(coords)
    matrix = place_coords(matrix, coords)
    res = []
    if(folds[0][0] == 'y'):
        res = fold_horizontal(matrix, folds[0][1])
    elif(folds[0][0] == 'x'):
        res = fold_vertical(matrix, folds[0][1])
    else:
        print("Erro:", folds[0])

    return count_hashtags(res)


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    coords, folds = process_lines(lines)
    matrix = create_matrix(coords)
    matrix = place_coords(matrix, coords)
    for i in folds:
        if(i[0] == 'y'):
            matrix = fold_horizontal(matrix, i[1])
        elif(i[0] == 'x'):
            matrix = fold_vertical(matrix, i[1])
        else:
            print("Erro:", i)

    return "\n" + pretty_matrix(matrix)


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
