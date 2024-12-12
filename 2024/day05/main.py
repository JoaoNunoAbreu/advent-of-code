from collections import defaultdict

from utils.files import read_file_lines


def process_input(data):
    split_index = data.index('')
    rules = data[:split_index]
    updates = data[split_index + 1:]

    for i in range(len(rules)):
        rules[i] = rules[i].split('|')
        rules[i] = (int(rules[i][0]), int(rules[i][1]))

    for i in range(len(updates)):
        updates[i] = updates[i].split(',')
        for j in range(len(updates[i])):
            updates[i][j] = int(updates[i][j])

    return rules, updates


def build_dict(rules):
    d = defaultdict(lambda: [])  # list represents "smaller than"

    for rule in rules:
        first = rule[0]
        second = rule[1]
        d[first].append(second)

    return d


def calculate_valids_and_invalids(d, updates):
    valids = []
    invalids = []
    for update in updates:
        invalid = False
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if update[j] not in d[update[i]]:
                    invalid = True
                    break
            if invalid:
                invalids.append(update)
                break
        if not invalid:
            valids.append(update)

    return valids, invalids


def part_1(rules, updates):
    d = build_dict(rules)

    valids, _ = calculate_valids_and_invalids(d, updates)

    count = 0
    for valid in valids:
        count += valid[len(valid) // 2]

    return count


def part_2(rules, updates):
    d = build_dict(rules)

    _, invalids = calculate_valids_and_invalids(d, updates)

    for invalid in invalids:
        swap = False
        i = 0
        while i < len(invalid):
            for j in range(i + 1, len(invalid)):
                if invalid[j] not in d[invalid[i]]:
                    invalid[i], invalid[j] = invalid[j], invalid[i]
                    swap = True
                    break
            if swap:
                i = 0
                swap = False
            else:
                i += 1

    count = 0
    for valid in invalids:
        count += valid[len(valid) // 2]

    return count


def main():
    data = read_file_lines()
    rules, updates = process_input(data)

    part1 = part_1(rules, updates)
    part2 = part_2(rules, updates)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main()
