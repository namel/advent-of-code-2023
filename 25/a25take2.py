from collections import defaultdict
from datetime import datetime
nodes = defaultdict(set)


def checkConfig(explore, s1, s2, chops, neighbors, new_disconnected, new_chops):
    new_connected = set(neighbors) - new_disconnected
    s1.update(new_connected)
    s2.update(new_disconnected)
    chops.update(new_chops)
    subgraph_check(explore | new_connected, s1, s2, chops)
    s1.difference_update(new_connected)
    s2.difference_update(new_disconnected)
    chops.difference_update(new_chops)    

def subgraph_check(explore, s1, s2, chops):

    if len(explore) == 0:
        if len(chops) == 3:
            print("Found! chops={} lengths({} = {} + {}) s1={} s2={}".format(chops, len(nodes), len(s1), len(s2), s1, s2))
        return
    
    n = explore.pop()
    if not s2.isdisjoint(nodes[n]):
        return
    neighbors = [n2 for n2 in nodes[n] if n2 not in s1 and n2 not in s2]

    # don't check 3-chops because it implies a trivial problem (only one element) or not worth checking
    # check all 2-chops permutations
    if len(chops) <= 1 and len(neighbors) >= 2:
        for chop1, chop2 in [(neighbors[n1], neighbors[n2]) for n1 in range(0, len(neighbors) - 1) for n2 in range(n1 + 1, len(neighbors))]:
            checkConfig(explore, s1, s2, chops, neighbors, { chop1, chop2 }, {(n, chop1), (n, chop2)})

    # check 1-chop permutations
    if len(chops) <= 2:
        for chop1 in neighbors:
            checkConfig(explore, s1, s2, chops, neighbors, { chop1 }, { (n, chop1) })

    # check no-chop permutations only if one chop already set
    # if len(chops) >= 1:
    if len(chops) == 0:
        print("[{}]: zero-chops at s1 size {}".format(datetime.now(), len(s1)))
    s1.update(neighbors)
    subgraph_check(explore | set(neighbors), s1, s2, chops)
    s1.difference_update(neighbors)


with open("25/smallinput.txt") as input:
    ll = [l.strip().split(':') for l in input]
    for n, nlist in ll:
        nlist = nlist.strip().split(' ')
        nodes[n].update(nlist)
        for n2 in nlist:
            nodes[n2].add(n)

subgraph_check({ list(nodes.keys())[0] }, { list(nodes.keys())[0] }, set(), set())

# after running this for 6 hours, I got Found! chops={('thl', 'nmv'), ('fzb', 'fxr'), ('mbq', 'vgk')} lengths(1550 = 759 + 3) (the 3 is wrong)
# so |s1|*|s2| = 759*791 = 600369
