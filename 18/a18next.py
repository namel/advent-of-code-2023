from collections import namedtuple

# 0 means R, 1 means D, 2 means L, and 3 means U
POS_MOVE = { 3: (0, -1), 1: (0, 1), 2: (-1, 0), 0: (1, 0)}

move_list = []

RangeDesc = namedtuple('RangeDesc', ('top_left', 'bottom_right', 'distance', 'is_horizontal'))

def move_pos(pos, dir, dist=1):
    return (pos[0] + POS_MOVE[dir][0]*dist, pos[1] + POS_MOVE[dir][1]*dist)

def get_incident_ranges(row):
    incident_ranges = {}
    for r in ranges:
        if row >= r.top_left[1] and row <= r.bottom_right[1]:
            col = r.top_left[0]
            if col not in incident_ranges:
                incident_ranges[col] = []
            incident_ranges[col].append(r)
    incident_ranges_list = list(incident_ranges.items())
    incident_ranges_list.sort(key = lambda x: x[0])
    return [r[1] for r in incident_ranges_list]

def get_corner_sig(horizontal, vertical):
    if horizontal.top_left == vertical.top_left:
        return '┌'
    if horizontal.top_left == vertical.bottom_right:
        return '└'
    if horizontal.bottom_right == vertical.top_left:
        return '┐'
    return '┘'

with open("18/input.txt", "r") as input:

    # collect lines
    for line in input:
        l = line.strip()
        dir, dist, color = tuple(line.split(' '))
        code = int(color.strip("()#\n"), 16)
        dir, dist = code % 16, code // 16
        move_list.append((dir, dist))
    
    # get top-right corner
    pos, min_pos, max_pos=(0,0), (0,0), (0,0)

    # each entry in a map has (pos, len, range_id)
    ranges = []
    for m in move_list:
        dir, dist = m
        new_pos = move_pos(pos, dir, dist)
        top_left = (min(pos[0], new_pos[0]), min(pos[1], new_pos[1]))
        bottom_right = (max(pos[0], new_pos[0]), max(pos[1], new_pos[1]))
        r = RangeDesc(top_left, bottom_right, dist + 1, top_left[1] == bottom_right[1])
        ranges.append(r)
        max_pos = (max(max_pos[0], bottom_right[0]), max(max_pos[1], bottom_right[1]))
        min_pos = (min(min_pos[0], top_left[0]), min(min_pos[1], top_left[1]))
        pos = new_pos
    offset = (abs(min_pos[0]), abs(min_pos[1]))
    print("rows [{},{}]".format(min_pos[1], max_pos[1] + 1))

    # go one row at a time
    total_area = 0
    for row in range(min_pos[1], max_pos[1] + 1):

        if row % 10**6 == 0:
            print("at row: ", row)
        is_inside = False
        area = 0
        last_empty_col = min_pos[1]
        corner_sig = None
        horizontal = None

        # for each incident range, pre-sorted by col
        for ranges_at_col in get_incident_ranges(row):

            r = ranges_at_col[0]
            col = r.top_left[0]

            if corner_sig is None and is_inside:
                area += col - last_empty_col

            # only one range found at column implies either (1) vertical wall (2) the completion of a horizontal range
            if len(ranges_at_col) == 1:
                last_empty_col = col + 1
                area += 1

                # if this is the ending corner of a horizontal range
                if corner_sig is not None:      
                    if (corner_sig, get_corner_sig(horizontal, r)) in [('└', '┐'), ('┌', '┘') ]:
                        is_inside = not is_inside
                    corner_sig = None    
                    continue

                is_inside = not is_inside
                continue
            
            horizontal = [r for r in ranges_at_col if r.is_horizontal][0]
            vertical = [r for r in ranges_at_col if not r.is_horizontal][0]

            corner_sig = get_corner_sig(horizontal, vertical)
            area += horizontal.distance - 1

        # print("row {} has counted {} ".format(row, area))
        total_area += area

    print("total area = ", total_area)

            

