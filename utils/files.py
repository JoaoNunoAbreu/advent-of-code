INPUT_FILE = 'input.txt'

def read_file():
    with open(INPUT_FILE, 'r') as file:
        return file.read()

def read_file_lines():
    with open(INPUT_FILE, 'r') as file:
        data = file.readlines()
        return [line.strip() for line in data]

def build_matrix(data):
    return [[char for char in line] for line in data]

def print_matrix(matrix):
    for line in matrix:
        print(' '.join(line))