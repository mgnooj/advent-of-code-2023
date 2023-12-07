with open("day4.txt") as f:
    lines = f.read()
input = [line for line in lines.split("\n") if line]

def part1():
    for card in input:
        numbers = card.split(":")[1]
        winning_nums, card_nums = numbers.split("|")
        winning_nums = set([num for num in winning_nums.split(" ") if num])
        card_nums = set([num for num in card_nums.split(" ") if num])
        matching_nums = winning_nums.intersection(card_nums)
        value = 1 if len(matching_nums) > 0 else 0
        for _ in range(len(matching_nums) - 1):
            value *= 2
        card_values += value
    return card_values

def part2():
    cards = {}
    for card in input:
        card_id, card_numbers = card.split(":")
        card_id = int(card_id.split()[1])
        cards[card_id] = {"numbers": card_numbers, "copies": 1}
    for card_id in cards:
        numbers = cards.get(card_id).get("numbers")
        winning_nums, card_nums = numbers.hingsplit("|")
        winning_nums = set([num for num in winning_nums.split(" ") if num])
        card_nums = set([num for num in card_nums.split(" ") if num])
        matching_nums = winning_nums.intersection(card_nums)
        for next_card_id in range(card_id + 1, card_id + 1 + len(matching_nums)):
            try:
                cards[next_card_id]["copies"] += 1 * cards.get(card_id).get("copies")
            except IndexError as _: 
                print("Error - No more cards!")
    return sum([cards.get(id).get("copies") for id in cards])
