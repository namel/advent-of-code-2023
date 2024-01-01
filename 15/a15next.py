from functools import reduce
from itertools import chain

def hash_asc(s, prev=0):
    return reduce(lambda acc, c: ((acc + ord(c)) * 17) % 256, s, prev)

with open("15/input.txt", "r") as input:
    lines = [l.strip() for l in input]
    entries = [l.split(',') for l in lines]
    entries = list(chain(*entries))

    boxes = [[] for n in range(256)]
    lenses = {}
    for e in entries:
        is_add_op = '=' in e
        lens_op = e.split('=' if is_add_op else '-')
        label = lens_op[0]
        focal_length = int(lens_op[1]) if lens_op[1].isnumeric() else 0
        boxid = hash_asc(label)
        lenses[label] = focal_length

        if is_add_op:
            if label not in boxes[boxid]:
                boxes[boxid].append(label)
        else:
            if label in boxes[boxid]:
                pos = boxes[boxid].index(label)
                boxes[boxid] = boxes[boxid][:pos] + (boxes[boxid][pos+1:] if pos + 1 < len(boxes[boxid]) else [])
        
    focus_power = 0
    for boxid, b in enumerate(boxes):
        for lens_pos, lens in enumerate(b):
            focus = (boxid + 1) * (lens_pos + 1) * lenses[lens]
            focus_power += focus

    print(focus_power)
    