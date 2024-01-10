from collections import deque
from datetime import datetime
from functools import cache

NUM_STEPS = 26501365
# NUM_STEPS = 5
NEXT_OF = [(0, -1), (-1, 0), (0, 1), (1, 0)]


@cache
def orig_next(pos):
    return [(pos[0] + n[0], pos[1] + n[1]) for n in NEXT_OF if ll[(pos[1] + n[1]) % col_len][(pos[0] + n[0]) % row_len] != '#']

def get_next(pos):
    offx, offy = pos[0] // row_len, pos[1] // col_len
    return [(offx + x, offy + y) for x,y in orig_next((pos[0] % row_len, pos[1] % col_len))]

q = deque()
with open("21/input.txt") as input:
    ll = [l.strip() for l in input]
    row_len, col_len = len(ll[0]), len(ll)
    start_row = [(row, l) for row, l in enumerate(ll) if 'S' in l][0]
    first_steps = get_next((start_row[1].index('S'), start_row[0]))
    q.extend([(p, 1) for p in first_steps])
    total = 0

visited = set()
reached = set()
while len(q) > 0:
    pos, dist = q.popleft()
    double_step = set()
    for next_pos in get_next(pos):
        for next_next_pos in get_next(next_pos):
            double_step.add(next_next_pos)
    new_entries = double_step - visited
    if len(new_entries) == 0:
         continue
    visited.update(new_entries)
    total += len(new_entries)
    if dist % 1000 == 1 and dist // 1000  not in reached:
        print("[{}] reached distance {}".format(datetime.now(), dist // 1000))
        reached.add(dist // 1000)
    if dist + 2 < NUM_STEPS:
        q.extend([(p, dist + 2) for p in new_entries])

print(total)
