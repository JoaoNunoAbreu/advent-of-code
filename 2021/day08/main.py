import re

# Funções Auxiliares ----------------------------------------------------------


def process_line(line):
    nums = re.search('(.*?)(?= \|)', line).group().split()
    code = re.search('(?<=\| )(.*)', line).group().split()

    return nums, code


def get_numbers(nums):
    one, four, seven, eight = 0, 0, 0, 0
    res_five = []
    res_six = []
    for i in nums:
        if(len(i) == 7):
            eight = i
        elif(len(i) == 3):
            seven = i
        elif(len(i) == 2):
            one = i
        elif(len(i) == 4):
            four = i
        elif(len(i) == 5):
            res_five.append(i)
        elif(len(i) == 6):
            res_six.append(i)
    return one, four, seven, eight, res_five, res_six


def digits_not_in_common(digits1, digits2):
    return len([i for i in digits2 if i not in digits1])


def digits_not_in_common_list(digits1, digits2):
    return [i for i in digits2 if i not in digits1]


def digits_in_common(digits1, digits2):
    return [i for i in digits2 if i in digits1]


def find_three(res_five):
    if(digits_not_in_common(res_five[0], res_five[1]) == 2):
        return res_five[2]
    elif(digits_not_in_common(res_five[0], res_five[2]) == 2):
        return res_five[1]
    elif(digits_not_in_common(res_five[1], res_five[2]) == 2):
        return res_five[0]
    else:
        print("Erro no find three!")


def find_two(one, four, res_five):
    print(one, four, res_five)
    common = digits_not_in_common_list(one, four)
    print(common)
    if(all(elem in res_five[0] for elem in common)):
        return res_five[1]
    elif(all(elem in res_five[1] for elem in common)):
        return res_five[0]
    else:
        print("Erro no find two!")


def find_zero(five, res_six):
    if(digits_not_in_common(five, res_six[0]) == 2):
        return res_six[0]
    elif(digits_not_in_common(five, res_six[1]) == 2):
        return res_six[1]
    elif(digits_not_in_common(five, res_six[2]) == 2):
        return res_six[2]
    else:
        print("Erro no find zero!")


def find_nine(one, res_six):
    common = list(one)
    if(all(elem in res_six[0] for elem in common)):
        return res_six[0]
    else:
        return res_six[1]


def equal_strings(str1, str2):
    return sorted(str1) == sorted(str2)

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
    result = 0
    for i in lines:
        res = []
        nums, code = process_line(i)
        one, four, seven, eight, res_five, res_six = get_numbers(nums)
        three = find_three(res_five)
        res_five.remove(three)
        two = find_two(one, four, res_five)
        res_five.remove(two)
        five = res_five[0]
        zero = find_zero(five, res_six)
        res_six.remove(zero)
        nine = find_nine(one, res_six)
        res_six.remove(nine)
        six = res_six[0]

        res.append(zero)
        res.append(one)
        res.append(two)
        res.append(three)
        res.append(four)
        res.append(five)
        res.append(six)
        res.append(seven)
        res.append(eight)
        res.append(nine)

        res = [''.join(sorted(ele)) for ele in res]
        print(res)
        res_str = ""
        for j in code:
            for num in range(len(res)):
                if(equal_strings(j, res[num])):
                    res_str += str(num)
        result += int(res_str)

    return result


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
