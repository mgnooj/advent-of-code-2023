with open("day5.txt") as f:
    lines = f.read()

def part1():
    seeds, soil_map, fertilizer_map, water_map, light_map, temp_map, humid_map, location_map = [x for x in lines.split("\n\n") if x]
    seeds = [int(x) for x in seeds.split("seeds: ")[1].split()]
    soil_map = [x for x in soil_map.split("\n") if x and "map:" not in x]
    fertilizer_map = [x for x in fertilizer_map.split("\n") if x and "map:" not in x]
    water_map = [x for x in water_map.split("\n") if x and "map:" not in x]
    light_map = [x for x in light_map.split("\n") if x and "map:" not in x]
    temp_map = [x for x in temp_map.split("\n") if x and "map:" not in x]
    humid_map = [x for x in humid_map.split("\n") if x and "map:" not in x]
    location_map = [x for x in location_map.split("\n") if x and "map:" not in x]
    lowest_location = None
    for seed in seeds:
        soil_loc = interpret_map(soil_map, seed)
        fertilizer_loc = interpret_map(fertilizer_map, soil_loc)
        water_loc = interpret_map(water_map, fertilizer_loc)
        light_loc = interpret_map(light_map, water_loc)
        temp_loc = interpret_map(temp_map, light_loc)
        humid_loc = interpret_map(humid_map, temp_loc)
        location = interpret_map(location_map, humid_loc)
        if lowest_location == None or lowest_location > location:
            lowest_location = location
    return lowest_location

def interpret_map(map_intervals: [str], input: int) -> int:
    ranges = []
    for interval in map_intervals:
        destination_idx, source_idx, length = [int(x) for x in interval.split()]
        source_range = {"range": range(source_idx, source_idx + length), "source_idx": source_idx, "dest_idx": destination_idx}
        ranges.append(source_range)
    for interval in ranges:
        if input in interval.get("range"):
            offset = input - interval.get("source_idx")
            return interval.get("dest_idx") + offset
    return input

def apply_map(map_rules, seeds):
    new_values = []
    while seeds:
        current_range = seeds.pop()
        divided = False
        for rule in map_rules:
            if overlap(current_range, rule["input"]):
                divided = True
                head = (current_range[0], rule["input"][0])
                tail = (rule["input"][1], current_range[1])
                overlapping_range = intersection(current_range, rule["input"])
                new_range = (overlapping_range[0] + rule["offset"], overlapping_range[1] + rule["offset"])
                new_values.append(new_range)
                if head[0] < head[1]:
                    seeds.append(head)
                if tail[0] < tail[1]:
                    seeds.append(tail)
                break
        if not divided:
            new_values.append(current_range)
    return new_values

def overlap(range1, range2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return range1[1] > range2[0] and range2[1] > range1[0]

def intersection(range1, range2):
    range_start = max(range1[0], range2[0])
    range_end = min(range1[1], range2[1])
    return (range_start, range_end)

def part2():
    seeds, soil_map, fertilizer_map, water_map, light_map, temp_map, humid_map, location_map = [x for x in lines.split("\n\n") if x]
    seeds = [int(x) for x in seeds.split("seeds: ")[1].split()]
    seed_ranges = []
    while seeds:
        range_start = seeds.pop(0)
        range_length = seeds.pop(0)
        seed_ranges.append((range_start, range_start + range_length))
    soil_map = build_map(soil_map)
    fertilizer_map = build_map(fertilizer_map)
    water_map = build_map(water_map)
    light_map = build_map(light_map)
    temp_map = build_map(temp_map)
    humid_map = build_map(humid_map)
    location_map = build_map(location_map)
    soil_locs = apply_map(soil_map, seed_ranges)
    fert_locs = apply_map(fertilizer_map, soil_locs)
    water_locs = apply_map(water_map, fert_locs)
    light_locs = apply_map(light_map, water_locs)
    temp_locs = apply_map(temp_map, light_locs)
    humid_locs = apply_map(humid_map, temp_locs)
    locs = apply_map(location_map, humid_locs)
    return min([loc_range[0] for loc_range in locs])

def build_map(map_string: str):
    map_intervals = [x for x in map_string.split("\n") if x and "map:" not in x]
    ranges = []
    for interval in map_intervals:
        destination_idx, source_idx, length = [int(x) for x in interval.split()]
        source_range = {"input": (source_idx, source_idx + length), "offset": destination_idx - source_idx}
        ranges.append(source_range)
    return ranges
