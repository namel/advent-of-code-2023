import sys
from functools import reduce

sys.setrecursionlimit(100000)
map = []
lines = []

# for each mirror/splitter type, given the direction it was previously headed,
# describe how the beam continues (give direction and position change)
MIRROR_OPS = {
    '/': { 'E': ['N'], 'W': ['S'], 'N': ['E'], 'S': ['W'] },
    '\\': { 'E': ['S'], 'W': ['N'], 'N': ['W'], 'S': ['E'] },
    '|': { 'E': ['N', 'S'], 'W': ['N', 'S'], 'N': ['N'], 'S': ['S'] },
    '-': { 'E': ['E'], 'W': ['W'], 'N': ['W', 'E'], 'S': ['W','E'] },
    '.': { 'E': ['E'], 'W': ['W'], 'N': ['N'], 'S': ['S'] }
}

# indicate how a direction affects aposition's (x,y)
POS_MOVE = { 'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}

def propagate_beam(pos, dir):
    global map
    item = lines[pos[1]][pos[0]]

    if dir in map[pos[1]][pos[0]]:
        return
    map[pos[1]][pos[0]].add(dir)

    next_directions = MIRROR_OPS[item][dir]
    for next_dir in next_directions:
        next_pos = (pos[0] + POS_MOVE[next_dir][0], pos[1] + POS_MOVE[next_dir][1])
        if next_pos[0] >= 0 and next_pos[0] < len(map[0]) and next_pos[1] >= 0 and next_pos[1] < len(map):
            propagate_beam(next_pos, next_dir)

def start_beam(pos, dir):
    global map, most_energies
    map = [[set() for x in range(len(lines[0]))] for y in range(len(lines))]
    propagate_beam(pos, dir)
    energies = [reduce(lambda acc, x: acc + int(len(x) > 0), map_row, 0) for map_row in map]
    total_energies = reduce(lambda acc, x: acc+x, energies, 0)
    print("pos[{}] dir[{}] has total energies: {}".format(pos, dir, total_energies))
    if total_energies > most_energies:
        most_energies = total_energies


most_energies = 0
with open("16/input.txt", "r") as input:
    lines = [l.strip() for l in input]

    for i in range(len(lines[0])):
        start_beam((i,0), "S")
    for i in range(len(lines[0])):
        start_beam((i,len(lines) - 1), "N")
    for i in range(len(lines)):
        start_beam((0, i), "E")
    for i in range(len(lines)):
        start_beam((len(lines[0])- 1, i), "W")

    print("highest energy sum = ", most_energies)
