POS_MOVE = { 'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
POS_NEXT = { 'N': ['W', 'N', 'E'], 'W': ['S', 'W', 'N'], 'S': ['E', 'S', 'W'], 'E': ['N', 'E', 'S'], '*': ['E', 'S'] }
BLOCKED = { 'N': 'v', 'W': '>', 'S': '^', 'E': '<' }

full_walk = {}

with open("23/input.txt") as input:
    ll = [l.strip() for l in input]
    last_x, last_y = len(ll[0]), len(ll)
    start_pos, end_pos = (1,1), (last_x - 2, last_y - 2)

def get_next_pos_list(pos_dir, trace):
    pos, dir = pos_dir
    nexts = [((POS_MOVE[n][0] + pos[0], POS_MOVE[n][1] + pos[1]), n) for n in POS_NEXT[dir]]
    return [n for n in nexts if ll[n[0][1]][n[0][0]] != '#' and (pos not in trace)]

def walk(pos_dir, trace, dist):
    next_pos_list = [pos_dir]
    while len(next_pos_list) == 1:
        pos_dir = next_pos_list[0]
        if pos_dir[0] == end_pos:
            full_walk[str(trace + [pos_dir[0]])] = dist
            return
        if BLOCKED[pos_dir[1]] == ll[pos_dir[0][1]][pos_dir[0][0]]:
            return
        dist += 1
        next_pos_list = get_next_pos_list(pos_dir, trace)
    for next_pos, next_dir in next_pos_list:
        walk((next_pos, next_dir), trace + [pos_dir[0]], dist)


walk((start_pos, 'S'), [], 2)
print("longest walk of {} steps".format(max(full_walk.values())))
# for p, d in full_walk.items():
    # print("{}: {}".format(d, p))


