import datetime
import re

UNFOLD_FACTOR = 5

# def verify(positions):
#     global required
#     p = 0
#     for r in required:
#         while positions[p] + ranges[p] < r[0]:
#             p += 1
#             if p == len(positions):
#                 return False
#         if positions[p] > r[0] or positions[p] + ranges[p] < r[1]:
#             return False
#     return True

def get_next_valid_pos(pos, span, last_pos):
    global row

    for i in range(pos, last_pos + 1):

        # ensure the previous character was not a span
        if i > 0 and row[i-1] == '#':
            continue
        range_end = i + span
        if range_end > len(row):
            return None, None
        valid = True
        for j in range(i, range_end):
            if row[j] == '.':
                valid = False
                break
        if valid and (range_end == len(row) or row[range_end] != '#'):
            return (i, range_end)
    return None, None  

def check_required(next_valid, next_end, last_required):
    new_last_required = last_required
    while new_last_required >= 0 and required[new_last_required][0] >= next_valid:
        if required[new_last_required][1] <= next_end:
            new_last_required -= 1
        else:
            return last_required, False
    return new_last_required, True

def get_sliding_positions(positions, slider, last_required):
    global row, ranges

    arrangements_found = 0
    new_positions = positions[:]
    pos = positions[slider]

    end_of_range = len(row) + 1
    if slider < len(positions) - 1:
        end_of_range = positions[slider + 1] 

    while pos + ranges[slider] < end_of_range:
        next_valid, next_end = get_next_valid_pos(pos, ranges[slider], end_of_range)

        if next_valid is None or next_end >= end_of_range:
            return arrangements_found
        
        new_positions[slider] = next_valid
        pos = next_valid + 1

        # check if one or more last-required spans are correctly covered
        new_last_required, is_valid = check_required(next_valid, next_end, last_required)
        if not is_valid:
            continue

        if slider > 0:
            arrangements_found += get_sliding_positions(new_positions, slider - 1, new_last_required)
        else:
            # confirm all required ranges were covered
            if new_last_required == -1:
                # print("found a sliding position at ", new_positions)
                arrangements_found += 1
    return arrangements_found

def count_arrangements():
    global row, ranges

    positions = []
    pos = 0
    for i in range(len(ranges)):
        min_ranges_span = sum(ranges[i:]) + len(ranges[i:]) - 1
        last_pos = len(row) - min_ranges_span
        pos, next_pos = get_next_valid_pos(pos, ranges[i], last_pos)
        positions.append(pos)
        pos = next_pos + 1

    print("starting positions {}".format(positions))

    return get_sliding_positions(positions, len(ranges)-1, len(required) - 1)

total_arrangements = 0
with open("12/input.txt", "r") as input:
    records = [l.strip().split(' ') for l in input]
    for rec in records:
        arrangements = 0
        row = "?".join([rec[0]] * UNFOLD_FACTOR)
        ranges = ",".join([rec[1]] * UNFOLD_FACTOR)
        ranges = [int(r) for r in ranges.split(',')]
        required = [m.span() for m in re.finditer("#+", row)]
        print("[{}] row {} and ranges {} and required {}".format(datetime.datetime.now(),row, ranges, required))
        arrangements += count_arrangements()
        print("arrangements = ", arrangements, flush=True)
        total_arrangements += arrangements
    print("total arrangements = ", total_arrangements)
    