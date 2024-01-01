import re

with open("8/input.txt", "r") as input:
    lines = [l for l in input]
    directions = lines[0].strip()
    node_data = [re.findall(r'[A-Z]+', l) for l in lines[2:]]
    nodes = {nd[0]:(nd[1], nd[2]) for nd in node_data}

    cycles = 0
    pos = "AAA"
    while pos != "ZZZ":
        for step in directions:
            if step == "L":
                pos = nodes[pos][0]
            else:
                pos = nodes[pos][1]
        cycles += 1
    
print("cycles = {} total steps = {}".format(cycles, cycles * len(directions)))
