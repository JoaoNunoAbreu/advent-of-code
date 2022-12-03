points = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3  # scissors
}
equality = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

def rock_paper_scissors(play1, play2):
    if equality[play1] == play2:
        return points[play2] + 3
    elif play1 == "A":
        if play2 == "Z":
            return points[play2]
        else:
            return points[play2] + 6
    elif play1 == "B":
        if play2 == "X":
            return points[play2]
        else:
            return points[play2] + 6
    elif play1 == "C":
        if play2 == "Y":
            return points[play2]
        else:
            return points[play2] + 6
    
def rock_paper_scissors_ending(play1, play2):
    if play2 == "X": # lose
        if play1 == "A":
            return points["Z"]
        elif play1 == "B":
            return points["X"]
        elif play1 == "C":
            return points["Y"]
    elif play2 == "Y": # empate
        return points[equality[play1]] + 3
    elif play2 == "Z": # win
        if play1 == "A":
            return points["Y"] + 6
        elif play1 == "B":
            return points["Z"] + 6
        elif play1 == "C":
            return points["X"] + 6

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    sum_val = 0
    for line in lines:
        them, me = line.split(' ')
        res = rock_paper_scissors(them, me)
        sum_val += res
    return sum_val

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    sum_val = 0
    for line in lines:
        them, me = line.split(' ')
        res = rock_paper_scissors_ending(them, me)
        sum_val += res
    return sum_val


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
