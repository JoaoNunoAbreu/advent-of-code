# Funções Auxiliares ----------------------------------------------------------

def process_input(lines):
    numbers = [int(i) for i in lines[0].split(",")]
    i = 2
    boards = []
    board = []

    while(i < len(lines)):
        if(lines[i] == ""):
            boards.append(board)
            board = []
        else:
            board.append([int(i) for i in lines[i].split()])
        i += 1
    return numbers, boards


def print_boards(boards):
    for board in boards:
        for row in board:
            print(row)
        print("")


def get_coords_from_board(board, num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == num):
                return i, j
    return -1, -1


def get_horizontal(board, x):
    return board[x]


def get_vertical(board, y):
    return [row[y] for row in board]


def check_victory(board, visited, x, y):
    horizontal = get_horizontal(board, x)
    vertical = get_vertical(board, y)
    h = all(elem in visited for elem in horizontal)
    v = all(elem in visited for elem in vertical)
    return h or v


def find_winner(numbers, boards, visited):
    for num in numbers:
        for board in boards:
            if(num not in visited):
                visited.append(num)
            x, y = get_coords_from_board(board, num)
            if(x != -1 and y != -1 and check_victory(board, visited, x, y)):
                return board, num


def get_sum_of_non_visited(board, visited):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] not in visited):
                sum += board[i][j]
    return sum


def find_loser(numbers, boards, visited):
    winners = []
    for num in numbers:
        for board in boards:
            if(num not in visited):
                visited.append(num)
            x, y = get_coords_from_board(board, num)
            if(x != -1 and y != -1 and check_victory(board, visited, x, y)):
                if(board not in [winners[0] for winners in winners]):
                    winners.append((board, num))
    return winners[-1][0], winners[-1][1]


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    numbers, boards = process_input(lines)
    visited = []
    res_board, res_num = find_winner(numbers, boards, visited)
    return get_sum_of_non_visited(res_board, visited) * res_num

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    numbers, boards = process_input(lines)
    visited = []
    res_board, res_num = find_loser(numbers, boards, visited)
    visited = [res_num]
    i = 0
    while(numbers[i] != res_num):
        visited.append(numbers[i])
        i += 1

    return get_sum_of_non_visited(res_board, visited) * res_num


def main():
    file = open('input.txt', 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part: ", end="")
    part = input()

    if(part == "1"):
        print(part1(lines))
    elif(part == "2"):
        print(part2(lines))
    else:
        print("Parte inválida!")


if __name__ == "__main__":
    main()
