import math
import re


def print_dict(d):
    for i in d:
        print(i, d[i])

def process_input(lines):
    items = {}
    operations = {}
    tests = {}
    monkeys_count = 0
    
    current_monkey = 0
    for i in lines:
        if i.startswith('Monkey'):
            current_monkey = int(re.findall(r'\d+', i)[0])
            monkeys_count += 1
        elif i.startswith('Starting items'):
            items[current_monkey] = [int(j) for j in i[16:].split(', ')]
        elif i.startswith('Operation'):
            operations[current_monkey] = i[21:]
        elif i.startswith('Test'):
            tests[current_monkey] = i[19:]
        elif i.startswith('If true'):
            tests[current_monkey] += ',' + i[25:]
        elif i.startswith('If false'):
            tests[current_monkey] += ',' + i[26:]
    
    return items, operations, tests, monkeys_count

def update_worry_level(monkey_id, item, operations, part2=False, supermodule=1):
    operator = operations[monkey_id][0]
    second_val = operations[monkey_id][1:]
    if 'old' in second_val:
        second_val = item
    else:
        second_val = int(second_val)

    if operator == '+':
        res = item + second_val
    elif operator == '-':
        res = item - second_val
    elif operator == '*':
        res = item * second_val
    elif operator == '/':
        res = item / second_val
        
    if part2:
        return res % supermodule
    else:
        return res // 3
        
def choose_monkey_throw(monkey_id, worry_level, tests):
    divider, true_monkey, false_monkey = tests[monkey_id].split(',')
    divider, true_monkey, false_monkey = int(divider), int(true_monkey), int(false_monkey)
    if worry_level % divider == 0:
        # print("Monkey", monkey_id, "throws", true_monkey, "the worry level:", worry_level)
        return true_monkey
    else:
        # print("Monkey", monkey_id, "throws", false_monkey, "the worry level:", worry_level)
        return false_monkey


# Part 1 ----------------------------------------------------------------------

def part1(lines):
    items, operations, tests, monkeys_count = process_input(lines)
    inspections = {}
    for _ in range(20):
        for monkey_id in range(monkeys_count):
            to_remove = []
            for item in items[monkey_id]:
                if monkey_id in inspections:
                    inspections[monkey_id] += 1
                else:
                    inspections[monkey_id] = 1
                    
                worry_level = update_worry_level(monkey_id, item, operations)
                dest_monkey = choose_monkey_throw(monkey_id, worry_level, tests)
                
                items[dest_monkey].append(worry_level)
                    
                to_remove.append(item)
            
            for i in to_remove:
                items[monkey_id].remove(i)
    print_dict(items)
    
    res = sorted(inspections.items(), key=lambda x: x[1], reverse=True)
    return res[0][1] * res[1][1]


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    items, operations, tests, monkeys_count = process_input(lines)
    inspections = {}
    
    # --------------------------------------------------------------------------------
    # Tive de copiar pela net bruh
    supermodule = 1
    for i in items:
        for j in items[i]:
            supermodule *= j
            
    # --------------------------------------------------------------------------------
    for _ in range(10000):
        for monkey_id in range(monkeys_count):
            to_remove = []
            for item in items[monkey_id]:
                if monkey_id in inspections:
                    inspections[monkey_id] += 1
                else:
                    inspections[monkey_id] = 1
                    
                worry_level = update_worry_level(monkey_id, item, operations, part2=True, supermodule=supermodule)
                dest_monkey = choose_monkey_throw(monkey_id, worry_level, tests)
                
                items[dest_monkey].append(worry_level)
                    
                to_remove.append(item)
            
            for i in to_remove:
                items[monkey_id].remove(i)
    print_dict(items)
    
    res = sorted(inspections.items(), key=lambda x: x[1], reverse=True)
    print_dict(inspections)
    return res[0][1] * res[1][1]

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
