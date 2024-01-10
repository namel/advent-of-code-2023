class Brick:
    def __init__(self, start, end) -> None:
        self.start, self.end, self.aboves, self.belows = start, end, set(), set()

    def __repr__(self) -> str:
        return "Brick: {}→{} {}".format(self.start, self.end, len(self.aboves))   
    
    def drop(self, z) -> None:
        self.start = (self.start[0], self.start[1], self.start[2] - z)
        self.end = (self.end[0], self.end[1], self.end[2] - z)

def xy_pos(b):
    if b.start[0] != b.end[0]:
        return [(x, b.start[1]) for x in range(b.start[0], b.end[0] + 1)]
    if b.start[1] != b.end[1]:
        return [(b.start[0], y) for y in range(b.start[1], b.end[1] + 1)]
    return [(b.start[0], b.start[1])]

def process_brick(b):
    global lowest_coverage

    # drop brick to lowest level coverage allows, recording touches to both entry (below->above and above->below)
    covered = [lowest_coverage[x][y] for x,y in xy_pos(b)]
    prev_level = max(covered, key = lambda c:c[1])[1]
    b.belows = set([below[0] for below in covered if below[1] == prev_level and below[0] is not None])
    brick_height = b.end[2] - b.start[2] + 1
    b.drop(b.start[2] - prev_level - 1)

    # update bricks that are holding this one
    for sub_brick in b.belows:
        sub_brick.aboves.add(b)

    # update the coverage map
    for x, y in xy_pos(b):
        lowest_coverage[x][y] = (b, prev_level + brick_height)

with open("22/input.txt") as input:
    bricks_l = [l.strip().split('~') for l in input]
    bricks_tup = [(p1.split(',') ,p2.split(',')) for p1, p2 in bricks_l]
    bricks = [Brick(tuple([int(x1) for x1 in p1]), tuple([int(x2) for x2 in p2])) for p1, p2 in bricks_tup]

# x-y map of lowest impact. Each entry is tuple (brick, top height)
lowest_coverage = [[(None, 0) for x in range(10)] for y in range(10)]
highest_z = max([b.end[2] for b in bricks])
for z in range(1, highest_z+1):
    at_level = [b for b in bricks if b.start[2] == z]
    for b in at_level:
        process_brick(b)

total = 0
for b in bricks:
    if 1 not in [len(a.belows) for a in b.aboves]:
        total += 1
print("\ntotal removable = ", total)
