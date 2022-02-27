from ast import literal_eval

# Funções Auxiliares ----------------------------------------------------------


# Binary tree class with values only at the leaves
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def concat_tree(self, other):
        n = Node(-1)
        n.left = self
        n.right = other
        return n

    def pprint(self, level=0):
        if self.left:
            self.left.pretty_print(level + 1)
        print('\t' * level, self.value)
        if self.right:
            self.right.pretty_print(level + 1)


# [[[6,6],3],0] to binary tree
def array_to_tree(array):
    if len(array) == 1:
        return Node(array[0])
    else:
        return array[0][0].concat_tree(array_to_tree(array[0][1]))


def print_dict(d):
    for k in d:
        print(k, d[k])

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = literal_eval(lines[0])
    print("line:", line)
    x = array_to_tree(line)
    x.pprint()


# Part 2 ----------------------------------------------------------------------

def part2(lines):
    pass


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
