POS_MOVE = { 'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
POS_NEXT = { 'N': ['W', 'N', 'E'], 'W': ['S', 'W', 'N'], 'S': ['E', 'S', 'W'], 'E': ['N', 'E', 'S'], '*': ['E', 'S'] }
BLOCKED = { 'N': 'v', 'W': '>', 'S': '^', 'E': '<' }

known_paths, longest_walk = {}, 0

with open("23/input.txt") as input:
    ll = [l.strip() for l in input]
    last_x, last_y = len(ll[0]), len(ll)
    start_pos, end_pos = (1,1), (last_x - 2, last_y - 2)

def get_next_pos_list(pos_dir):
    pos, dir = pos_dir
    nexts = [((POS_MOVE[n][0] + pos[0], POS_MOVE[n][1] + pos[1]), n) for n in POS_NEXT[dir]]
    return [n for n in nexts if ll[n[0][1]][n[0][0]] != '#']

def advance_to_junction(pos_dir):
    if pos_dir in known_paths:  # memoized advance
        return known_paths[pos_dir]

    dist = 0
    next_pos_list = [pos_dir]
    while len(next_pos_list) == 1:
        next_pos_dir = next_pos_list[0]
        if next_pos_dir[0] == end_pos:
            next_pos_list = []
            break
        dist += 1
        next_pos_list = get_next_pos_list(next_pos_dir)
    known_paths[pos_dir] = (next_pos_dir, next_pos_list, dist)
    return (next_pos_dir, next_pos_list, dist)

def walk(pos_dir, trace, dist):
    global longest_walk
    next_junction, next_pos_list, delta = advance_to_junction(pos_dir)
    if next_junction[0] == end_pos:
        if dist+delta > longest_walk:
            print("{} through path {}".format(dist + delta, str(trace)))
            longest_walk = dist+delta
        return
    if next_junction[0] in trace:
        return
    for next_pos, next_dir in next_pos_list:
        walk((next_pos, next_dir), trace + [next_junction[0]], dist + delta)

walk((start_pos, 'S'), [], 2)
