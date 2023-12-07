with open("day6.txt") as f:
    lines = f.read()

input = [x for x in lines.split("\n") if x]

def part1():
    times = [int(x) for x in input[0].split()[1:]]
    distances = [int(x) for x in input[1].split()[1:]]
    races = [race for race in zip(times, distances)]
    margin_of_error = []
    for race in races:
        record_beating_strategies = 0
        time, record = race
        for charge_time in range(1, time):
            distance = (time - charge_time) * charge_time
            if distance > record:
                record_beating_strategies += 1
        margin_of_error.append(record_beating_strategies)
    product = 1
    for x in margin_of_error:
        product *= x
    return product

def part2():
    times = [x for x in input[0].split()[1:]]
    time = int("".join(times))
    distances = [x for x in input[1].split()[1:]]
    record = int("".join(distances))
    record_beating_strategies = 0
    for charge_time in range(1, time):
        distance = (time - charge_time) * charge_time
        if distance > record:
            record_beating_strategies += 1
    return record_beating_strategies
