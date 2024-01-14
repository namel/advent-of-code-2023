START_RANGE, END_RANGE = 200000000000000, 400000000000000

class Stone:
    def __init__(self, l) -> None:
        self.px, self.py, self.pz = [int(u.strip()) for u in l[0].split(',')]
        self.vx, self.vy, self.vz = [int(u.strip()) for u in l[1].split(',')]

with open("24/input.txt") as input:
    stones = [Stone(l.strip().split('@')) for l in input]

def check_pairs(s1, s2):
    if (s1.vy * s2.vx - s1.vx *s2.vy) == 0 or (s2.vy * s1.vx - s2.vx *s1.vy) == 0:
        return False
    l1 = (s2.vy*(s2.px - s1.px) + s2.vx*(s1.py - s2.py)) / (s2.vy * s1.vx - s2.vx *s1.vy)
    l2 = (s1.vy*(s1.px - s2.px) + s1.vx*(s2.py - s1.py)) / (s1.vy * s2.vx - s1.vx *s2.vy)
    px, py = s2.px + s2.vx * l2, s2.py + s2.vy * l2
    return px >= START_RANGE and px <= END_RANGE and py >= START_RANGE and py <= END_RANGE and l2>0 and l1>0

pairs = [check_pairs(stones[s1], stones[s2]) for s1 in range(0, len(stones) - 1) for s2 in range(s1 + 1, len(stones))]
print(sum(pairs))
