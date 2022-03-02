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

    def in_order(self, level=0):
        if self.left is not None:
            self.left.in_order(level+1)
        if(self.value != -1):
            print(self.value, level)
        if self.right is not None:
            self.right.in_order(level+1)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# nested arrays to binary tree
def array_to_tree(arr):
    if isinstance(arr, int):
        return Node(arr)
    else:
        return array_to_tree(arr[0]).concat_tree(array_to_tree(arr[1]))


def print_dict(d):
    for k in d:
        print(k, d[k])

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    line = literal_eval(lines[0])
    print("line:", line)
    tree = array_to_tree(line)
    tree.display()
    tree.in_order()
    print(tree.get_pair_of_lowest_level())

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
