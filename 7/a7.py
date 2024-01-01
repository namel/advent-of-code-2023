import functools

hands = []

CARD_TO_INT = { "T":10, "J":11, "Q":12, "K": 13, "A": 14}

def card_to_int(c):
    return int(CARD_TO_INT.get(c,c))

def calc_score(hand):
    counts = {}
    for c in hand:
        counts[c] = counts.get(c, 0) + 1

    items = list(counts.items())
    items.sort(key = lambda x: x[1], reverse=True)

    # encoding is
    # types: 7 => 5kind; 6 => 4kind; 5 => 3+2; 4 => 3; 3 => 2+2; 2 => 2; 1 => 1
    cardHi = card_to_int(items[0][0])
    cardLo = 0
    if len(items) > 1:
        cardLo = card_to_int(items[1][0])
    if items[0][1] == 5:
        type = 7
    elif items[0][1] == 4:
        type = 6
    elif items[0][1] == 3 and items[1][1] == 2:
        type = 5
    elif items[0][1] == 3:
        type = 4
    elif items[0][1] == 2 and items[1][1] ==2:
        type = 3
    elif items[0][1] == 2:
        type = 2
    else:
        type = 1   
 

    return "{}{}{}{}{}{}".format(str(type), 
                                 str(card_to_int(hand[0])).zfill(2), 
                                 str(card_to_int(hand[1])).zfill(2),
                                 str(card_to_int(hand[2])).zfill(2),
                                 str(card_to_int(hand[3])).zfill(2),
                                 str(card_to_int(hand[4])).zfill(2))



with open("7/input.txt", "r") as input:
    for l in input:
        (hand, bid) = l.strip().split(" ")
        hands.append({ "hand": hand, "bid":int(bid), "score": calc_score(hand)})
    hands.sort(key = lambda x: x["score"])
    score = 0
    i = 1
    for h in hands:
        score += h["bid"] * i
        i += 1
    print(score)


