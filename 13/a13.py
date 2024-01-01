def check_reflection(map, loc, score_mult):
    global total
    up = loc - 1
    down = loc + 2
    while up >= 0 and down < len(map):
        if map[up] != map[down]:
            return
        up -= 1
        down += 1
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
            if m[i] == m[i+1]:
                check_reflection(m, i, 100)
    for t in t_maps:
        for i in range(len(t) - 1):
            if t[i] == t[i+1]:
                check_reflection(t, i, 1)

    print("total = ", total)

    
    


