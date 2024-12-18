INPUT_FILE = 'input.txt'


# Files

def read_file():
    with open(INPUT_FILE, 'r') as file:
        return file.read()


def read_file_lines():
    with open(INPUT_FILE, 'r') as file:
        data = file.readlines()
        return [line.strip() for line in data]


# Matrices

def build_matrix(data):
    return [list(line) for line in data]

def build_matrix_ints(data):
    return [list(map(int, line)) for line in data]


def print_matrix(matrix):
    for line in matrix:
        print(' '.join(line))


# Lists/Dicts

def remove_duplicates_preserve_order(visited):
    return list(dict.fromkeys(visited))
