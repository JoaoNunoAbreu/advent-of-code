import re

# Funções Auxiliares ----------------------------------------------------------

d = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}


def process_line(line):
    nums = re.search('(.*?)(?= \|)', line).group().split()
    code = re.search('(?<=\| )(.*)', line).group().split()

    return nums, code


def get_eight_digit_code(nums):
    for i in nums:
        if(len(i) == 7):
            return i


def digits_in_common(digits1, digits2):
    return [i for i in digits2 if i in digits1]

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    count = 0
    for i in lines:
        nums, code = process_line(i)
        for j in code:
            if(len(j) in [2, 4, 3, 7]):
                count += 1
    return count


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    for i in lines:
        nums, code = process_line(i)
        print(get_eight_digit_code(nums))
        for j in code:
            print(j)
            print(digits_in_common(get_eight_digit_code(nums), j))
    return None


def main():
    file = open('input2.txt', 'r')
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
