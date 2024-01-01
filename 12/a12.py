import re

def count_arrangements(row, ranges):
    arrangements = 0
    num_wildcards = 2 ** len([True for c in row if c == '?'])
    print("checking row {} for ranges {}".format(row,ranges))
    for comb in range(num_wildcards):
        new_row = ""
        wildcard = 0
        for i in range(len(row)):
            if row[i] == '?':
                new_row += '#' if comb & 2**wildcard else '.'
                wildcard += 1
            else:
                new_row += row[i]
        ranges_found = re.findall(r'#+', new_row)
        ranges_found = [len(r) for r in ranges_found]
        if tuple(ranges_found) == tuple(ranges):
            # print("row {} is good".format(new_row))
            arrangements += 1
    return arrangements        

total_arrangements = 0
with open("12/input.txt", "r") as input:
    records = [l.strip().split(' ') for l in input]
    for rec in records:
        ranges = [int(r) for r in rec[1].split(',')]
        total_arrangements += count_arrangements(rec[0], ranges)

print("total arrangements = ", total_arrangements)