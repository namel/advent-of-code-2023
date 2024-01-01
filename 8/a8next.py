import re

with open("8/input.txt", "r") as input:
    lines = [l for l in input]
    directions = lines[0].strip()
    node_data = [re.findall(r'[1-9A-Z]+', l) for l in lines[2:]]
    nodes = {nd[0]:(nd[1], nd[2]) for nd in node_data}
    positions = [n for n in nodes.keys() if n[2] == "A"]

    cycles = 0
    
    for pos in positions:
        p = pos
        cycles = 0
        while p[2] != "Z":
            for step in directions:
                if step == "L":
                    p = nodes[p][0]
                else:
                    p = nodes[p][1]
            cycles += 1
        print("pos {} completes after {} cycles, or {} steps".format(pos, cycles, cycles * len(directions)))
        

# the above reveals how many cycles for each one of the 6:
# pos MSA completes after 53 cycles, or 14893 steps
# pos AAA completes after 73 cycles, or 20513 steps
# pos PKA completes after 79 cycles, or 22199 steps
# pos NBA completes after 71 cycles, or 19951 steps
# pos RHA completes after 61 cycles, or 17141 steps
# pos CDA completes after 43 cycles, or 12083 steps


# finding the number of cycles that will have all 6 terminate in Z, is the same
# as finding the number which is divisible by the numbers above
# but guess what, they are all prime numbers !  (the cycles)
# so the number of cycles where they meet is 53*73*79*71*61*43=
# 56922302683
# the number of steps is 281 times that
# 15995167053923



# actually running them in parallel is a BAD IDEA !!
# the code runs forever (well, not really, but many hours?)
    # while len([p for p in positions if p[2] != "Z"]) > 0 :
    #     for step in directions:
    #         if step == "L":
    #             positions = [nodes[p][0] for p in positions]
    #         else:
    #             positions = [nodes[p][1] for p in positions]
    #     cycles += 1
# print("cycles = {} total steps = {}".format(cycles, cycles * len(directions)))
