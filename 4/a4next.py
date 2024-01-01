



def get_hits(line):
    hits = 0
    lists = line.split(":")[1].split("|")
    nums1 = lists[0].lstrip().rstrip().split(" ")
    nums2 = lists[1].lstrip().rstrip().split(" ")
    nums1_int = [int(x) for x in nums1 if x != '']
    nums2_int = [int(x) for x in nums2 if x != '']
    for i in nums2_int:
        if i in nums1_int:
            hits += 1
    return hits

total = 0
card_num = 1
cards_won = [1] * 300
with open("4/input.txt", "r") as input:
    for l in input:
        copies_of_this_card = cards_won[card_num]
        hits = get_hits(l)
        print("card {} has {} hits. I hold {} copies of this card".format(card_num, hits, copies_of_this_card))
        for i in range(1, hits + 1):
            cards_won[card_num + i] += copies_of_this_card
        total += copies_of_this_card
        card_num += 1
print(total)
