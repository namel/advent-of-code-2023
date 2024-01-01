import functools

POS_MOVE = { 'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
SIG_MAP = {
    "OUT": { (1, 1, 1): "IN", (0, 1, 1): "OUTR", (1, 1, 0): "OUTL" },
    "IN": { (1, 1, 1): "OUT", (0, 1, 1): "INR", (1, 1, 0): "INL" },
    "OUTR": { (0, 1, 1): "OUT", (1, 1, 0): "IN", (0, 1, 0): "OUTR" },
    "OUTL": { (0, 1, 1): "IN", (1, 1, 0): "OUT", (0, 1, 0): "OUTL" },
    "INR": { (0, 1, 1): "IN", (1, 1, 0): "OUT", (0, 1, 0): "INR" },
    "INL": { (0, 1, 1): "OUT", (1, 1, 0): "IN", (0, 1, 0): "INL" }
}
def move_pos(pos, dir):
    return (pos[0] + POS_MOVE[dir][0], pos[1] + POS_MOVE[dir][1])

def advance(pos, dir, dist):
    moves = []
    for i in range(dist):
        pos = move_pos(pos, dir)
        moves.append(pos)
    return moves

def map_set(pos, val):
    global map
    map[pos[1] + offset[1]][pos[0] + offset[0]] = val

def show_map():
    for row in map:
        print("".join([str(c) for c in row]))

def row_sig(row, i):
    if i == 0:
        return (0, row[0], row[1])
    if i == len(row) - 1:
        return (row[-2], row[-1], 0 )
    return (row[i-1], row[i], row[i+1])

with open("18/input.txt", "r") as input:
    moves = []
    map = [[]]

    # collect lines
    for line in input:
        l = line.strip()
        dir, dist, color = tuple(line.split(' '))
        moves.append((dir, int(dist), color))
    
    # get top-right corner to build an empty map
    pos, min_pos, max_pos=(0,0), (0,0), (0,0)
    for m in moves:
        dir, dist, color = m
        positions = advance(pos, dir, dist)
        max_pos = functools.reduce(lambda acc, x: (max(acc[0], pos[0]), max(acc[1], pos[1])), positions, max_pos)
        min_pos = functools.reduce(lambda acc, x: (min(acc[0], pos[0]), min(acc[1], pos[1])), positions, min_pos)
        pos = positions[-1]
    
    offset = (abs(min_pos[0]), abs(min_pos[1]))
    map = [[0 for j in range(max_pos[0] - min_pos[0] + 1)] for i in range(max_pos[1] - min_pos[1] + 1)]

    # build the map
    pos=(0,0)
    map_set(pos, 1)
    for m in moves:
        dir, dist, color = m
        positions = advance(pos, dir, dist)
        for p in positions:
            map_set(p, 1)
        pos = positions[-1]
    show_map()

    # fill the inside
    # count the number of walls traversed above you, for this current column:
    #
    # if above had ### then you have one wall above -> flip inside/outside
    # if above had 0## then you are on the edge of a wall that arrived from the right -> left edge
    #    encounters 0##  keeps your state, encounter ##0 flips, encounter 0#0 leaves you on left edge 
    # if above had ##0 then you are on the edge of a wall that arrived from the left -> right edge
    #    encounters 0## flips, encounter ##0 keeps your state, encounter 0#0 leaves you on right edge 
    col_desc = ["OUT" for c in range(len(map[0]))]
    for j, row in enumerate(map):
        orig_row = row[:]
        for i, state in enumerate(row):
            if state == 0:
                if col_desc[i] == "IN":
                    map[j][i] = 1
            else:
                col_desc[i] = SIG_MAP[col_desc[i]][row_sig(orig_row, i)]

    print("\n\nfilled map")
    show_map()
    print("total space = ", sum([sum(row) for row in map]))
