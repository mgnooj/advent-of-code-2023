import numpy

with open("day8.txt") as f:
    lines = f.read()

input = [x for x in lines.split("\n") if x]
directions = input[0]
nodes = {}
for line in input[1:]:
    key, neighbors = line.split(" = ")
    neighbor1, neighbor2 = neighbors.replace("(", "").replace(")", "").split(", ")
    nodes[key] = {"L": neighbor1, "R": neighbor2}

def part1():
    current_key = "AAA"
    rounds = 0
    directions_idx = 0
    while directions:
        if current_key == "ZZZ":
            return rounds
        rounds += 1
        current_direction = directions[directions_idx]
        directions_idx = 0 if directions_idx + 1 == len(directions) else directions_idx + 1
        current_key = nodes[current_key][current_direction]

def part2():
    current_keys = [key for key in nodes if key[-1] == "A"]
    min_rounds = []
    for key in current_keys:
        rounds = 0
        directions_idx = 0
        while directions:
            if key[-1] == "Z":
                min_rounds.append(rounds)
                break
            rounds += 1
            current_direction = directions[directions_idx]
            directions_idx = 0 if directions_idx + 1 == len(directions) else directions_idx + 1
            key = nodes[key][current_direction]
    return numpy.lcm.reduce(min_rounds)
