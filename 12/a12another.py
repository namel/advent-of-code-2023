import re
import datetime
import random

UNFOLD_FACTOR = 5
prog = re.compile(r'#+')
row = ""
ranges = []
counter = 0


def check_paths(prev_acc, is_in_sequence, pos):
    global row, ranges, counter

    counter += 1
    if counter % 2**28 == 0:
        print("[{}] I'm looking at acc={} pos={} ranges={} ".format(datetime.datetime.now(), prev_acc, pos, ranges))

    seq_acc = prev_acc[:]
    if pos == len(row):
        return int(seq_acc == ranges)
    
    if row[pos] == '.':
        if is_in_sequence:
            if seq_acc != ranges[:len(seq_acc)]:
                return 0
            remaining_ranges = ranges[len(seq_acc):]
            if pos + sum(remaining_ranges) + len(remaining_ranges) - 1 > len(row):
                return 0
        return check_paths(seq_acc, False, pos+1)
    
    if row[pos] == '#':
        if is_in_sequence:
            seq_acc[-1] += 1
            if seq_acc[-1] > ranges[len(seq_acc) - 1]:
                return 0
        else:
            seq_acc.append(1)
        return check_paths(seq_acc, True, pos+1)
    
    sub_counts = 0
    # handle case of '.'
    if is_in_sequence:
        if seq_acc == ranges[:len(seq_acc)]:
            sub_counts += check_paths(seq_acc, False, pos+1)
    else:
        sub_counts += check_paths(seq_acc, False, pos+1)

    # handle case of '#'
    if is_in_sequence:
        seq_acc[-1] += 1
        if len(seq_acc) <=len(ranges) and seq_acc[-1] <= ranges[len(seq_acc) - 1]:
            sub_counts += check_paths(seq_acc, True, pos+1)
    else:
        seq_acc.append(1)
        sub_counts += check_paths(seq_acc, True, pos+1)

    return sub_counts


def count_arrangements():
    arrangements = check_paths([], False, 0)
    print("[{}] arrangements count = {}".format(datetime.datetime.now(), arrangements))
    return arrangements        

total_arrangements = 0
with open("12/input.txt", "r") as input:
    records = [l.strip().split(' ') for l in input]
    for rec in records:
        row = "?".join([rec[0]] * UNFOLD_FACTOR)
        ranges = ",".join([rec[1]] * UNFOLD_FACTOR)
        ranges = [int(r) for r in ranges.split(',')]
        total_arrangements += count_arrangements()

print("total arrangements = ", total_arrangements)