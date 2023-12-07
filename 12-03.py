with open("day3.txt") as f:
    lines = f.read()

input = [line for line in lines.split("\n") if line]
arr = [[x for x in line] for line in input]
digits = [str(x) for x in range(10)]

def part1():
    numbers = []
    symbols = []
    for row_idx, row in enumerate(arr):
        num = ""
        num_coords = []
        for col_idx, cell in enumerate(row):
            if cell == ".":
                if num:
                    numbers.append((int(num), num_coords))
                    num = ""
                    num_coords = []
            else:
                if cell in digits:
                    num += cell
                    num_coords.append((row_idx, col_idx))
                else:
                    if num:
                        numbers.append((int(num), num_coords))
                        num = ""
                        num_coords = []
                    symbols.append((row_idx, col_idx))
        if num:
            numbers.append((int(num), num_coords))
    valid_numbers = []
    for number, coords in numbers:
        all_neighbors = set(point for neighbors in map(valid_neighbors, coords) for point in neighbors)
        if all_neighbors.intersection(set(symbols)):
            valid_numbers.append(number)
    return sum(valid_numbers)

def part2():
    numbers = []
    symbols = []
    for row_idx, row in enumerate(arr):
        num = ""
        num_coords = []
        for col_idx, cell in enumerate(row):
            if cell == ".":
                if num:
                    numbers.append((int(num), num_coords))
                    num = ""
                    num_coords = []
            else:
                if cell in digits:
                    num += cell
                    num_coords.append((row_idx, col_idx))
                if cell == "*":
                    if num:
                        numbers.append((int(num), num_coords))
                        num = ""
                        num_coords = []
                    symbols.append((row_idx, col_idx))
        if num:
            numbers.append((int(num), num_coords))
    gear_ratio_sum = 0
    for gear in symbols:
        neighbors = []
        valid_coords = set(valid_neighbors(gear))
        for number, coords in numbers:
            if valid_coords.intersection(set(coords)):
                neighbors.append(number)
        if len(neighbors) == 2:
            gear_ratio_sum += neighbors[0] * neighbors[1]
    return gear_ratio_sum

def valid_neighbors(coords):
    x, y = coords
    return [(x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1), (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)]