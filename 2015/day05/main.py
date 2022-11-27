def three_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for c in word:
        if c in vowels:
            count += 1
    return count >= 3

def check_double_letter(word):
    for c in range(len(word) - 1):
        if(word[c] == word[c + 1]):
            return True
    return False

def forbidden_strings(word):
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    for string in forbidden_strings:
        if string in word:
            return False
    return True

def check_double_letter_between(word):
    for c in range(len(word) - 2):
        if(word[c] == word[c + 2]):
            return True
    return False

def no_overlap_pairs(word):
    d = {}
    for c in range(len(word) - 1):
        pair = word[c] + word[c + 1]
        if(pair in d):
            d[pair] += [(c, c+1)]
        else:
            d[pair] = [(c, c+1)]
            
    for key in d:
        clean_arr = []
        coord = 0
        while coord < len(d[key]):
            clean_arr.append(d[key][coord])
            if coord + 1 < len(d[key]):
                if(d[key][coord][1] == d[key][coord + 1][0]):
                    coord += 1
                else:
                    clean_arr.append(d[key][coord + 1])
            coord += 1
        if len(clean_arr) > 1:
            return True
            
    return False

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    count = 0
    for line in lines:
        if three_vowels(line) and check_double_letter(line) and forbidden_strings(line):
            count += 1
    return count

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    count = 0
    for line in lines:
        if check_double_letter_between(line) and no_overlap_pairs(line):
            count += 1
    return count

def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()