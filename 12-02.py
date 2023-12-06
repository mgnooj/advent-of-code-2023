file = "day2.txt"
with open(file) as f:
    text = f.read()
input = [x for x in text.split('\n') if x != ""]

def part1():
    game_ids = []
    for game in input:
        id, list_of_rounds = game.split(":")
        id = int(id.replace("Game ", ""))
        rounds = list_of_rounds.split(";")
        valid = True
        for round in rounds:
            cubes = round.split(",")
            for cube in cubes:
                if "green" in cube:
                    num = int(cube.split("green")[0].strip())
                    if num > 13:
                        valid = False
                if "red" in cube:
                    num = int(cube.split("red")[0].strip())
                    if num > 12:
                        valid = False
                if "blue" in cube:
                    num = int(cube.split("blue")[0].strip())
                    if num > 14:
                        valid = False
        if valid:
            game_ids.append(id)
    return sum(game_ids)

def part2():
    game_values = []
    for game in input:
        id, list_of_rounds = game.split(":")
        id = int(id.replace("Game ", ""))
        rounds = list_of_rounds.split(";")
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for round in rounds:
            cubes = round.split(",")
            for cube in cubes:
                for color in ("green", "red", "blue"):
                    if color in cube:
                        num = int(cube.split(color)[0].strip())
                        if num > max_cubes.get(color):
                            max_cubes[color] = num
        power_of_cubes = max_cubes.get("green") * max_cubes.get("red") * max_cubes.get("blue")
        game_values.append(power_of_cubes)
    return sum(game_values)
