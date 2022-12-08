import json


def update_dir(old, new):
    if old == "/":
        return old + new
    else:
        return old + "/" + new

def calculate_structure(lines):
    d = {
        "/": {
            "parent": "",
            "size": 0
        }
    }
    current_dir = "/"
    for line in lines[1:]:
        if line.startswith("$ cd .."):
            if d[current_dir]["parent"] != "":
                current_dir = d[current_dir]["parent"]
        elif line.startswith("$ cd"):
            old_dir = current_dir
            current_dir = update_dir(current_dir, line.split()[-1])
            if current_dir not in d:
                d[current_dir] = {
                    "parent": old_dir,
                    "size": 0
                }
        elif line.startswith("dir"):
            new_dir = update_dir(current_dir, line.split()[-1])
            if new_dir not in d:
                d[new_dir] = {
                    "parent": current_dir,
                    "size": 0
                }
            d[current_dir]["size"] += d[new_dir]["size"]
        elif line.startswith("$ ls"):
            pass
        else:
            d[current_dir]["size"] += int(line.split()[0])
            parent = d[current_dir]["parent"]
            while parent != "":
                d[parent]["size"] += int(line.split()[0])
                parent = d[parent]["parent"]
    return d

def find_removable(d):
    res = 0
    for data in d.values():
        if data["size"] <= 100000:
            res += data["size"]
    return res

def find_smallest_folder(d):
    unused_space = 70000000 - d["/"]["size"]
    sizes = [data["size"] for data in d.values() if unused_space + data["size"] > 30000000]
    return min(sizes)

# Part 1 ----------------------------------------------------------------------

def part1(lines):
    d = calculate_structure(lines)
    removable = find_removable(d)
    return removable

# Part 2 ----------------------------------------------------------------------

def part2(lines):
    d = calculate_structure(lines)
    return find_smallest_folder(d)


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
