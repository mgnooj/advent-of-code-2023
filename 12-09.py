with open("day9.txt") as f:
    lines = f.read()

input = [x for x in lines.split("\n") if x]
input = [x.split() for x in input]
input = [[val for val in map(lambda x: int(x), row)] for row in input]

next_level = lambda input: [y - x for (x, y) in pairwise(input)]
pairwise = lambda input: [(input[x], input[x + 1]) for x in range(len(input) - 1)]

def next_integer(sequence):
    vector = list(sequence)
    tree = []
    while vector:
        tree.append(vector)
        if all([x == 0 for x in vector]):
            break
        vector = next_level(vector)
    tree.reverse()
    for level in range(len(tree) - 1):
        tree[level + 1].append(tree[level][-1] + tree[level + 1][-1])
    return tree[-1][-1]

def part1():
    values = [x for x in map(next_integer, input)]
    return sum(values)

def previous_integer(sequence):
    vector = list(sequence)
    tree = []
    while vector:
        tree.append(vector)
        if all([x == 0 for x in vector]):
            break
        vector = next_level(vector)
    tree.reverse()
    for level in range(len(tree) - 1):
        tree[level + 1].insert(0, tree[level + 1][0] - tree[level][0])
    for level in tree:
        print(level)
    return tree[-1][0]

def part2():
    values = [x for x in map(previous_integer, input)]
    return sum(values)
