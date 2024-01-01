
def error_count(l1,l2):
    return len([True for pos in range(len(l1)) if l1[pos] != l2[pos]])

def check_reflection(map, loc, score_mult):
    global total
    up, down, errors = loc, loc + 1, 0
    while up >= 0 and down < len(map):
        errors += error_count(map[up], map[down])
        if errors > 1:
            return
        up -= 1
        down += 1
    if errors == 0:
        return
    print("found score = ", (loc + 1)*score_mult)
    total += (loc + 1) * score_mult
    return

total = 0
with open("13/input.txt", "r") as input:
    lines = [l.strip() for l in input]
    maps = [[]]
    for l in lines:
        if len(l) == 0:
            maps.append([])
        else:
            maps[-1].append(l)

    t_maps = []
    for m in maps:
        trans_map = [""] * len(m[0])
        for i in range(len(m[0])):
            for j in m:
                trans_map[i] += j[i]
        t_maps.append(trans_map)

    for m in maps:
        for i in range(len(m) - 1):
            check_reflection(m, i, 100)
    for t in t_maps:
        for i in range(len(t) - 1):
            check_reflection(t, i, 1)

    print("total = ", total)

    
    


