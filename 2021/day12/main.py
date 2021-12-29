# Classes Auxiliares ----------------------------------------------------------


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        if(v1 == 'start' or v2 == 'end'):
            self.graph[v1].append(v2)
        elif(v2 == 'start' or v1 == 'end'):
            self.graph[v2].append(v1)
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def print_graph(self):
        for key in self.graph:
            print(key, ':', self.graph[key])

    def get_all_paths_between_start_and_end(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for vertex in self.graph[start]:
            if vertex not in path or check_uppercase(vertex):
                newpaths = self.get_all_paths_between_start_and_end(
                    vertex, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def get_all_paths_between_start_and_end_special(self, start, end, special, num_left, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for vertex in self.graph[start]:
            if vertex not in path or check_uppercase(vertex) or (vertex == special and num_left > 0):
                num_atual = num_left
                if(vertex == special):
                    num_left -= 1
                newpaths = self.get_all_paths_between_start_and_end_special(
                    vertex, end, special, num_left, path)
                num_left = num_atual
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def get_lowercases_letters(self):
        return [
            i for i in self.graph.keys()
            if check_uppercase(i) == False and
            i != 'start' and i != 'end'
        ]

# Funções Auxiliares ----------------------------------------------------------


def check_uppercase(word):
    return word[0].isupper()


def fill_graph(lines):
    g = Graph()
    for i in lines:
        source = i.split('-')[0]
        destiny = i.split('-')[1]
        g.add_vertex(source)
        g.add_vertex(destiny)
        g.add_edge(source, destiny)
    return g


def remove_repeated_lists_in_list_of_lists(l):
    return [list(x) for x in set(tuple(x) for x in l)]

# Part 1 ----------------------------------------------------------------------


def part1(lines):
    g = fill_graph(lines)
    res = g.get_all_paths_between_start_and_end('start', 'end')
    return len(res)

# Part 2 ----------------------------------------------------------------------


def part2(lines):
    g = fill_graph(lines)
    lowerscases = g.get_lowercases_letters()
    all_paths = []
    for i in lowerscases:
        paths = g.get_all_paths_between_start_and_end_special(
            'start', 'end', i, 2)
        for j in paths:
            all_paths.append(j)

    return len(remove_repeated_lists_in_list_of_lists(all_paths))


def main():
    filename = 'input.txt'
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
