data  = open("data/7").read().splitlines()

hands = [list(x[:5]) for x in data]
bids  = [int(x[5:]) for x in data]

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hand_ratings = []

for hand, bid in zip(hands, bids):
    print(hand)

    hand_copy = [x for x in hand]

    counts = []

    jokers = 0

    while hand_copy:
        pop_card = hand_copy[0]
        occurences = 0

        while pop_card in hand_copy:
            hand_copy.remove(pop_card)
            occurences += 1

        if pop_card == "J":
            jokers = occurences
        else:
            counts.append(occurences)

    if counts:
        counts[counts.index(max(counts))] += jokers
    else:
        counts = [5]

    if counts == [5]:
        score = 6
    elif 4 in counts:
        score = 5
    elif 3 in counts and len(counts) == 2:
        score = 4
    elif 3 in counts and len(counts) == 3:
        score = 3
    elif 2 in counts and len(counts) == 3:
        score = 2
    elif 2 in counts and len(counts) == 4:
        score = 1
    else:
        score = 0

    letter_score = 0
    for i, c in enumerate(hand[::-1]):
        letter_score += cards.index(c) * len(cards) ** i

    total_score = score * len(cards) ** len(hand) + letter_score

    print(total_score)

    hand_ratings.append((total_score, bid))

hand_ratings.sort()

print(hand_ratings)

s = 0

for i, bid in enumerate([x[1] for x in hand_ratings]):
    s += (i + 1) * bid

print(s)
