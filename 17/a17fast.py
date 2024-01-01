from datetime import datetime
import pickle

POS_MOVE = { 'N': (0, -1), 'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
POS_NEXT = { 'N': ['W', 'N', 'E'], 'W': ['S', 'W', 'N'], 'S': ['E', 'S', 'W'], 'E': ['N', 'E', 'S'] }
DUMP_FREQ = 2**28
MAX_TWIST = 4
MAX_OVER = 5
USE_MAP = True

def move_pos(pos, dir):
    return (pos[0] + POS_MOVE[dir][0], pos[1] + POS_MOVE[dir][1])

def get_heat(pos):
    return int(lines[pos[1]][pos[0]])

def was_reached(pos, new_val):
    last_val = map[pos[1]][pos[0]]
    if last_val is None or new_val < last_val:
        map[pos[1]][pos[0]] = new_val
        return False
    return new_val > last_val + MAX_OVER

# travel from "pos" along direction "dir"
# dir_count: the distance travelled in a straight line
# heat_acc: heat accumulated so far
def travel(pos, dir, dir_count, heat_acc, twist, depth):
    global map, min_heat_path, counter

    counter += 1
    if counter % DUMP_FREQ == 0:
        print("dumping map")
        with open('data.pickle', 'wb') as f:
            pickle.dump(map, f)

    next_positions = [(move_pos(pos, next_dir), next_dir, i - 1) for i, next_dir in enumerate(POS_NEXT[dir])]
    for next_pos, next_dir, new_twist in next_positions:
        if next_pos[0] < 0 or next_pos[0] >= len(map[0]) \
            or next_pos[1] < 0 or next_pos[1] >= len(map) \
            or abs(twist + new_twist)> MAX_TWIST \
            or (next_dir == dir and dir_count == 2):
            continue
        new_heat_acc = heat_acc + get_heat(next_pos)
        if was_reached(next_pos, new_heat_acc) or new_heat_acc > min_heat_path:
            continue
        if next_pos == the_end:
            if new_heat_acc < min_heat_path:
                print("found a path with energy {}".format(new_heat_acc))
                min_heat_path = new_heat_acc
            return
        if depth<6:
            print("[{}]expoloring depth {} seq {}-{}".format(datetime.now(), depth, dir, next_dir))
        if next_dir == dir:
            travel(next_pos, next_dir, dir_count + 1, new_heat_acc, twist, depth + 1)
        else:
            travel(next_pos, next_dir, 0, new_heat_acc, twist + new_twist, depth + 1)


with open("17/input.txt", "r") as input:
    lines = [l.strip() for l in input]
    map = [[None for i in range(len(lines[0]))] for j in range(len(lines))]
    the_end = (len(lines[0]) - 1, len(lines) - 1)
    counter = 0

    # find a starting path
    min_heat_path = 0
    pos = (0,0)
    while pos != the_end:
        if pos[0] + 1 < len(map[0]):
            pos = move_pos(pos, 'E')
            min_heat_path += get_heat(pos)
        if pos[1] + 1 < len(map) and pos != the_end:
            pos = move_pos(pos, 'S')
            min_heat_path += get_heat(pos)
    print("zig zag path has heat ", min_heat_path)

    # found in a previous execution
    min_heat_path = 847

    # old map
    if USE_MAP:
        print("loading map")
        with open('data.pickle', 'rb') as f:
            map = pickle.load(f)

    travel((0,0), 'S', dir_count=0, heat_acc=0, twist=0, depth=0)
    travel((0,0), 'E', dir_count=0, heat_acc=0, twist=0, depth=0)
    print("[{}] lowest energy path = {}".format(datetime.now(), min_heat_path))