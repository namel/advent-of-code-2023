NUM_STEPS = 26501365
NEXT_OF = { 'N': (0, -1), 'W': (-1, 0), 'S': (0, 1), 'E': (1, 0) }
positions = set()

def explore_steps(positions):
    next_set = set()
    for p in positions:
        for direction in ['N', 'W', 'S', 'E']:
            next_pos = (NEXT_OF[direction][0] + p[0], NEXT_OF[direction][1] + p[1])
            if next_pos[0] < 0 or next_pos[0] == len(ll[0]) or next_pos[1] < 0 or next_pos[1] == len(ll):
                continue
            if ll[next_pos[1]][next_pos[0]] != '#':
                next_set.add(next_pos)
    return next_set


with open("21/input.txt") as input:
    ll = [l.strip() for l in input]
    start_row = [(row, l) for row, l in enumerate(ll) if 'S' in l][0]
    positions.add((start_row[1].index('S'), start_row[0]))

    for step in range(NUM_STEPS):
        new_positions = explore_steps(positions)
        # print("at step {} positions list is {}".format(step, new_positions))
        positions = new_positions
    
    print("total positions = ", len(positions))

