from sympy import solve, Symbol, Eq


START_RANGE, END_RANGE = 200000000000000, 400000000000000

class Stone:
    def __init__(self, l) -> None:
        self.px, self.py, self.pz = [int(u.strip()) for u in l[0].split(',')]
        self.vx, self.vy, self.vz = [int(u.strip()) for u in l[1].split(',')]

with open("24/input.txt") as input:
    stones = [Stone(l.strip().split('@')) for l in input]


# px1, py1, pz1, vx1, vy1, vz1, t1 = Symbol('px1'), Symbol('py1'), Symbol('pz1'), Symbol('vx1'), Symbol('vy1'), Symbol('vz1'), Symbol('t1')
pxr, pyr, pzr, vxr, vyr, vzr = Symbol('pxr'), Symbol('pyr'), Symbol('pzr'), Symbol('vxr'), Symbol('vyr'), Symbol('vzr')
tsym = [Symbol('t'+str(i)) for i in range(0, 10)]

equations = []
for i in range(0, 3):
    s, t = stones[i], tsym[i]
    equations.append(Eq(s.px + s.vx*t, pxr +vxr*t))
    equations.append(Eq(s.py + s.vy*t, pyr +vyr*t))
    equations.append(Eq(s.pz + s.vz*t, pzr +vzr*t))

sol = solve(equations)
print(sol)






