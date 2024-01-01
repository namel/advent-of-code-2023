from functools import reduce
from itertools import chain

def hash_asc(s, prev=0):
    return reduce(lambda acc, c: ((acc + ord(c)) * 17) % 256, s, prev)

with open("15/input.txt", "r") as input:
    lines = [l.strip() for l in input]
    entries = [l.split(',') for l in lines]
    entries = list(chain(*entries))
    print(entries)

    sum_hashes = reduce(lambda acc, e: (acc + hash_asc(e)), entries, 0)
    print(sum_hashes)
    