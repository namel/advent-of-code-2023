import re
import datetime

UNFOLD_FACTOR = 5
prog = re.compile(r'#+')

def invalid_row(new_ranges, ranges):
    for i in range(len(new_ranges)):
        if new_ranges[i] != ranges[i]:
            return True
    return False

def check_comb(comb, row, ranges):
    new_ranges = []
    current_range = None
    wildcard = 0
    if comb % 1000000 == 0:
        print(".")
    # print("checking row {} for ranges {}".format(row,ranges))
    for i in range(len(row)):
        if row[i] == '?':
            if comb & 2**wildcard:
                if current_range is None:
                    current_range = 1
                else:
                    current_range += 1
            else:
                if current_range is not None:
                    new_ranges.append(current_range)
                    if invalid_row(new_ranges, ranges):
                        return 0
            wildcard += 1
        elif row[i] == '#':
            if current_range is None:
                current_range = 1
            else:
                current_range += 1
        else:
            if current_range is not None:
                new_ranges.append(current_range)
                if invalid_row(new_ranges, ranges):
                    return 0
            
    return int(not invalid_row(new_ranges, ranges))

def count_arrangements(row, ranges):
    arrangements = 0
    num_wildcards = 2 ** len([True for c in row if c == '?'])
    for comb in range(num_wildcards):
        arrangements += check_comb(comb, row, ranges)
    print("[{}] arrangements count = {}".format(datetime.datetime.now(), arrangements))
    return arrangements        

total_arrangements = 0
with open("12/smallinput.txt", "r") as input:
    records = [l.strip().split(' ') for l in input]
    for rec in records:
        unfolded_rec = "?".join([rec[0]] * UNFOLD_FACTOR)
        ranges = ",".join([rec[1]] * UNFOLD_FACTOR)
        unfolded_ranges = [int(r) for r in ranges.split(',')]
        total_arrangements += count_arrangements(unfolded_rec, unfolded_ranges)

print("total arrangements = ", total_arrangements)