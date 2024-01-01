from collections import deque


POS_MOVE = { 'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
POS_NEXT = { 'N': ['W', 'N', 'E'], 'W': ['S', 'W', 'N'], 'S': ['E', 'S', 'W'], 'E': ['N', 'E', 'S'], '*': ['E', 'S'] }


def move_pos(pos, dir):
    return (pos[0] + POS_MOVE[dir][0], pos[1] + POS_MOVE[dir][1])

def get_heat(pos):
    return int(lines[pos[1]][pos[0]])

def was_reached(next_pos, next_dir, next_linear_repeat, next_energy):
    pos_info = map[next_pos[1]][next_pos[0]]
    entry = (next_dir, next_linear_repeat)
    if (entry not in pos_info) or pos_info[entry] > next_energy:
        pos_info[entry] = next_energy
        return False
    return True

with open("17/input.txt", "r") as input:
    lines = [l.strip() for l in input]
    map = [[{} for i in range(len(lines[0]))] for j in range(len(lines))]
    the_end = (len(lines[0]) - 1, len(lines) - 1)
    counter = 0

    # each element contains (pos(x,y), direction, energy_acc, linear_repeat)
    fifo = deque()
    fifo.append(((0,0), "*", 0, 0))

    while len(fifo) > 0:
        pos, dir, energy_acc, linear_repeat = fifo.popleft()
        for next_pos, next_dir in [(move_pos(pos, dir2), dir2) for i, dir2 in enumerate(POS_NEXT[dir])]:

            # check out of bounds
            if next_pos[0] < 0 or next_pos[0] >= len(map[0]) or next_pos[1] < 0 or next_pos[1] >= len(map):
                continue

            # check linear repeat limit
            next_linear_repeat = linear_repeat + 1 if next_dir == dir else 0
            if next_linear_repeat == 3:
                continue

            # check if this case was visited
            next_energy_acc = energy_acc + get_heat(next_pos)
            if was_reached(next_pos, next_dir, next_linear_repeat, next_energy_acc):
                continue

            # check if we reached the end
            if next_pos == the_end:
                print("found a path to the end with energy {}".format(next_energy_acc))

            fifo.append((next_pos, next_dir, next_energy_acc, next_linear_repeat))
    print("last_pos contents: ", map[the_end[1]][the_end[0]])

    


