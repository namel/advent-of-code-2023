
MAP_LAYERS = 7
maps = [[] for i in range(MAP_LAYERS)]


def build_map(lines, current_line, layer):
    while current_line < len(lines) and len(lines[current_line]) > 1:
        new_map = lines[current_line].strip().split(" ")
        new_map = [int(n) for n in new_map]
        maps[layer].append(new_map)
        current_line += 1
    return current_line

# tuples are destination, source, range length
def lookup(n, layer):
    if len(maps) <= layer:
        return n
    next_num = n
    for (dest, source, range_len) in maps[layer]:
        if n >= source and n < source + range_len:
            offset = n - source
            next_num = dest + offset
            break
    print("lookup next level for value {}", layer, next_num)    
    return lookup(next_num, layer + 1)


with open("5/input.txt", "r") as input:
    lines = [l for l in input]
    seeds = lines[0].split(":")[1].strip().split(" ")
    seeds = [int(n) for n in seeds]
    current_line = 3

    for layer in range(0, MAP_LAYERS):
        current_line = build_map(lines, current_line, layer)
        current_line += 2
        print(maps[layer])

    locations = []
    for s in seeds:
        locations.append(lookup(s, 0))
        print("next seed!")
    print("seeds {} have locations {}".format(seeds, locations))
    locations.sort()
    print("lowest location is {}".format(locations[0]))
    