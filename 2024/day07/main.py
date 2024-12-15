from utils.files import *
from itertools import product


def concat_numbers(n1, n2):
    return int(str(n1) + str(n2))


def process_data(data):
    res = []
    for line in data:
        parts = line.split(':')
        result = int(parts[0])
        nums = [int(x) for x in parts[1].split()]
        res.append((result, nums))
    return res


def calculate_operation_combinations(num_of_numbers, operations):
    if num_of_numbers <= 1:
        return []

    num_of_operations = num_of_numbers - 1
    operation_combinations = [''.join(p) for p in product(operations, repeat=num_of_operations)]
    return operation_combinations


def eval_equation(combination):
    result = combination[0]
    i = 1
    while i < len(combination):
        operator = combination[i]
        operand = combination[i + 1]
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "|":
            result = concat_numbers(result, operand)
        i += 2
    return result


def generate_equation(ops, numbers):
    equation = []
    for i in range(len(numbers)):
        equation.append(numbers[i])
        if i < len(ops):
            equation.append(ops[i])
    return equation


def calculate(equations, valid_operations):
    count = 0
    for [result, numbers] in equations:
        operations_combinations = calculate_operation_combinations(len(numbers), valid_operations)

        for ops in operations_combinations:
            equation = generate_equation(ops, numbers)
            res_equation = eval_equation(equation)
            if res_equation == result:
                count += result
                break

    return count


def part_1(equations):
    operations = ['+', '*']
    return calculate(equations, operations)


def part_2(equations):
    operations = ['+', '*', '|']
    return calculate(equations, operations)


def main():
    data = read_file_lines()
    equations = process_data(data)

    part1 = part_1(equations)
    part2 = part_2(equations)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
