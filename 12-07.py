with open("day7.txt") as f:
    lines = f.read()

input = [x for x in lines.split("\n") if x]

def part1():
    card_faces = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    hand_dict = {}
    for hand in input:
        cards, bid = hand.split()
        cards = [c for c in cards]
        bid = int(bid)
        hand_type = eval_hand(cards)
        _ = hand_dict.setdefault(hand_type, [])
        hand_dict[hand_type].append((cards, bid))
    for hand_type in hand_dict:
        hand_dict[hand_type].sort(key=lambda x: [val for val in map(lambda y: card_faces.index(y), x[0])]) 
    all_hands = hand_dict["Five of a kind"] + hand_dict["Four of a kind"] + hand_dict["Full house"] + hand_dict["Three of a kind"] + hand_dict["Two pair"] + hand_dict["One pair"] + hand_dict["High card"]
    all_hands.reverse()
    final_rank = [pair for pair in zip([x for x in range(1, len(all_hands) + 1)], [hand[1] for hand in all_hands])]
    winnings = [val for val in map(lambda x: x[0] * x[1], final_rank)]
    return sum(winnings)

def part2():
    card_faces = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    hand_dict = {}
    for hand in input:
        cards, bid = hand.split()
        cards = [c for c in cards]
        bid = int(bid)
        hand_type = eval_hand_with_joker(cards)
        _ = hand_dict.setdefault(hand_type, [])
        hand_dict[hand_type].append((cards, bid))
    for hand_type in hand_dict:
        hand_dict[hand_type].sort(key=lambda x: [val for val in map(lambda y: card_faces.index(y), x[0])]) 
    all_hands = hand_dict["Five of a kind"] + hand_dict["Four of a kind"] + hand_dict["Full house"] + hand_dict["Three of a kind"] + hand_dict["Two pair"] + hand_dict["One pair"] + hand_dict["High card"]
    all_hands.reverse()
    final_rank = [pair for pair in zip([x for x in range(1, len(all_hands) + 1)], [hand[1] for hand in all_hands])]
    winnings = [val for val in map(lambda x: x[0] * x[1], final_rank)]
    return sum(winnings)

def eval_hand(hand):
    if len(set(hand)) == 1:
        return "Five of a kind"
    if len(set(hand)) == 2:
        for card in hand[:2]:
            if hand.count(card) == 4:
                return "Four of a kind"
        return "Full house"
    if len(set(hand)) == 3:
        for card in hand[:3]:
            if hand.count(card) == 3:
                return "Three of a kind"
        return "Two pair"
    if len(set(hand)) == 4:
        return "One pair"
    return "High card"

def eval_hand_with_joker(hand):
    if len(set(hand)) == 1:
        return "Five of a kind"
    if len(set(hand)) == 2:
        if "J" in set(hand):
            return "Five of a kind"
        for card in hand[:2]:
            if hand.count(card) == 4:
                return "Four of a kind"
        return "Full house"
    if len(set(hand)) == 3:
        if "J" in set(hand):
            hand_minus_joker = [card for card in set(hand) if card != "J"]
            if hand.count(hand_minus_joker[0]) == 2 and hand.count(hand_minus_joker[1]) == 2:
                return "Full house"
            return "Four of a kind"
        for card in hand[:3]:
            if hand.count(card) == 3:
                return "Three of a kind"
        return "Two pair"
    if len(set(hand)) == 4:
        if "J" in set(hand):
            return "Three of a kind"
        return "One pair"
    if "J" in set(hand):
        return "One pair"
    return "High card"
