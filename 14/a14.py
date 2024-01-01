import functools

with open("14/input.txt", "r") as input:
    lines = [l.strip() for l in input]
    columns = ["".join([l[i] for l in lines]) for i in range(len(lines[0]))]


    packed_col = []
    for colid, col in enumerate(columns):
        lowest_stop = 0
        packed_col.append(['.'] * len(columns[0]))
        for pos, c in enumerate(col):
            if c == '#':
                lowest_stop = pos + 1
            elif c == 'O':
                packed_col[-1][lowest_stop] = 'O'
                lowest_stop += 1
    
    print(packed_col)
    total = 0 
    for col in packed_col:
        score = 0
        for cid, c in enumerate(col):
            if c == 'O':
                score += len(col) - cid
        # print("col score ", score)
        total += score
    print("total score ", total)


