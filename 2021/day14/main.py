import copy

# Notes -----------------------------------------------------------------------

''' 
For a better understanding of the code, I recommend reading the following:

After de first step, the dictionary looks like this:

d = {
    'B': {
        'B': 0,
        'N': 0,
        'H': 0,
        'C': 1,
        'count': 2
    },
    'N': {
        'B': 1,
        'N': 0,
        'H': 0,
        'C': 1,
        'count': 2
    },
    'H': {
        'B': 1,
        'N': 0,
        'H': 0,
        'C': 0,
        'count': 1
    },
    'C': {
        'B': 0,
        'N': 1,
        'H': 1,
        'C': 0,
        'count': 2
    }
} 
'''


# Funções Auxiliares ----------------------------------------------------------


def process_lines(lines):
    template = lines[0]
    rules = lines[2:]
    rules_dict = {}
    for i in rules:
        key, value = i.split(' -> ')
        rules_dict[key] = value
    return template, rules_dict


def fill_dict(template, rules):
    d = {}
    letters = list(dict.fromkeys([i for i in rules.values()]))
    for i in letters:
        d[i] = {letter: 0 for letter in letters}
        d[i]['count'] = 0

    for i in range(len(template)):
        letter = template[i]
        d[letter]['count'] += 1

        if(i != len(template)-1):
            d[letter][template[i+1]] += 1
    return d


def counter(d):
    counters = [i['count'] for i in d.values()]
    return max(counters), min(counters)


def step(d, rules):
    new_dict = copy.deepcopy(d)

    for rule in rules:
        first_letter = rule[0]
        second_letter = rule[1]
        pair_occurence = d[first_letter][second_letter]
        if(pair_occurence > 0):
            new_dict[first_letter][second_letter] -= pair_occurence
            new_dict[first_letter][rules[rule]] += pair_occurence
            new_dict[rules[rule]][second_letter] += pair_occurence
            new_dict[rules[rule]]['count'] += pair_occurence
    return new_dict


# Part 1 ----------------------------------------------------------------------


def part1(lines):
    template, rules = process_lines(lines)
    d = fill_dict(template, rules)
    for _ in range(10):
        d = step(d, rules)

    maximum, minimum = counter(d)
    return maximum - minimum


# Part 2 ----------------------------------------------------------------------


def part2(lines):
    template, rules = process_lines(lines)
    d = fill_dict(template, rules)
    for _ in range(40):
        d = step(d, rules)

    maximum, minimum = counter(d)
    return maximum - minimum


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
